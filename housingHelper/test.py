import keywordsOfInterest
from fuzzywuzzy import fuzz, process
import testPost
import emailSender
import faceBookPoller
post = testPost.data
post["message"] = """
Room available August 25th in my NY apt. at !!! It's in a great location off of the M23 & L train two stops from Union Square in Midtown! Cool area, great restraunts and shops. Utilities are included. One bathroom (shared) with tub and shower, large bedroom (for rent) with 2 walk in closet, air conditioner and window. Kitchen has fridge with ice maker, dishwasher, gas oven and stove and microwave. security door system and garbage chute. Deposit required but refundable on move out if you leave all in good condition.
Let me know!
"""
import  ConfigParser

config = ConfigParser.ConfigParser()
config.read('../config.cfg')



faceBookPoller.checkIfPostOfInterest(post, "group" , 12356123)