(function () {
  // Open pages at the top (a host frame can restore an old scroll position)
  try { if ('scrollRestoration' in history) history.scrollRestoration = 'manual'; } catch (e) {}
  if (!location.hash) { window.scrollTo(0, 0); window.addEventListener('load', function () { window.scrollTo(0, 0); }); }
  var all = function (sel, root) { return Array.prototype.slice.call((root || document).querySelectorAll(sel)); };

  // Mobile menu (a checkbox may already drive it in the single-file preview)
  all('button.nav-toggle').forEach(function (t) {
    var nav = t.parentNode.querySelector('.nav');
    if (!nav) return;
    t.addEventListener('click', function () {
      var open = nav.classList.toggle('open');
      t.setAttribute('aria-expanded', open ? 'true' : 'false');
      var sr = t.querySelector('.sr'); if (sr) sr.textContent = open ? 'Close menu' : 'Menu';
    });
  });

  // Phone hero: the walkaround reel plays behind the headline (phones only, skipped for reduced motion and data saver)
  all('video.hero-reel').forEach(function (reel) {
    var small = window.matchMedia('(max-width: 720px)').matches;
    var calm = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    var save = navigator.connection && navigator.connection.saveData;
    if (small && !calm && !save && reel.dataset.src) {
      reel.src = reel.dataset.src;
      var p = reel.play(); if (p && p.catch) p.catch(function () {});
    }
  });

  // Gallery: open a photo bigger
  var lb = document.querySelector('dialog.lb');
  if (lb && lb.showModal) {
    var lbImg = lb.querySelector('img');
    all('[data-lb]').forEach(function (a) {
      a.addEventListener('click', function (e) {
        e.preventDefault();
        var inner = a.querySelector('img');
        lbImg.src = a.getAttribute('href'); lbImg.alt = inner ? inner.alt : '';
        lb.showModal();
      });
    });
    lb.querySelector('.lb-x').addEventListener('click', function () { lb.close(); });
    lb.addEventListener('click', function (e) { if (e.target === lb) lb.close(); });
  }

  // Today's hours in Louisville time (mirrors the Google Business Profile)
  var HOURS = { 1: [9, 15], 2: [9, 15], 3: [10, 17], 4: [9, 15], 5: [9, 15], 6: [8, 13] };
  var NAMES = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'];
  function h12(h) { return (h > 12 ? h - 12 : h) + (h < 12 ? ' AM' : ' PM'); }
  var msg = null;
  try {
    var parts = new Intl.DateTimeFormat('en-US', { timeZone: 'America/New_York', weekday: 'short', hour: 'numeric', hour12: false }).formatToParts(new Date());
    var wd = { Sun: 0, Mon: 1, Tue: 2, Wed: 3, Thu: 4, Fri: 5, Sat: 6 }[parts.find(function (p) { return p.type === 'weekday'; }).value];
    var hr = Number(parts.find(function (p) { return p.type === 'hour'; }).value) % 24;
    var h = HOURS[wd];
    if (h && hr >= h[0] && hr < h[1]) msg = '<strong>Open now</strong>, until ' + h12(h[1]);
    else if (h && hr < h[0]) msg = 'Opens today at ' + h12(h[0]);
    else {
      var n = (wd + 1) % 7; while (!HOURS[n]) n = (n + 1) % 7;
      msg = 'Closed now. Opens ' + (n === (wd + 1) % 7 ? 'tomorrow' : NAMES[n]) + ' at ' + h12(HOURS[n][0]);
    }
  } catch (e) {}
  if (msg) all('[data-today]').forEach(function (el) { el.innerHTML = msg; });

  // Kentucky shade check (KRS 189.110): fronts 35%+, behind the driver 18%+ (8%+ on MPVs), film rated on clear glass
  all('[data-tool]').forEach(function (tool) {
    var st = { front: 35, rear: 20, veh: 'car' };
    var dark = function (v) { return (1 - v / 100).toFixed(2); };
    var out = function (k) { return tool.querySelector('[data-out="' + k + '"]'); };
    var render = function () {
      tool.style.setProperty('--tint-front', dark(st.front));
      tool.style.setProperty('--tint-rear', dark(st.rear));
      all('.chip', tool).forEach(function (b) {
        b.setAttribute('aria-pressed', String(Number(b.dataset.vlt) === st[b.dataset.group]));
      });
      var f = out('front'), r = out('rear'), min = st.veh === 'mpv' ? 8 : 18;
      if (st.front >= 35) { f.className = 'ok'; f.textContent = st.front + '% on the front doors is legal in Kentucky.'; }
      else { f.className = 'no'; f.textContent = st.front + '% is too dark for the front doors. Kentucky’s minimum is 35%.'; }
      if (st.rear >= min) { r.className = 'ok'; r.textContent = st.rear + '% behind the driver is legal' + (st.veh === 'mpv' ? ' on an SUV or van labeled MPV.' : ' on a car or truck.'); }
      else { r.className = 'no'; r.textContent = st.rear + '% is too dark behind the driver. The minimum is ' + min + '%' + (st.veh === 'mpv' ? ' on an MPV.' : ' on a car or truck' + (st.rear >= 8 ? ' (8% is only for SUVs and vans labeled MPV).' : '.')); }
    };
    all('.chip', tool).forEach(function (b) {
      b.addEventListener('click', function () { st[b.dataset.group] = Number(b.dataset.vlt); render(); });
    });
    all('input[type="radio"]', tool).forEach(function (i) {
      i.addEventListener('change', function () { st.veh = i.value; render(); });
    });
    render();
  });

  // Quote form: a normal form post to FormSubmit, which emails Shane and sends the visitor to /thank-you.
  // Swap for GlassFlow later.
  all('[data-qf]').forEach(function (form) {
    var q = new URLSearchParams(location.search).get('service');
    if (q) { var s = form.querySelector('[name="service"]'); Array.prototype.forEach.call(s.options, function (o) { if (o.text.toLowerCase().indexOf(q.toLowerCase()) === 0) s.value = o.text; }); }
    var status = form.querySelector('.qf-status');
    form.addEventListener('submit', function (ev) {
      var honey = form.querySelector('[name="_honey"]');
      if (honey && honey.value) { ev.preventDefault(); return; }
      if (form.dataset.preview) {
        ev.preventDefault();
        status.className = 'qf-status ok';
        status.textContent = 'Preview only: on the live site this request is emailed to 502tinted@gmail.com.';
        return;
      }
      var btn = form.querySelector('button[type="submit"]');
      setTimeout(function () { btn.disabled = true; btn.textContent = 'Sending…'; }, 0);
    });
  });
})();
