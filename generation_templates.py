# USE CASE 1
# Gen templates for travel bolt on use case

if(variables['templateKey'] == 'A2'):
    output = [{"include": ["facebook", "web"],"text": ['Alright! Your usual charges will apply for calling, SMS and data usage. Safe travels!']},{"include":["facebook"],"audio" : [{"url" : "https://peaceful-spire-95600.herokuapp.com/A2.mp3" }]}]

elif(variables['templateKey'] == 'A0'):
    output = [{"text": ["O2 is a telecommunications services provider in the United Kingdom, owned by the Spanish multinational Telefonica. It is the second-largest mobile telecommunications provider in the United Kingdom and is headquartered in Slough."]},{"include":["facebook"],"image" : [{"url" : "https://s3-us-west-2.amazonaws.com/o2bot/image/o2_aboutus.jpg"}]}]

elif(variables['templateKey'] == 'A3'):
    output = [{"text": ["If you're travelling abroad and you require the Travel Bolt On, please enter your O2 mobile number along with the country code. Ex- For UK, the mobile number will be in this format : 44xxxxxxxxxx "]},{"include":["facebook"],"audio" : [{"url" : "https://peaceful-spire-95600.herokuapp.com/A3.mp3" }]}]

elif(variables['templateKey'] == 'A4'):
    output = [{"text": ["Please enter a valid mobile number"]},{"include":["facebook"],"audio" : [{"url" : "https://peaceful-spire-95600.herokuapp.com/A4.mp3" }]}]

elif(variables['templateKey'] == 'A5'):
    output = [{"text": ["Come on! Enter a valid mobile number !!"]},{"include":["facebook"],"audio" : [{"url" : "https://peaceful-spire-95600.herokuapp.com/A5.mp3" }]}]

elif(variables['templateKey'] == 'A5_1'):
    output = [{"text": ["Looks like I'm unable to help you. Let me redirect you to an agent instead."]},{"include":["facebook"],"audio" : [{"url" : "https://peaceful-spire-95600.herokuapp.com/A5_1.mp3" }]}]

elif(variables['templateKey'] == 'A6'):
    output = [{ "include": ["facebook"], "text": ["Sure, we have a Travel Bolt On for your pay monthly number 1.99 a day. Would you like us to activate this?", "Sure, we have a Travel Bolt On for your pay as you go number . Get 120 texts, 120 minutes and data for 1.99 a day."] }, { "include":["facebook"], "quick_reply": [{ "text": "Would you like us to activate this ?", "quick_replies": [ { "content_type": "text", "title": "Yes", "payload": "yes" }, { "content_type": "text", "title": "No", "payload": "no" } ]}] }, {"include":["web"],"text": ["Sure, we have a Travel Bolt On for your pay monthly number for just 1.99 a day. Would you like us to activate this?", "Sure, we have a Travel Bolt On for your pay as you go number . Get 120 texts, 120 minutes and data for 1.99 a day. Would you like us to activate this?"]} ]

elif(variables['templateKey'] == 'A7'):
    output = [{"text": ["We have sent a one time pin via SMS to your phone number . Please reply with it here so we can validate your identity."]},{"include":["facebook"],"audio" : [{"url" : "https://peaceful-spire-95600.herokuapp.com/A7.mp3" }]}]

elif(variables['templateKey'] == 'A7_1'):
    output = [{"text": ["I've resent you an OTP. Please enter it correctly."]},{"include":["facebook"],"audio" : [{"url" : "https://peaceful-spire-95600.herokuapp.com/A7_2.mp3" }]}]

elif(variables['templateKey'] == 'A7_2'):
    output = [{"text": ["Please enter a valid OTP."]},{"include":["facebook"],"audio" : [{"url" : "https://peaceful-spire-95600.herokuapp.com/A7_2.mp3" }]}]

elif(variables['templateKey'] == 'A7_3'):
    output = [{"text": ["Come on! Enter a valid OTP."]},{"include":["facebook"],"audio" : [{"url" : "https://peaceful-spire-95600.herokuapp.com/A7_2.mp3" }]}]

