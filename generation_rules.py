templateKey = ""
messageStore = {}

output_db = variables['databases']['nva_o2']

if(variables['newdfState']['local_city']):
    templateKey = "A2"
    messageStore = {
    "endflow":True,
    "sendtoagent":False
    }


elif 'reset' in variables['nlp']['custom_ners'] and variables['nlp']['custom_ners']['reset']:
    templateKey = "what_can_you_do"
    messageStore = {
    "endflow":False,
    "sendtoagent":False
    }

elif 'about_us' in variables['nlp']['custom_ners'] and variables['nlp']['custom_ners']['about_us']:
    templateKey = "A0"
    messageStore = {
    "endflow":False,
    "sendtoagent":False
    }


elif 'reset' in variables['nlp']['custom_ners'] and variables['nlp']['custom_ners']['reset']:
    templateKey = "what_can_you_do"
    messageStore = {
    "endflow":False,
    "sendtoagent":False
    }


#common sense generation templates
elif "commonsense_tag" in variables["nlp"].keys() and variables["nlp"]["commonsense_tag"] is not None:
    templateKey = str(variables["nlp"]["commonsense_tag"])
    messageStore = {
    "endflow":False,
    "sendtoagent":False
    }

#when the user doesnt enter a valid phone number in the first attempt
elif variables['dataStore']['last_requested_df'] == "mobile" and variables['dataStore']['counter']==1:
    templateKey = "A4"
    messageStore = {
    "endflow":False,
    "sendtoagent":False
    }

#when the user doesnt enter a valid phone number in the second attempt
elif variables['dataStore']['last_requested_df'] == "mobile" and variables['dataStore']['counter']==2:
    templateKey = "A5"
    messageStore = {
    "endflow":False,
    "sendtoagent":False
    }


#when the user doesnt enter a valid datetime in the second attempt
elif variables['dataStore']['last_requested_df'] == "datetime" and variables['dataStore']['counter']>=1 and variables['dataStore']['counter']<=2:
    templateKey = "A15"
    messageStore = {
    "endflow":False,
    "sendtoagent":False
    }

#when the user doesnt enter a valid OTP in the first attempt
elif variables['dataStore']['last_requested_df'] == "otp" and variables['dataStore']['counter']==1:
    templateKey = "A7_2"
    messageStore = {
    "endflow":False,
    "sendtoagent":False
    }

#when the user doesnt enter a valid OTP in the second attempt
elif variables['dataStore']['last_requested_df'] == "otp" and variables['dataStore']['counter']==2:
    templateKey = "A7_3"
    messageStore = {
    "endflow":False,
    "sendtoagent":False
    }


elif variables['dataStore']['counter']>2:
    templateKey = "A5_1"
    messageStore = {
    "endflow":True,
    "sendtoagent":False
    }

elif("mobile" in variables["newdfState"] and variables['newdfState']['mobile']!=None and 'verb' in variables['newdfState'] and variables['newdfState']['verb'] == "renew" and 'call_now' in variables['newdfState']  and variables['newdfState']['call_now']==1):
    templateKey = "A14"
    messageStore = {
    "endflow":True,
    "sendtoagent":False
    }


elif("mobile" in variables["newdfState"] and variables['newdfState']['mobile']!=None and 'verb' in variables['newdfState'] and variables['newdfState']['verb'] == "renew" and "date" in variables['newdfState'] and variables['newdfState']['date']!= None and "time" in variables['newdfState'] and variables['newdfState']['time']!= None ):
    templateKey = "A13"
    messageStore = {
    "endflow":True,
    "sendtoagent":False
    }

elif("mobile" in variables["newdfState"] and variables['newdfState']['mobile']!=None and 'verb' in variables['newdfState'] and variables['newdfState']['verb'] == "renew" and "date" in variables['newdfState'] and variables['newdfState']['date']!= None and "time" in variables['newdfState'] and variables['newdfState']['time']== None ):
    templateKey = "A12"
    messageStore = {
    "endflow":True,
    "sendtoagent":False
    }



elif("mobile" in variables["newdfState"] and variables['newdfState']['mobile']!=None and 'verb' in variables['newdfState'] and variables['newdfState']['verb'] == "renew"):
    templateKey = "A11"
    messageStore = {
    "endflow":True,
    "sendtoagent":False
    }

elif("travel_yes" in variables["newdfState"] and variables['newdfState']['travel_yes'] == "yes" and variables['dataStore']['isAuthenticated'] == 1):
    templateKey = "A8"
    messageStore = {
    "endflow":True,
    "sendtoagent":False
    }

elif("travel_yes" in variables["newdfState"] and variables['newdfState']['travel_yes'] == "no"):
    templateKey = "A9"
    messageStore = {
    "endflow":True,
    "sendtoagent":False
    }

elif("travel_yes" in variables["newdfState"] and variables['newdfState']['travel_yes'] == "yes"):
    templateKey = "A7"
    messageStore = {
    "endflow":True,
    "sendtoagent":False
    }

elif("noun" in variables["newdfState"] and variables['newdfState']['noun'] == "roaming" and "mobile" in variables['newdfState'] and variables['newdfState']['mobile'] != None):
    templateKey = "A6"
    messageStore = {
    "endflow":True,
    "sendtoagent":False
    }

elif(variables['newdfState']['noun'] or variables['newdfState']['verb'] or variables['newdfState']['adj']):
    for item in output_db:
        if item["noun"] == variables['newdfState']['noun'] and item["verb"] == variables['newdfState']['verb'] and item["adj"] == variables['newdfState']['adj']:
            templateKey = item["output"]
    if templateKey == "":
        templateKey = "default"

    messageStore = {
    "endflow":True,
    "sendtoagent":False
    }


else:
    templateKey = "default"
    messageStore = {
    "endflow": True,
    "sendtoagent": False
    }

if templateKey in ["A2", "A8" , "A9" , "A13" , "A17" , "A18" , "A19" , "A20", "default", "", "A5_1"]:
    variables['dataStore']['resetFlag'] = 1

if templateKey in ["", "A20"]:
    variables['dataStore']['sendtoagent'] = 1

output = {
"templateKey": templateKey,
"messageStore": messageStore
}
