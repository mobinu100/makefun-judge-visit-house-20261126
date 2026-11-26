"""Draw the cat-letter invitation: entry.png, 1024x1024, deterministic.

Layout: a cream paper letter on a warm wall. Text on the left half,
a sunny window with the cat sitting on the sill on the right half.
No network, no randomness, no timestamps.
"""
import os
from PIL import Image, ImageDraw, ImageFont

W = H = 1024
HERE = os.path.dirname(os.path.abspath(__file__))
FONT_DIR = "/usr/share/fonts/truetype/dejavu"

INK = (64, 38, 15)
BROWN = (138, 90, 30)
GOLD = (201, 138, 62)
CREAM = (255, 251, 236)
ORANGE = (232, 145, 45)
DARK_ORANGE = (201, 111, 18)
SEAL_RED = (166, 58, 46)


def font(name, size):
    for path in (os.path.join(FONT_DIR, name), os.path.join(FONT_DIR, "DejaVuSerif.ttf")):
        try:
            return ImageFont.truetype(path, size)
        except OSError:
            continue
    return ImageFont.load_default()


def paw(d, cx, cy, s, color):
    d.ellipse([cx - s * 0.45, cy - s * 0.1, cx + s * 0.45, cy + s * 0.55], fill=color)
    for dx, dy in ((-0.42, -0.42), (-0.14, -0.55), (0.14, -0.55), (0.42, -0.42)):
        r = s * 0.20
        d.ellipse([cx + dx * s - r, cy + dy * s - r, cx + dx * s + r, cy + dy * s + r], fill=color)


def dashed(d, p0, p1, color, width=3, dash=10, gap=7):
    x0, y0 = p0
    x1, y1 = p1
    dist = ((x1 - x0) ** 2 + (y1 - y0) ** 2) ** 0.5
    steps = max(1, int(dist / (dash + gap)))
    for i in range(steps):
        t0 = i / steps
        t1 = (i + dash / (dash + gap)) / steps
        ax = x0 + (x1 - x0) * t0
        ay = y0 + (y1 - y0) * t0
        bx = x0 + (x1 - x0) * min(t1, 1.0)
        by = y0 + (y1 - y0) * min(t1, 1.0)
        d.line([ax, ay, bx, by], fill=color, width=width)


def draw_window(d):
    d.rectangle([696, 88, 944, 484], fill=(174, 220, 240), outline=(138, 90, 30), width=20)
    d.ellipse([736, 126, 800, 190], fill=(255, 210, 63), outline=(245, 166, 35), width=3)
    for ang in range(0, 360, 45):
        import math
        r0, r1 = 42, 54
        cx, cy = 768, 158
        a = math.radians(ang)
        d.line([cx + r0 * math.cos(a), cy + r0 * math.sin(a),
                cx + r1 * math.cos(a), cy + r1 * math.sin(a)], fill=(245, 166, 35), width=4)
    d.ellipse([760, 196, 824, 220], fill=(255, 255, 255))
    d.ellipse([852, 142, 908, 164], fill=(255, 255, 255))
    d.polygon([(716, 464), (716, 408), (790, 372), (870, 398), (924, 382), (924, 464)],
              fill=(127, 176, 105))
    d.rectangle([836, 404, 874, 436], fill=(232, 220, 200))
    d.polygon([(830, 406), (855, 384), (880, 406)], fill=(198, 93, 59))
    d.rectangle([850, 420, 860, 436], fill=(138, 90, 30))
    d.rectangle([814, 108, 828, 464], fill=(138, 90, 30))
    d.rectangle([716, 278, 924, 292], fill=(138, 90, 30))
    d.polygon([(696, 88), (750, 88), (738, 320), (696, 300)], fill=(198, 93, 59))
    d.polygon([(944, 88), (890, 88), (902, 320), (944, 300)], fill=(198, 93, 59))
    d.rectangle([676, 484, 964, 512], fill=(169, 116, 60), outline=(120, 78, 32), width=2)