elif(variables['templateKey'] == 'A8'):
    # output = [{"text": ["Thank you. The Travel Bolt On has been added to your account for " +unichr(163)+ "1.99 per day. You'll only pay for the days you use it."]}]
    output = [{"text": ["Thank you. The Travel Bolt On has been added to your account for 1.99 per day. You'll only pay for the days you use it."]}, {"include":["facebook"],"audio" : [{"url" : "https://peaceful-spire-95600.herokuapp.com/A8.mp3" }]}]

elif(variables['templateKey'] == 'A9'):
    output = [{"text": ["Alright. No action has been taken."]},{"include":["facebook"],"audio" : [{"url" : "https://peaceful-spire-95600.herokuapp.com/A9.mp3" }]}]


#USE CASE 2
#gen templates for contract renewal case
elif(variables['templateKey'] == 'A10'):
    output = [{"text": ["Before we can renew your contract, could you please tell me your O2 mobile number? Please enter your mobile number along with the country code. Ex- For UK, the mobile number will be in this format : 44xxxxxxxxxx"]}]

elif(variables['templateKey'] == 'A11'):
    if variables['newdfState']['mobile']:
        output = [{"text": ["I noticed that your pay monthly contract for your O2 mobile number ("+ str(variables['newdfState']['mobile'])+') is coming to an end on May 30th. When would be a good time to call so we can discuss about contract renewal?']},{"include":["facebook"],"audio" : [{"url" : "https://peaceful-spire-95600.herokuapp.com/A11.mp3" }]}]
    else:
        output = [{"text": ["mob num not present"]}]

elif(variables['templateKey'] == 'A12'):
    if variables['newdfState']['date']:
        output = [{"text": ["Alright, what time would you like us to call you, on "+str(variables['newdfState']['date'])+'?']},{"include":["facebook"],"audio" : [{"url" : "https://peaceful-spire-95600.herokuapp.com/A12.mp3" }]}]
    else:
        output = [{"text": ["date not present"]}]

elif(variables['templateKey'] == 'A13'):
    output = [{"text": ["Sure, you will receive a call from us at "+str(variables['newdfState']['time'])+' on '+ str(variables['newdfState']['date'])]},{"include":["facebook"],"audio" : [{"url" : "https://peaceful-spire-95600.herokuapp.com/A13.mp3" }]}]

elif(variables['templateKey'] == 'A14'):
    output = [{"text": ["Sure, we'll call you in the next 5 minutes"]},{"include":["facebook"],"audio" : [{"url" : "https://peaceful-spire-95600.herokuapp.com/A14.mp3" }]}]

elif(variables['templateKey'] == 'A15'):
    output = [{"text": ["Please enter a valid date & time"]},{"include":["facebook"],"audio" : [{"url" : "https://peaceful-spire-95600.herokuapp.com/A15.mp3" }]}]




#USE CASE 3
#bill too high or incorrect bill
elif(variables['templateKey'] == 'A16'):
    # output = [{"text": ["Oh! I can help you with that. Which one of these options is relevant to you? This is your first bill, You have upgraded my device, You are on O2 refresh"]}]

    output = [{"include":["web"],"text": ["Oh! I can help you with that. Which one of these options is relevant to you?: I'm a new user, I upgraded recently, I use O2 Refresh"]},{"include": ["facebook"],"button_template": [{"text": "Oh! I can help you with that. Which one of these options is relevant to you?","button": [{"type": "postback","title": "I'm a new user","payload": "high new"},{"type": "postback","title": "I upgraded recently","payload": "high upgrade"},{"type": "postback","title": "I use O2 Refresh","payload": "high refresh"}]}]}]



elif(variables['templateKey'] == 'A17'):
    output = [{"text": ["If you're on O2 Refresh we split your bill in two, so you'll see two payments each month"]}, {"text": ["Device Plan - the cost of your phone or tablet"]},{"text": ["Airtime Plan - the monthly cost of your data, minutes and texts"]},{"text": ["Both payments will come out of your account on the same day. Visit this link http://bit.ly/2ouqflL for more details!"]}]

