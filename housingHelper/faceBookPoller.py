import facebook
from dateutil.parser import *
from datetime import datetime
import keywordsOfInterest
import emailSender
from fuzzywuzzy import fuzz, process
import dateutil.tz as tz
import  ConfigParser

config = ConfigParser.ConfigParser()
config.read('../config.cfg')


groups = {
    'art-gypsy-housing': '7030462319', #public
    #'not-gpysy-housing': '474569976042465', #closed
    'rent-sublet-share': '323359541058575', #public
    #'nyc-actor-sublet-connection': '6239548339', #closed
    #'gypsy-housing-avaible-new': '1438152599794284', #closed
    #'gpysy-housing-nyc': '1650616371871158', #closed
}


#token = facebook.GraphAPI().get_app_access_token(config.get('facebook_app', 'app_id'), config.get('facebook_app', 'app_secret'))
token = config.get('facebook', 'token')
#NOTICE THE GET INT HERE!! WE DO THIS BECASUE THIS IS AN INT
confidence_threshold = config.getint('fuzzywuzzy', 'confidence_threshold')
graph = facebook.GraphAPI(token)
previous_poll_time = datetime.now(tz.tzutc())
current_poll_time = datetime.now(tz.tzutc())
polling_offset = 30

lowercaseKeywordList = [element.lower() for element in keywordsOfInterest.KEYWORDS]

def findMatchedWords(post):
    #this is from fuzzy wuzzy yayay!
    #matchedWords = process.extract(post, lowercaseKeywordList, scorer=fuzz.token_set_ratio)
    matchedWords = process.extract(post, lowercaseKeywordList, scorer=fuzz.partial_ratio)
    #only keep confident matches. Lets say above 80 for now
    confidentMatchedWords = [s for s in matchedWords if s[1] > confidence_threshold]
    return confidentMatchedWords


def checkIfPostOfInterest(post, group, groupId):
	matchedWordsWithConfidence = findMatchedWords(post["message"].lower())
	if (len(matchedWordsWithConfidence) > 0):
		link = ''
		try:
			# try and get link.  If there is none fall back to the group name and id
			link = post['link']
		except KeyError:
			link = group + " " + groupId
		print "post is of interest %s , %s" % (matchedWordsWithConfidence, link)
		html = emailSender.formatMessage(post, group, groupId, matchedWordsWithConfidence)
		html = html.encode('utf-8')
		# lets just get the matched names.  We end up with a trailing comma and space so we remove the last 2 chars
		onlyMatchedWords = ''.join(e[0] + ", " for e in matchedWordsWithConfidence)[:-2]
		emailSender.sendEmail(html, onlyMatchedWords)


def poll():
	print "IN POLL "
	global current_poll_time
	global previous_poll_time
	global polling_offset
	#update the polling times
	previous_poll_time = current_poll_time
	current_poll_time=datetime.now(tz.tzutc())
	for groupName, groupId in groups.iteritems():
		url = groupId + "/feed?fields=message,created_time,updated_time,link&limit=10"
		test = graph.get_object(url)
		lower_time_limit = previous_poll_time
		for post in test["data"]:
			created_time = parse(post['created_time'])

			if (created_time > lower_time_limit):
				print "found new post in %s created at %s " % (groupName, created_time)
				checkIfPostOfInterest(post, groupName, groupId)

	print "done polling"