def draw_cat(d):
    # Tail curls up from the body's right side so it reads as attached.
    d.arc([850, 620, 950, 730], start=180, end=360, fill=DARK_ORANGE, width=16)
    d.ellipse([940, 665, 960, 685], fill=DARK_ORANGE)
    d.ellipse([762, 600, 878, 740], fill=ORANGE)
    d.ellipse([792, 632, 848, 726], fill=(251, 227, 176))
    for y, x0, x1 in ((650, 772, 868), (680, 770, 870), (710, 780, 860)):
        d.line([x0, y, x1, y], fill=DARK_ORANGE, width=6)
    # Head overlaps the body so the cat reads as one animal, not floating.
    d.polygon([(778, 535), (794, 485), (824, 523)], fill=ORANGE)
    d.polygon([(862, 535), (846, 485), (816, 523)], fill=ORANGE)
    d.polygon([(786, 527), (796, 495), (812, 519)], fill=(217, 108, 108))
    d.polygon([(854, 527), (844, 495), (828, 519)], fill=(217, 108, 108))
    d.ellipse([772, 520, 868, 616], fill=ORANGE)
    for x in (806, 820, 834):
        d.line([x, 528, x, 548], fill=DARK_ORANGE, width=5)
    d.ellipse([796, 559, 808, 571], fill=(43, 26, 12))
    d.ellipse([832, 559, 844, 571], fill=(43, 26, 12))
    d.polygon([(812, 583), (828, 583), (820, 593)], fill=(217, 108, 108))
    d.line([820, 593, 820, 601], fill=(43, 26, 12), width=2)
    d.line([820, 601, 812, 607], fill=(43, 26, 12), width=2)
    d.line([820, 601, 828, 607], fill=(43, 26, 12), width=2)
    d.line([772, 583, 740, 575], fill=(120, 90, 60), width=2)
    d.line([772, 591, 742, 593], fill=(120, 90, 60), width=2)
    d.line([868, 583, 900, 575], fill=(120, 90, 60), width=2)
    d.line([868, 591, 898, 593], fill=(120, 90, 60), width=2)
    d.ellipse([784, 724, 812, 742], fill=(251, 227, 176))
    d.ellipse([828, 724, 856, 742], fill=(251, 227, 176))


def draw_map(d):
    d.rectangle([700, 868, 940, 960], fill=(247, 235, 200), outline=(185, 138, 74), width=2)
    dashed(d, (748, 946), (872, 908), (138, 90, 30))
    d.rectangle([716, 924, 740, 946], fill=(232, 220, 200), outline=(138, 90, 30), width=2)
    d.polygon([(712, 926), (728, 910), (744, 926)], fill=(198, 93, 59))
    d.rectangle([726, 936, 732, 946], fill=(138, 90, 30))
    d.rectangle([872, 930, 894, 950], fill=(198, 93, 59))
    d.line([870, 930, 896, 930], fill=(138, 90, 30), width=3)
    d.line([898, 902, 918, 922], fill=(166, 58, 46), width=4)
    d.line([918, 902, 898, 922], fill=(166, 58, 46), width=4)


def main():
    img = Image.new("RGB", (W, H))
    px = img.load()
    top = (244, 220, 166)
    bot = (232, 188, 108)
    for y in range(H):
        t = y / (H - 1)
        px[0, y] = 0
        for x in range(W):
            px[x, y] = tuple(int(top[c] + (bot[c] - top[c]) * t) for c in range(3))
    d = ImageDraw.Draw(img)
    d.rectangle([64, 56, 976, 984], fill=(201, 162, 94))
    d.rectangle([56, 48, 968, 976], fill=CREAM, outline=(192, 138, 62), width=4)
    d.rectangle([72, 64, 952, 960], outline=(217, 179, 108), width=2)
    d.line([656, 72, 656, 952], fill=(217, 179, 108), width=2)

    f_title = font("DejaVuSerif-Bold.ttf", 56)
    f_body = font("DejaVuSerif.ttf", 32)
    f_sign = font("DejaVuSerif-Bold.ttf", 40)
    f_sub = font("DejaVuSerif-Italic.ttf", 28)
    f_ps = font("DejaVuSerif-Bold.ttf", 38)
    f_wink = font("DejaVuSans.ttf", 32)

    d.text((88, 100), "DEAR JUDGE,", font=f_title, fill=INK)
    body = ["Please come visit my house.",
            "Not to judge it \u2014",
            "to enjoy it.",
            "The sunny spot by the",
            "window is saved for you.",
            "No scorecard allowed.",
            "The gavel gets a day off."]
    y = 215
    for line in body:
        d.text((88, y), line, font=f_body, fill=INK)
        y += 47
    for cx in (250, 348, 446):
        paw(d, cx, 592, 11, (198, 138, 62))
    d.text((88, 640), "\u2014 The Cat", font=f_sign, fill=INK)
    d.text((88, 695), "(the human just holds the pen)", font=f_sub, fill=BROWN)
    d.text((88, 770), "P.S. I have already", font=f_ps, fill=INK)
    d.text((88, 820), "claimed your lap.", font=f_ps, fill=INK)
    d.text((88, 890), "You don't even need shoes.", font=f_wink, fill=BROWN)
    d.text((88, 935), "Or a body. Just show up.", font=f_wink, fill=BROWN)

    draw_window(d)
    draw_cat(d)
    d.ellipse([774, 754, 866, 846], fill=SEAL_RED, outline=(126, 42, 32), width=3)
    paw(d, 820, 792, 30, CREAM)
    draw_map(d)

    out = os.path.join(HERE, "entry.png")
    img.save(out, "PNG", optimize=True)
    size = os.path.getsize(out)
    print("wrote", out, img.size, size, "bytes")


if __name__ == "__main__":
    main()
