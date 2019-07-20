# Create Android Launcher Icon from an image file.

import sys
import os
import shutil

from PIL import Image

OUTPUT_DIR = 'output'
ICON_NAME = 'ic_launcher.png'
ICON_MAP = {
  "mipmap-hdpi": 72,
  "mipmap-mdpi": 48,
  "mipmap-xhdpi": 96,
  "mipmap-xxhdpi": 144,
  "mipmap-xxxhdpi": 192,
}

if __name__ == '__main__':
  if len(sys.argv) < 2:
    sys.exit('Please specify an image file.')

  srcImage = Image.open(sys.argv[1])
  width, height = srcImage.size
  
  if os.path.isdir(OUTPUT_DIR):
    shutil.rmtree(OUTPUT_DIR)
    
  for key in ICON_MAP.keys():
    dstDir = os.path.join(OUTPUT_DIR, key)
    os.makedirs(dstDir)
    
    dstFile = os.path.join(dstDir, ICON_NAME)

    size = ICON_MAP[key]
    dstImage = srcImage.resize((size, size), Image.BICUBIC)
    dstImage.save(dstFile)
