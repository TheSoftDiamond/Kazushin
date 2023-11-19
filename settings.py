import sys #Do not remove this line

##### AI SPECIFIC Settings #####

# AI's Name 
AINAME = 'AINAME'
# Conversation History
CONVERSATION_LIMIT = 10

### TTS SETTING ###
#For more info on this section, see https://cloud.google.com/text-to-speech/docs/voices

#Language Code
languageCode = "en-US"
#Name of Voice Model 
voiceName = "en-US-Polyglot-1"
#Gender (Accepts MALE/FEMALE)
ssmlGender = "MALE"

##### REDEEM DETECTION SETTINGS #####

# Should the bot listen for a specific redeem?
doRedeem = True
# Redeem ID
redeemID = ''

##### BITS DETECTION SETTINGS #####

# Should the bot listen for bits donations?
doBits = True
# Lower Bits Detection Number 
bitsLookAtLowNumber = 100
# Higher Bits Detection Number
bitsLookAtHighNumber = sys.maxsize
#Cooldown Timer in seconds
cooldownBits = 120
#Log to Twitch Chat?
bitsMessageLogChat = True

##### MESSAGE DETECTION SETTINGS #####

# Should we listen in for raw messages with the prefix?
doRawMessages = False
# AI NAME to Detect
detectMSGName = 'AINAME'
# Prefix
prefix = '!'
#Cooldown Timer in seconds
cooldownMsg = 120
#Log to Twitch Chat?
rawMessageLogChat = True

##### MESSAGE SPECIFIC SETTINGS #####

# Should the bot send messages to chat?
PostMSGtoChat = True
# Should block list be on?
blockList = False
# Profanity Filter Check
doProfanityCheck = True
# Minimum message length of message to AI to get a response (not related to message detection events)
globalminimumLength = 3
# Max Message Length (200-500), but would recommend leaving it at 500
globalmaximumLength = 500