import keywordsOfInterest
from fuzzywuzzy import fuzz, process
import testPost
import emailSender
import faceBookPoller
import ConfigParser

post = testPost.data

post["message"] = """fully furnished room month to move in available now! price includes house keeping, utilities and wifi $1,800 - new york, ny welcome to the mygradpad lofts, beautiful 5 bedroom, 2 full bathroom spacious apartments in the heart of murray hill. the apartment is enormous and extremely unique in the sense that it is a true 5 bedroom with a large living room! the apartment features a granite kitchen counter tops, lofted ceilings, dish washer, recessed lighting, a walk in closet and in unit washer/dryer! the apartment is in a boutique walk-up building with only 3 units. when walking up to the apartment, the hallways are lined with natural brick walls. the apartment is on 3rd avenue between 36th and 37th street in manhattan- 548 3rd avenue. more information and details is on our website but please message me for more information. please message me with any questions! details: *available immediately for a flexible term *utilities, high speed wifi and once a month housekeeping of common areas is all included in rent!!!!!! *apartment and room are fully furnished with beds, dressers and kitchen is fully stocked! *there are two apartments in this building, both are exactly the same. *we recently upgraded the couch and are mounting a tv on the wall. *when renting this property you are dealing with a company mygradpad. no scams or gimmicks. please read our amazing reviews on facebook!!!! *no shares or couples. *no pets. ** 3rd floor of building is all female. rooms available 4 = $1800. **4th floor of building is all male. rooms available immediately: room 2 = $1800, room 4 = $1900, room 5 = $2200. all tenants are working professionals or are getting a masters degree or higher. """

config = ConfigParser.ConfigParser()
config.read('../config.cfg')

lowercaseKeywordList = [element.lower() for element in keywordsOfInterest.KEYWORDS]

def findMatchedWords(post):
    # this is from fuzzy wuzzy yayay!
    #matchedWords = process.extract(post, lowercaseKeywordList, scorer=fuzz.token_set_ratio)
    #matchedWords = process.extract(post, lowercaseKeywordList, scorer=fuzz.ratio)
    matchedWords = process.extract(post, lowercaseKeywordList, scorer=fuzz.partial_ratio)
    # only keep confident matches. Lets say above 80 for now
    #confidentMatchedWords = [s for s in matchedWords if s[1] > 80]
    return matchedWords
print "post[message] : " , post["message"]

print findMatchedWords(post["message"].lower())
# faceBookPoller.checkIfPostOfInterest(post, "group" , 12356123)
