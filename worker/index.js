// 502 Tinted: the website is static files in ./site. This Worker only handles POST /api/quote:
// it emails the quote request to Shane through Cloudflare Email Routing (free for verified addresses),
// then sends the visitor to /thank-you. Every other request is served straight from ./site.
import { EmailMessage } from "cloudflare:email";

const TO = "502tinted@gmail.com";        // must be a verified destination in Email Routing
const FROM = "quotes@502tinted.com";     // any address on 502tinted.com (Email Routing is enabled there)
const FIELDS = [
  ["name", "Name"], ["phone", "Phone"], ["email", "Email"], ["vehicle", "Vehicle"], ["service", "Service"],
  ["coverage", "Tint coverage"], ["film", "Film"], ["shade", "Shade"], ["detail_package", "Detailing package"],
  ["preferred_day", "Preferred day"], ["message", "Anything else"],
];

export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    if (url.pathname === "/api/quote") {
      if (request.method !== "POST") return Response.redirect(new URL("/get-a-quote", url).toString(), 303);
      return handleQuote(request, env, url);
    }
    return env.ASSETS.fetch(request);
  },
};

async function handleQuote(request, env, url) {
  const wantsJson = (request.headers.get("Accept") || "").includes("application/json");
  const reply = (ok, code) => wantsJson
    ? Response.json({ ok, error: ok ? undefined : code }, { status: ok ? 200 : 400 })
    : Response.redirect(new URL(ok ? "/thank-you" : `/get-a-quote?error=${code}#quote`, url).toString(), 303);

  let data = {};
  try {
    const type = request.headers.get("Content-Type") || "";
    if (type.includes("application/json")) data = await request.json();
    else (await request.formData()).forEach((v, k) => { if (typeof v === "string") data[k] = v; });
  } catch (e) {
    return reply(false, "bad-request");
  }
  if (data._honey) return reply(true);                       // bots fill the hidden field; pretend it worked
  const val = (k) => String(data[k] || "").replace(/\s+$/g, "").slice(0, 2000);
  if (!val("name") || !val("phone") || !val("vehicle")) return reply(false, "missing");

  try {
    await env.QUOTE_EMAIL.send(new EmailMessage(FROM, TO, buildMime(val, url.hostname)));
    return reply(true);
  } catch (e) {
    console.error("quote email failed", e && e.message);
    return reply(false, "send");
  }
}

function buildMime(val, host) {
  const oneLine = (s) => s.replace(/[\r\n]+/g, " ").trim();
  const name = oneLine(val("name")), vehicle = oneLine(val("vehicle")), email = oneLine(val("email"));
  const rows = FIELDS.filter(([k]) => val(k)).map(([k, label]) => [label, val(k)]);
  const text = "New quote request from " + host + "\n\n" + rows.map(([l, v]) => `${l}: ${v}`).join("\n") +
    "\n\nReply to this email or call/text the customer back.\n";
  const esc = (s) => s.replace(/[&<>"]/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));
  const html = `<div style="font-family:Arial,sans-serif;font-size:15px;color:#111">
<p style="font-size:17px"><strong>New quote request from ${esc(host)}</strong></p>
<table cellpadding="8" cellspacing="0" style="border-collapse:collapse;border:1px solid #ddd">${rows.map(([l, v]) =>
    `<tr><th align="left" style="background:#f4f4f4;border:1px solid #ddd;white-space:nowrap">${esc(l)}</th>` +
    `<td style="border:1px solid #ddd">${esc(v).replace(/\n/g, "<br>")}</td></tr>`).join("")}</table>
<p style="color:#555">Reply to this email or call/text the customer back.</p></div>`;
  const boundary = "502t-" + crypto.randomUUID();
  const replyTo = /^[^\s@<>"]+@[^\s@<>"]+\.[^\s@<>"]+$/.test(email) ? email : "";
  const subject = `New quote request: ${name} (${vehicle})`.slice(0, 180);
  const headers = [
    `From: "502 Tinted Website" <${FROM}>`,
    `To: <${TO}>`,
    replyTo ? `Reply-To: <${replyTo}>` : null,
    `Subject: ${encodeWord(subject)}`,
    `Date: ${new Date().toUTCString().replace("GMT", "+0000")}`,
    `Message-ID: <${crypto.randomUUID()}@502tinted.com>`,
    "MIME-Version: 1.0",
    `Content-Type: multipart/alternative; boundary="${boundary}"`,
  ].filter(Boolean);
  return headers.join("\r\n") + "\r\n\r\n" + [
    `--${boundary}`, "Content-Type: text/plain; charset=utf-8", "Content-Transfer-Encoding: base64", "", b64wrap(text),
    `--${boundary}`, "Content-Type: text/html; charset=utf-8", "Content-Transfer-Encoding: base64", "", b64wrap(html),
    `--${boundary}--`, "",
  ].join("\r\n");
}

function b64(s) {
  const bytes = new TextEncoder().encode(s);
  let bin = "";
  for (let i = 0; i < bytes.length; i += 0x8000) bin += String.fromCharCode.apply(null, bytes.subarray(i, i + 0x8000));
  return btoa(bin);
}
function b64wrap(s) { return b64(s).replace(/.{1,76}/g, "$&\r\n").trimEnd(); }
function encodeWord(s) { return /^[\x20-\x7e]*$/.test(s) ? s : `=?UTF-8?B?${b64(s)}?=`; }
