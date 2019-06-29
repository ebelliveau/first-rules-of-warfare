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


def main():
	mag = Magazine("https://www.youtube.com/channel/UCZFipeZtQM5CKUjx6grh54g")
	mag.load()

	for video in mag.list_all():
		ammo = Ammunition(v=video.v, lang="en")
		ammo.prime()

		


if __name__ == '__main__':
	main()