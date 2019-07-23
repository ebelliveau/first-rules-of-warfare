#!/usr/bin/env python

class Magazine():
	"""
		An object for retrieving a list of videos on a YouTube channel.
	"""
	
	def __init__(self, channel_id=""):
		self._channel_id = channel_id
		self.api_key = "AIzaSyCR5ob2qQEEpFyG4qdU9IUfa3UjolOBKqE"
		self.payload = []

	def parse_video_id(self, video_string=""):
		return video_string.replace("https://www.youtube.com/watch?v=", "")

	def get_all_videos_in_channel(self, channel_id):
		import urllib
		import json
		import requests
		api_key = self.api_key

		base_video_url = "https://www.youtube.com/watch?v="
		base_search_url = "https://www.googleapis.com/youtube/v3/search?"

		first_url = base_search_url + 'key={}&channelId={}&part=snippet,id&order=date&maxResults=25'.format(self.api_key, channel_id)

		video_links = []
		url = first_url
		
		limit = 100
		round = 0

		last_token = "start"
		current_token = ""

		while round < limit:
			print("Fetching meta for %s" % (url))
			resp = requests.get(url).json()

			#print(resp)
			for i in resp['items']:
				if i['id']['kind'] == "youtube#video":
					video_links.append(base_video_url + i['id']['videoId'])
				try:
					next_page_token = current_token = resp['nextPageToken']
					url = first_url + '&pageToken={}'.format(next_page_token)
					if current_token is last_token:
						round = limit + 1
				except:
					round = limit + 1
					break
			round += 1
			last_token = current_token
			print(video_links)
			#break #break after one iteration to not kill the API rate limits
		return video_links

			

class Ammunition(object):
	"""
		An object for pulling down and parsing subtitle XML from YouTube's gdata API
	"""
	
	def __init__(self, v="", lang="en"):
		self._v = v
		self._lang = lang
		# Target = GData public URL to retrieve videoID's subtitles in XML format:
		self._target = "https://www.youtube.com/api/timedtext?v=%s&hl=%s&lang=%s&fmt=srv3" % (self.v, self.lang, self.lang)
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

		from lxml import etree as commander

		if self.v is not None and self.charge.strip() is not "":
			tree = commander.parse(self.target)
			self.charge = commander.tostring(tree, encoding='utf8', method='text')
			
			return True

		else:
			return False