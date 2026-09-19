#!/usr/bin/env python3
from pathlib import Path
from PIL import Image, ImageChops, ImageStat
import argparse

HERE = Path(__file__).resolve().parent.parent
OVERLAY = HERE / "templates" / "透明框.png"
BLANK = HERE / "templates" / "空白模板.png"
SIZE = (1254, 1254)
SAFE_BOX = (135, 315, 1120, 1030)

def white_background_to_alpha(im: Image.Image) -> Image.Image:
    """Remove a near-white studio background without changing product RGB pixels."""
    im = im.convert("RGBA")
    if im.getchannel("A").getextrema()[0] < 250:
        return im
    rgb = im.convert("RGB")
    # Estimate the background from the four corners.
    corners = Image.new("RGB", (4, 1))
    pts = [(0,0),(im.width-1,0),(0,im.height-1),(im.width-1,im.height-1)]
    for i,p in enumerate(pts): corners.putpixel((i,0), rgb.getpixel(p))
    bg = tuple(round(v) for v in ImageStat.Stat(corners).mean)
    diff = ImageChops.difference(rgb, Image.new("RGB", im.size, bg))
    # Strong alpha on real product pixels, soft alpha on original shadows.
    strength = diff.convert("L").point(lambda v: 0 if v <= 2 else min(255, (v-2)*12))
    im.putalpha(strength)
    box = strength.getbbox()
    return im.crop(box) if box else im

def render(product_path: Path, output_path: Path):
    product = white_background_to_alpha(Image.open(product_path))
    max_w = int((SAFE_BOX[2] - SAFE_BOX[0]) * 0.94)
    max_h = int((SAFE_BOX[3] - SAFE_BOX[1]) * 0.90)
    ratio = min(max_w / product.width, max_h / product.height)
    size = (max(1, round(product.width*ratio)), max(1, round(product.height*ratio)))
    product = product.resize(size, Image.Resampling.LANCZOS)

    canvas = Image.open(BLANK).convert("RGBA")
    x = SAFE_BOX[0] + ((SAFE_BOX[2]-SAFE_BOX[0])-product.width)//2
    y = SAFE_BOX[1] + ((SAFE_BOX[3]-SAFE_BOX[1])-product.height)//2
    canvas.alpha_composite(product, (x,y))
    canvas = Image.alpha_composite(canvas, Image.open(OVERLAY).convert("RGBA"))
    output_path.parent.mkdir(parents=True, exist_ok=True)
    canvas.save(output_path)

if __name__ == "__main__":
    p=argparse.ArgumentParser(description="套用康生固定产品图模板")
    p.add_argument("product",type=Path)
    p.add_argument("output",type=Path)
    a=p.parse_args(); render(a.product,a.output)
