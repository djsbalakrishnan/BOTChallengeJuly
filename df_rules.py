import requests
from random import randint
import requests
import json


localcity = None
noun_val = None
verb_val = None
adj_val = None
validate_result = 0
date_val = None
time_val = None

mobile_num=None
one_time_pin = None
travel_yes_val = None
call_now_val = None
last_requested_df_val = None
counter_val = 0

syn_db = variables['databases']['synonyms']


#To reset
if ('dataStore' in variables and variables['dataStore'] != None and len(variables['dataStore'])>=1 and 'resetFlag' in variables['dataStore'] and variables['dataStore']['resetFlag']!= None and variables['dataStore']['resetFlag']==1) or  ('dataStore' in variables and variables['dataStore'] != None and len(variables['dataStore'])>=1 and 'sendtoagent' in variables['dataStore'] and variables['dataStore']['sendtoagent']!= None and variables['dataStore']['sendtoagent']==1) or ('reset' in variables['nlp']['custom_ners']):
    localcity = None
    noun_val = None
    verb_val = None
    adj_val = None
    validate_result = 0
    date_val = None
    time_val = None

    mobile_num=None
    one_time_pin = None
    travel_yes_val = None
    call_now_val = None
    last_requested_df_val = None
    counter_val = 0

#to handle the travel bolt on use case when the user is travelling within the country and no travel bolt on will be needed
if('local_city' in variables['nlp']['custom_ners']):
    localcity = variables['nlp']['custom_ners']['local_city_value'][0]


#Fill call_now
if('call_now' in variables['nlp']['custom_ners'] and variables['nlp']['custom_ners']['call_now']):
    call_now_val = 1

elif ('dataStore' in variables and variables['dataStore']!=None and len(variables['dataStore']) >= 1 and 'resetFlag' in variables['dataStore'] and variables['dataStore']['resetFlag']!= None and variables['dataStore']['resetFlag']==1) or ('dataStore' in variables and variables['dataStore']!=None and len(variables['dataStore']) >= 1 and 'sendtoagent' in variables['dataStore'] and variables['dataStore']['sendtoagent']!= None and variables['dataStore']['sendtoagent']==1):
    call_now_val = None

elif('call_now' in variables['lastdfState'] and variables['lastdfState']['call_now']):
    call_now_val = 1


#get date value from NER
if('datetime' in variables['nlp'] and len(variables['nlp']['datetime'])==1 and variables['nlp']['datetime'][0]!= None and 'result' in variables['nlp']['datetime'][0] and 'date' in variables['nlp']['datetime'][0]['result'] and variables['nlp']['datetime'][0]['result']['date']!= None):
    date_val = variables['nlp']['datetime'][0]['result']['date']

elif ('dataStore' in variables and variables['dataStore']!=None and len(variables['dataStore']) >= 1 and 'resetFlag' in variables['dataStore'] and variables['dataStore']['resetFlag']!= None and variables['dataStore']['resetFlag']==1) or ('dataStore' in variables and variables['dataStore']!=None and len(variables['dataStore']) >= 1 and 'sendtoagent' in variables['dataStore'] and variables['dataStore']['sendtoagent']!= None and variables['dataStore']['sendtoagent']==1):
    date_val = None

elif('date' in variables['lastdfState'] and variables['lastdfState']['date']!= None):
    date_val = variables['lastdfState']['date']


#get time value from NER
if('datetime' in variables['nlp'] and len(variables['nlp']['datetime'])==1 and variables['nlp']['datetime'][0]!= None and 'result' in variables['nlp']['datetime'][0] and 'time' in variables['nlp']['datetime'][0]['result'] and variables['nlp']['datetime'][0]['result']['time']!= None):
    time_val = variables['nlp']['datetime'][0]['result']['time']

elif ('dataStore' in variables and variables['dataStore']!=None and len(variables['dataStore']) >= 1 and 'resetFlag' in variables['dataStore'] and variables['dataStore']['resetFlag']!= None and variables['dataStore']['resetFlag']==1) or ('dataStore' in variables and variables['dataStore']!=None and len(variables['dataStore']) >= 1 and 'sendtoagent' in variables['dataStore'] and variables['dataStore']['sendtoagent']!= None and variables['dataStore']['sendtoagent']==1):
    time_val = None

