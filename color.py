import pyautogui
import time
import os
from PIL import Image
from PIL import ImageGrab
from colormap import rgb2hex

fn = "bgd_img.png"

while 1:
	# Get cursor position
	pos = pyautogui.position()

	# Take screenshot and save 
	im = ImageGrab.grab()
	im.save(fn)

	# Open screen shot and convert
	image = Image.open(fn)
	rgb = image.convert("RGB").getpixel((pos[0],pos[1]))

	# Print RGB and hex code of pixel at cursor position
	print(rgb[0],rgb[1],rgb[2], rgb2hex(rgb[0],rgb[1],rgb[2]))

	# Remove the screenshot
	os.remove(fn)

	# Pause
	time.sleep(1)