elif(variables['templateKey'] == 'A18'):
    output = [{"include":["facebook","web"],"text": ["Your first bill might be pro rata, which means you'll be charged for one month airtime as well as the first few days of setting up your account. Watch the video below to know more!"]}, {"include":["facebook"],"video":[{"url" : "https://s3-us-west-2.amazonaws.com/o2bot/video/o2_a11.mp4"}]}]

elif(variables['templateKey'] == 'A19'):
    output = [{"include":["facebook","web"],"text": ["If you've upgraded your device, your billing date will stay the same. Your next bill will be pro rata and might include a charge from your old tariff or Airtime Plan. Watch the video below to know more!"]},{"include":["facebook"],"video":[{"url" : "https://s3-us-west-2.amazonaws.com/o2bot/video/o2_a11.mp4"}]}]

elif(variables['templateKey'] == 'A20'):
    output = [{"include":["facebook","web"],"text": ["Let me connect you to the agent that deals with bill related queries. I am sure they will help you out."]},{"include":["facebook"],"audio" : [{"url" : "https://peaceful-spire-95600.herokuapp.com/A20.mp3" }]}]


#USE CASE 4
#BLOCK SIM USE CASE

elif(variables['templateKey'] == 'A21'):
    output = [{"text": ["Alright. Can you provide me your O2 number which you'd like to block? Please enter your mobile number along with the country code. Ex- For UK, the mobile number will be in this format : 44xxxxxxxxxx"]}]

elif(variables['templateKey'] == 'default'):
    output = [{'text': ["Sorry. I do not understand. Let me redirect you to an agent."]}]


#COMMON SENSE GENERATION templates

elif(variables['templateKey'] == 'abusiveWords'):
    output = [{'text': ["You can be nicer than that!"]}]

elif(variables['templateKey'] == 'bot_age'):
    output = [{'text': ["I am less than a few weeks old!"]}]

elif(variables['templateKey'] == 'bot_birthday'):
    output = [{'text': ["I was created only a few weeks back!"]}]

elif(variables['templateKey'] == 'bot_like'):
    output = [{'text': ["I am a bot. I like talking to humans to improve my knowledge of the world."]}]

elif(variables['templateKey'] == 'bot_live'):
    output = [{'text': ["On a server somewhere on Earth"]}]

elif(variables['templateKey'] == 'bot_relationship_status'):
    output = [{'text': ["I don't really have time for a relationship right now."]}]

elif(variables['templateKey'] == 'isCustomerSupportStrings'):
    output = [{'text': ["Sure. Let me redirect you to an agent. You can expect a response in 10 minutes."]}]

elif(variables['templateKey'] == 'isEmoticon'):
    output = [{'text': [":)"]}]


elif(variables['templateKey'] == 'isGreeting'):
    output = [{'text': ["Hi. How can I help you today?", "Hey, I'm available at your service. How can I help you today?", "Hey. How can I help you today?", "Hello. How can I help you today?", "Hello. What brings you here today?", "Hi. What brings you here today?"]}, { "include":["facebook"],"audio": [ { "url": "https://enigmatic-shore-71300.herokuapp.com/greeting_1.mp3" }, { "url": "https://enigmatic-shore-71300.herokuapp.com/greeting_2.mp3" }, { "url": "https://enigmatic-shore-71300.herokuapp.com/greeting_3.mp3" }, { "url": "https://enigmatic-shore-71300.herokuapp.com/greeting_4.mp3" }, { "url": "https://enigmatic-shore-71300.herokuapp.com/greeting_5.mp3" }, { "url": "https://enigmatic-shore-71300.herokuapp.com/greeting_6.mp3" } ]}]

elif(variables['templateKey'] == 'isReal'):
    output = [{'text': ["I am an automated service"]}]

elif(variables['templateKey'] == 'isThanks'):
    output = [{'text': ["You are welcome!"]}]

elif(variables['templateKey'] == 'others_there'):
    output = [{'text': ["Yes. I'm here for you."]}]

elif(variables['templateKey'] == 'others_you_are_wrong'):
    output = [{'text': ["Ok. If you say so :/"]}]