elif('date' in variables['lastdfState'] and variables['lastdfState']['date']!= None):
    time_val = variables['lastdfState']['time']



#NOUN
if('noun' in variables['nlp']['custom_ners']):
    noun_val = variables['nlp']['custom_ners']['noun_value'][0]

    for item in syn_db:
        if noun_val == item["synonym"]:
            noun_syn_val = item["actual_value"]
    noun_val = noun_syn_val

    #set last_req_df to mobile if NER noun is roaming
    if(noun_val=="roaming" and 'mobile' not in variables['nlp']['custom_ners']):
        last_requested_df_val = "mobile"


elif ('dataStore' in variables and variables['dataStore']!=None and len(variables['dataStore']) >= 1 and 'resetFlag' in variables['dataStore'] and variables['dataStore']['resetFlag']!= None and variables['dataStore']['resetFlag']==1) or ('dataStore' in variables and variables['dataStore']!=None and len(variables['dataStore']) >= 1 and 'sendtoagent' in variables['dataStore'] and variables['dataStore']['sendtoagent']!= None and variables['dataStore']['sendtoagent']==1):
    noun_val = None

elif('noun' in variables['lastdfState'] and variables['lastdfState']['noun'] != None):
    noun_val = variables['lastdfState']['noun']


# Last requested DF
# if ('dataStore' in variables and variables['dataStore']!=None and len(variables['dataStore']) >= 1 and 'resetFlag' in variables['dataStore'] and variables['dataStore']['resetFlag']!= None and variables['dataStore']['resetFlag']==1) or ('dataStore' in variables and variables['dataStore']!=None and len(variables['dataStore']) >= 1 and 'sendtoagent' in variables['dataStore'] and variables['dataStore']['sendtoagent']!= None and variables['dataStore']['sendtoagent']==1):
#     last_requested_df_val = None
# elif()


#VERB
if('verb' in variables['nlp']['custom_ners']):
    verb_val = variables['nlp']['custom_ners']['verb_value'][0]
    verb_syn_val = verb_val
    for item in syn_db:
        if verb_val == item["synonym"]:
            verb_syn_val = item["actual_value"]
    verb_val = verb_syn_val

    #set last_req_df to mobile if NER vern is renew
    if(verb_val=="renew" and 'mobile' not in variables['nlp']['custom_ners']):
        last_requested_df_val = "mobile"


elif ('dataStore' in variables and variables['dataStore']!=None and len(variables['dataStore']) >= 1 and 'resetFlag' in variables['dataStore'] and variables['dataStore']['resetFlag']!= None and variables['dataStore']['resetFlag']==1) or ('dataStore' in variables and variables['dataStore']!=None and len(variables['dataStore']) >= 1 and 'sendtoagent' in variables['dataStore'] and variables['dataStore']['sendtoagent']!= None and variables['dataStore']['sendtoagent']==1):
    verb_val = None

elif('verb' in variables['lastdfState'] and variables['lastdfState']['verb'] != None):
    verb_val = variables['lastdfState']['verb']



#ADJECTIVE
if('adj' in variables['nlp']['custom_ners']):
    adj_val = variables['nlp']['custom_ners']['adj_value'][0]
    adj_syn_val = adj_val
    for item in syn_db:
        if adj_val == item["synonym"]:
            adj_syn_val = item["actual_value"]
    adj_val = adj_syn_val

elif ('dataStore' in variables and variables['dataStore']!=None and len(variables['dataStore']) >= 1 and 'resetFlag' in variables['dataStore'] and variables['dataStore']['resetFlag']!= None and variables['dataStore']['resetFlag']==1) or ('dataStore' in variables and variables['dataStore']!=None and len(variables['dataStore']) >= 1 and 'sendtoagent' in variables['dataStore'] and variables['dataStore']['sendtoagent']!= None and variables['dataStore']['sendtoagent']==1):
    adj_val = None

elif('adj' in variables['lastdfState'] and variables['lastdfState']['adj'] != None):
    adj_val = variables['lastdfState']['adj']


