#!/usr/bin/env python

class Magazine():
	"""
		An object for retrieving a list of videos on a YouTube channel.
	"""
	def __init__(self, channel_string=""):
		self.channel_string = channel_string

	@property
	def channel_string(self):
		return self._channel_string

	def get_channel_id(self):
		if self.channel_string
	


class Ammunition(object):
	"""
		An object for pulling down and parsing subtitle XML from YouTube's gdata API
	"""
	import requests
	def __init__(self, v="", lang="en"):
		self._v = v
		self._lang = lang
		# Target = GData public URL to retrieve videoID's subtitles in XML format:
		self._target = "http://video.google.com/timedtext?lang=%s&v=%s" % (self.v, self.lang)
		# Charge = eventually-parsed flat text of the target.
		self.charge=""

	@property
	def v(self):
		return self._v
	
	@property
	def lang(self):
		return self._lang

	@property
	def target(self):
		return self._target
	
	

	def prime(self):
		if v is not None:
			payload = requests.get(self.target)

			

		else:
			return False