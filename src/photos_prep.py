"""One-time prep: turn Shane's phone photos and video into web files in assets/work/.
Writes <name>-1600.webp and <name>-800.webp (EXIF, including any GPS, is dropped), plus the hero reel."""
import os, subprocess, sys
from PIL import Image, ImageOps

UP = "/root/.claude/uploads/fba557de-8df6-5e45-b214-36df694bccd5"
OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "assets", "work")
SRC = {  # upload id -> web name
    "e9cc1754": "audi-q5-tint-red-bay",
    "bad77764": "toyota-tacoma-tint-shop-front",
    "575dc406": "range-rover-ceramic-tint",
    "f182f1a7": "windshield-film-install",
    "b4bb20f4": "kia-sportage-tint-shop-front",
    "3e0d82c4": "vw-tiguan-tint-hitek-bay",
    "a1ea32fa": "toyota-rav4-tint-side",
    "db442ef6": "chevy-suburban-tint-hitek-bay",
    "1ba29ea5": "toyota-rav4-detailing-sign",
    "99e79812": "white-suburban-tint-red-bay",
    "f691d7af": "vw-jetta-tint-gloss",
    "3f4ea093": "honda-crv-tint-5410-valley-station",
    "e0c8b984": "chevy-silverado-windshield-film",
    "308fbf59": "shane-crosier-502-tinted",
    # AI-generated example images (stand-ins until Shane sends real photos of these steps)
    "b55b58fb": "tint-removal-example",
    "3ee897e8": "foam-wash-example",
    "9bd5eb25": "interior-detail-example",
    "88b413cc": "iron-remover-example",
    "d0882d51": "paint-correction-5050-example",
}
CROPS = [  # (upload id, web name, crop box): one side-by-side image split into separate photos
    ("41d96f2b", "interior-before-example", (0, 0, 764, 1024)),
    ("41d96f2b", "interior-after-example", (772, 0, 1536, 1024)),
]

def prep(uid, name, box=None):
    src = next(os.path.join(UP, f) for f in os.listdir(UP) if f.startswith(uid))
    im = ImageOps.exif_transpose(Image.open(src)).convert("RGB")
    if box:
        im = im.crop(box)
    for w, q in ((1600, 68), (800, 66)):
        tw = min(w, im.width)                      # never upscale small photos
        h = round(im.height * tw / im.width)
        im.resize((tw, h), Image.LANCZOS).save(os.path.join(OUT, f"{name}-{w}.webp"), "WEBP", quality=q, method=6)

def main():
    os.makedirs(OUT, exist_ok=True)
    only = set(sys.argv[1:])                       # pass web names to prep just those photos
    for uid, name in SRC.items():
        if not only or name in only:
            prep(uid, name)
    for uid, name, box in CROPS:
        if not only or name in only:
            prep(uid, name, box)
    if only:
        return
    vid = next(os.path.join(UP, f) for f in os.listdir(UP) if f.endswith(".mp4"))
    reel = os.path.join(OUT, "expedition-reel.mp4")
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", vid, "-an", "-vf", "scale=540:-2", "-c:v", "libx264",
                    "-preset", "slow", "-crf", "29", "-pix_fmt", "yuv420p", "-movflags", "+faststart", reel], check=True)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", "0.3", "-i", vid, "-frames:v", "1", "-vf", "scale=540:-2",
                    os.path.join(OUT, "expedition-reel-poster.jpg")], check=True)
    Image.open(os.path.join(OUT, "expedition-reel-poster.jpg")).save(os.path.join(OUT, "expedition-reel-poster.webp"), "WEBP", quality=66)
    os.remove(os.path.join(OUT, "expedition-reel-poster.jpg"))
    for f in sorted(os.listdir(OUT)):
        print(f"{f:48} {os.path.getsize(os.path.join(OUT, f)) // 1024} KB")

if __name__ == "__main__":
    main()