#mobile
if('mobile' in variables['nlp']['custom_ners']):
    mobile_num = variables['nlp']['custom_ners']['mobile_value'][0]

    if ('verb' in variables['nlp']['custom_ners'] and verb_val == "renew") or (variables['lastdfState']['verb'] == "renew" and 'dataStore' in variables and variables['dataStore']!= None and len(variables['dataStore']) >= 1 and 'resetFlag' in variables['dataStore'] and variables['dataStore']['resetFlag']== None):
        last_requested_df_val = "datetime"

elif ('dataStore' in variables and variables['dataStore']!=None and len(variables['dataStore']) >= 1 and 'resetFlag' in variables['dataStore'] and variables['dataStore']['resetFlag']!= None and variables['dataStore']['resetFlag']==1) or ('dataStore' in variables and variables['dataStore']!=None and len(variables['dataStore']) >= 1 and 'sendtoagent' in variables['dataStore'] and variables['dataStore']['sendtoagent']!= None and variables['dataStore']['sendtoagent']==1):
    mobile_num = None

elif('mobile' in variables['lastdfState']):
    mobile_num = variables['lastdfState']['mobile']



#Fill OTP
if('otp' in variables['nlp']['custom_ners']):
    one_time_pin = variables['nlp']['custom_ners']['otp_value'][0]

elif ('dataStore' in variables and variables['dataStore']!=None and len(variables['dataStore']) >= 1 and 'resetFlag' in variables['dataStore'] and variables['dataStore']['resetFlag']!= None and variables['dataStore']['resetFlag']==1) or ('dataStore' in variables and variables['dataStore']!=None and len(variables['dataStore']) >= 1 and 'sendtoagent' in variables['dataStore'] and variables['dataStore']['sendtoagent']!= None and variables['dataStore']['sendtoagent']==1):
    one_time_pin = None

elif('otp' in variables['lastdfState']):
    one_time_pin = variables['lastdfState']['otp']



#isYes
if('isYes' in variables['nlp']['custom_ners'] and variables['lastdfState']['noun'] == "roaming" and variables['lastdfState']['mobile'] != None):
    travel_yes_val = "yes"
    last_requested_df_val = "otp"

elif ('dataStore' in variables and variables['dataStore']!=None and len(variables['dataStore']) >= 1 and 'resetFlag' in variables['dataStore'] and variables['dataStore']['resetFlag']!= None and variables['dataStore']['resetFlag']==1) or ('dataStore' in variables and variables['dataStore']!=None and len(variables['dataStore']) >= 1 and 'sendtoagent' in variables['dataStore'] and variables['dataStore']['sendtoagent']!= None and variables['dataStore']['sendtoagent']==1):
    travel_yes_val = None

elif('travel_yes' in variables['lastdfState'] and variables['lastdfState']['travel_yes'] == "yes"):
    travel_yes_val = "yes"


#isNo
if('isNo' in variables['nlp']['custom_ners'] and variables['lastdfState']['noun'] == "roaming" and variables['lastdfState']['mobile'] != None):
    travel_yes_val = "no"

# Function to sendOTP to a mobile number
def sendOTP(mob):
    import requests
    import json
    url = 'https://api.imiconnect.io/resources/v1/events/externalevent'
    data = {
    	"key":"8f973731-f511-11e6-bfef-0213261164bb",
    	"events":[
    		{
    			"evtid":"1789",
    			"correlationid":"2394",
    			"parameters":
    			{ "mobile": mob }
    		}
    	]
    }
    headers = {'content-type': 'application/json'}
    response = requests.post(url, data=json.dumps(data) , headers=headers)
    print("OTP has been sent")

# Function to validate OTP sent to a mobile number
def validateOTP(mob,otp):
    import requests
    import json
    url = "https://api.imiconnect.io/resources/v1/OTP/verify"
    data = {"identifier": mob ,"pin": otp }
    headers = {'content-type': 'application/json', 'key' : '8f973731-f511-11e6-bfef-0213261164bb'}
    response = requests.post(url, data=json.dumps(data) , headers=headers)
    response_json = json.loads(response.text)

    if response_json["description"] == "invalid OTP":
        return 0
        print("Invalid OTP!!")
    elif response_json["description"] == "SUCCESS":
        return 1
        print("otp validation successful")
    elif otp=="":
        return 0
        print("blank OTP")
    # print(type(response_json))
    print("called imiconnect URL to validate OTP")