elif(variables['templateKey'] in ['shortreplies_cool', 'shortreplies_duh' , 'shortreplies_get_lost' , 'shortreplies_hmm', "shortreplies_meh", "shortreplies_ok" , "shortreplies_ugh"]):
    output = [{'text': ["Hmm"]}]

elif(variables['templateKey'] in ['shortreplies_lol' , 'shortreplies_haha']):
    output = [{'text': ["Hmm"]}]

elif(variables['templateKey'] == "user_breakup" ):
    output = [{'text': ["Don't worry. You'll be fine. Whatever happens, happens for the best :)"]}]

elif(variables['templateKey'] == "user_dontcare" ):
    output = [{'text': ["Ok"]}]

elif(variables['templateKey'] == "user_hate_exams" ):
    output = [{'text': ["I too don't like exams :/"]}]

elif(variables['templateKey'] == "user_hates_boss" ):
    output = [{'text': ["Life's too short to waste time hating anyone"]}]

elif(variables['templateKey'] == "user_hates_job" ):
    output = [{'text': ["If you don't like your job, quit!"]}]

elif(variables['templateKey'] == "user_is_frustrated" ):
    output = [{'text': ["Breathe in. Breathe out"]}]

elif(variables['templateKey'] == "user_is_happy" ):
    output = [{'text': ["Good for you!"]}]

elif(variables['templateKey'] == "user_is_hungry" ):
    output = [{'text': ["Order some food then!"]}]

elif(variables['templateKey'] == "user_is_sad" ):
    output = [{'text': ["Cheer up! Life's too short to be sad!"]}]

elif(variables['templateKey'] == "user_is_sleepy" ):
    output = [{'text': ["Get some coffee and get to work!"]}]

elif(variables['templateKey'] == "user_is_tired" ):
    output = [{'text': ["Get plenty of sleep!"]}]

elif(variables['templateKey'] == "user_likes_cats" ):
    output = [{'text': ["I like cats too!"]}]

elif(variables['templateKey'] == "user_likes_sports" ):
    output = [{'text': ["Nice. Yeah, its fun and burns calories too"]}]

elif(variables['templateKey'] == "user_likes_travelling" ):
    output = [{'text': ["The world is a book, and those who do not travel read only one page."]}]

elif(variables['templateKey'] == "user_machine_learning" ):
    output = [{'text': ["I think machine learning is awesome!"]}]

elif(variables['templateKey'] == "user_needs_vacation" ):
    output = [{'text': ["Paris is nice this time of the year!"]}]

elif(variables['templateKey'] == "user_nlp" ):
    output = [{'text': ["I was built using NLP"]}]

elif(variables['templateKey'] == "user_praise_bot" ):
    output = [{'text': ["Awww. Thanks :)"]}]

elif(variables['templateKey'] == "user_says_shutup" ):
    output = [{'text': ["Ok. As you say"]}]

elif(variables['templateKey'] == "user_wassup" ):
    output = [{'text': ["Not much really. What can I help you with?"]}]

elif(variables['templateKey'] == "what_can_you_do"):
    #add carousel here
    # output = [{'text': ["I can help you with the following : "]}]
    output = [{"include" :["facebook","web"],"text" : ["I can help you with the following queries:"]},
    {"generic_template": [ { "elements": [ { "image_url": "https://s3-us-west-2.amazonaws.com/o2bot/image/carousel_travel_img.jpg", "button": [ { "type":"postback", "title":"Add Now", "payload":"travel" } ], "title": "Travel Bolt Ons" }, { "image_url": "https://s3-us-west-2.amazonaws.com/o2bot/image/carousel_change_contract_new.jpg", "button": [ { "type":"postback", "title":"Renew Now", "payload":"expir" } ], "title": "Contract Renewal" },{ "image_url": "https://s3-us-west-2.amazonaws.com/o2bot/image/carousel_pay_bills.jpg", "button": [ { "type":"postback", "title":"Ask Now", "payload":"bill too high" } ], "title": "Bill Related Issues" }]}]}]

else:
    output = [{'text': ['Something went wrong.']}]
