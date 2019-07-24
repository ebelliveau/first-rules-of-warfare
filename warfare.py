#!/usr/bin/env python

'''
	warfare.py:

	A recurring theme in Isaac Arthur's YouTube channel (https://www.youtube.com/channel/UCZFipeZtQM5CKUjx6grh54g) is that
	he quotes "The first rule of warfare is..." and gives a brief description of varying warfare theatre scenarios.  This
	is a pretty constant theme across all of his videos (which are numerous), and I wanted to compile a list of all of his 
	"first rules", but didn't have the time to sit down and watch all of the videos again and listen for this phrase.

	This script is a direct result of that curiosity.  

	There's always more ways to skin a cat than are immediately visible.
'''

from models import Magazine, Ammunition
import sys, re

def get_channel_id(channel_string=""):
	return channel_string.replace("https://www.youtube.com/channel/", "").strip()

def main():
	channel_id = get_channel_id("https://www.youtube.com/channel/UCZFipeZtQM5CKUjx6grh54g")
	mag = Magazine(channel_id=channel_id)
	

	for video in mag.get_all_videos_in_channel(channel_id=channel_id):
		print(video)
		ammo = Ammunition(v=video.split("?v=")[1], lang="en")
		
		if ammo.prime() is True:
			pattern = "((\[Tt\]he first rule of warfare)+[\ A-Za-z,\.\;\"\']+\.\ \ )"
			spread = re.match(ammo.payload, pattern)

			if spread:
				emissions = re.findall(pattern, ammo.payload)
				for munition in emissions:
					print("Munition:  ", munition)

		else:
			exc = "Cannot process channel information!"
			print(exc)
			sys.exit(exc)




if __name__ == '__main__':
	main()