# Send and validate OTP --- for Travel Use Case
if('noun' in variables['lastdfState'] and variables['lastdfState']['noun'] == "roaming" and variables['lastdfState']['mobile'] != None and 'isYes' in variables['nlp']['custom_ners'] and variables['nlp']['custom_ners']['isYes']):
    sendOTP(variables['lastdfState']['mobile'])

if('noun' in variables['lastdfState'] and variables['lastdfState']['noun'] == "roaming" and variables['lastdfState']['mobile'] != None and 'otp' in variables['nlp']['custom_ners'] and variables['nlp']['custom_ners']['otp'] and variables['lastdfState']['travel_yes'] == "yes"):
    print "CALL OTP VALIDATION FUNCTION"
    validate_result = validateOTP(variables['lastdfState']['mobile'], variables['nlp']['custom_ners']['otp_value'][0])


'''
LAST REQUESTED DF and COUNTER FOR TRAVEL AND CONTRACT RENEWAL USE CASE
'''

#For Mobile in travel use case
if(noun_val == "roaming" and 'mobile' not in variables['nlp']['custom_ners'] and 'dataStore' in variables and variables['dataStore']!=None and len(variables['dataStore']) >= 1 and 'last_requested_df' in variables['dataStore'] and variables['dataStore']['last_requested_df']!= None and variables['dataStore']['last_requested_df']=="mobile"):
    counter_val = variables['dataStore']['counter']+1
    last_requested_df_val = "mobile"

#For OTP in travel use case
if(noun_val == "roaming" and 'otp' not in variables['nlp']['custom_ners'] and 'dataStore' in variables and variables['dataStore']!=None and len(variables['dataStore']) >= 1 and 'last_requested_df' in variables['dataStore'] and variables['dataStore']['last_requested_df']!= None and variables['dataStore']['last_requested_df']=="otp" and variables['lastdfState']['travel_yes']=="yes"):
    counter_val = variables['dataStore']['counter']+1
    last_requested_df_val = "otp"

#For Mobile in contract renewal use case
if(verb_val == "renew" and 'mobile' not in variables['nlp']['custom_ners'] and 'dataStore' in variables and variables['dataStore']!=None and len(variables['dataStore']) >= 1 and 'last_requested_df' in variables['dataStore'] and variables['dataStore']['last_requested_df']!= None and variables['dataStore']['last_requested_df']=="mobile"):
    counter_val = variables['dataStore']['counter']+1
    last_requested_df_val = "mobile"


#For datetime in contract renewal use case
if(verb_val == "renew" and mobile_num != None and len(variables['nlp']['datetime']) == 0 and 'dataStore' in variables and variables['dataStore']!=None and len(variables['dataStore']) >= 1 and 'last_requested_df' in variables['dataStore'] and variables['dataStore']['last_requested_df']!= None and variables['dataStore']['last_requested_df']=="datetime"):
    counter_val = variables['dataStore']['counter']+1
    last_requested_df_val = "datetime"


if 'reset' in variables['nlp']['custom_ners'] and variables['nlp']['custom_ners']['reset']:
    localcity = None
    noun_val = None
    verb_val = None
    adj_val = None
    validate_result = 0
    date_val = None
    time_val = None

    mobile_num=None
    one_time_pin = None
    travel_yes_val = None
    call_now_val = None
    last_requested_df_val = None


data_store = {"counter" : 0 , "isAuthenticated" : validate_result, "resetFlag" : None , "sendtoagent" : None , "last_requested_df" : last_requested_df_val , "counter" : counter_val}

newdf = {
	"noun": noun_val,
	"verb": verb_val,
	"adj": adj_val,
	"mobile": mobile_num,
	"otp": one_time_pin,
	"local_city": localcity,
	"country": None,
	"travel_yes": travel_yes_val,
	"date": date_val,
	"time": time_val,
	"call_now": call_now_val,
	"bill_options": None,
	"backup_phone": None,
	"dob": None,
	"last_topup": None,
	"new_sim": None,
	# "last_requested_df": None,
	# "counter": 0,
	"logout": None
	# "sessionrequired": None
}

output = {
  "df": newdf,
  "dataStore" : data_store
}
