#!/usr/bin/env python


class Operator(xml.sax.ContentHandler):
	def __init__(self):
		self.current_data = ""
		self.orders = ""


	def startElement(self, tag, attributes):
		self.current_data = tag

		if self.current_data == "text":
			self.orders += attributes["text"].replace(". ", ".  ") # Make sure proper sentences are brought together with ".  " to give us a splittable target for regex.


class Magazine():
	"""
		An object for retrieving a list of videos on a YouTube channel.
	"""
	def __init__(self, channel_string=""):
		self.channel_string = channel_string
		self.api_key = "YEET"
		self.payload = []

	@property
	def channel_string(self):
		return self._channel_string

	def get_channel_id(self):
		return self.channel_string.replace("https://www.youtube.com/channel/", "").strip()

	def self.parse_video_id(self, video_string=""):
		return video_string.replace("https://www.youtube.com/watch?v=", "")

	def get_all_videos_in_channel(channel_id):
		import urllib
		import json
		api_key = self.api_key

		base_video_url = 'https://www.youtube.com/watch?v='
		base_search_url = 'https://www.googleapis.com/youtube/v3/search?'

		first_url = base_search_url + 'key={}&channelId={}&part=snippet,id&order=date&maxResults=25'.format(self.api_key, self.get_channel_id())

		video_links = []
		url = first_url
		while True:
			inp = urllib.urlopen(url)
			resp = json.load(inp)

		for i in resp['items']:
			if i['id']['kind'] == "youtube#video":
				video_links.append(base_video_url + i['id']['videoId'])
			try:
				next_page_token = resp['nextPageToken']
				url = first_url + '&pageToken={}'.format(next_page_token)
			except:
				break
		return video_links
			

class Ammunition(object):
	"""
		An object for pulling down and parsing subtitle XML from YouTube's gdata API
	"""
	import xml.sax as commander
	def __init__(self, v="", lang="en"):
		self._v = v
		self._lang = lang
		# Target = GData public URL to retrieve videoID's subtitles in XML format:
		self._target = "http://video.google.com/timedtext?lang=%s&v=%s" % (self.v, self.lang)
		# Charge = eventually-parsed flat text of the target.
		self.charge = ""

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
			parser = commander.make_parser()
			parser.setFeature(xml.sax.handler.feature_namespaces, 0)
			operator = Operator()
			parser.setContentHandler(operator)

			parser.parse(self.target)

			retrun True

		else:
			return False