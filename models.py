#!/usr/bin/env python

class Magazine():
	"""
		An object for retrieving a list of videos on a YouTube channel.
	"""
	
	def __init__(self, channel_id=""):
		self._channel_id = channel_id
<<<<<<< HEAD
		self.api_key = "AIzaSyCR5ob2qQEEpFyG4qdU9IUfa3UjolOBKqE"
=======
		self.api_key = "LOL YEA RIGHT"
>>>>>>> 914b14f... Interim commit while I wait out the GData API restrictions.
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

		current_token = ""

		tokens_encountered = []

		while round < limit:
			print("Fetching meta for %s" % (url))
			print("Round = %d" % (round))
			resp = requests.get(url).json()

			print(resp)

			#print(resp)
			for i in resp['items']:
				try:
					if i['id']['kind'] == "youtube#video":
						video_links.append(base_video_url + i['id']['videoId'])
				except Exception as ex:
					print("Exception encountered in parsing video items:  %s" % (ex))
					round += 1
					break
<<<<<<< HEAD
			round += 1
			last_token = current_token
			print(video_links)
=======

			try:
				next_page_token = resp['nextPageToken']
				if next_page_token in tokens_encountered:
					print("Found the same token!!!")
					print(next_page_token, tokens_encountered, len(tokens_encountered))
					round = limit+1
					break
				url = first_url + '&pageToken={}'.format(next_page_token)

				tokens_encountered.append(next_page_token)

			except Exception as ex:
				print("Exception encountered:  %s " % (ex))
				round = limit+1
			
			for link in video_links:
				print(link.split("v=")[1])
>>>>>>> 914b14f... Interim commit while I wait out the GData API restrictions.
			#break #break after one iteration to not kill the API rate limits
			round += 1
		self.payload.append(video_links)
		return sorted(set(self.payload)) #sorted(set(video_links))

			

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