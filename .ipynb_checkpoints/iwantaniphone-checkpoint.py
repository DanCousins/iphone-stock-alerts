import requests
import time
import datetime

#Example
#15PM
#MU793ZD/A
#https://www.apple.com/uk/shop/fulfillment-messages?pl=true&mts.0=regular&parts.0=MU793ZD/A&location=W1B%202EL

def apple_scanner():
    #stick your url below
    response = requests.get("https://www.apple.com/uk/shop/fulfillment-messages?pl=true&mts.0=regular&parts.0=MU793ZD/A&location=W1B%202EL").json()
    #put your model in here
    availability = response['body']['content']['pickupMessage']['stores'][0]['partsAvailability']['MU793ZD/A']['pickupSearchQuote'] #replace "MU793ZD/A" here with your model
    post_code = response['body']['content']['pickupMessage']['stores'][0]['address']['postalCode']
    response_list = []

    if availability == "Currently unavailable":
        response_list.append(False)
        response_list.append(post_code)
        return response_list
    else:
        response_list.append(True)
        response_list.append(post_code)
        return response_list

iphone_question = False
#Create a Telegram bot and start a conversation with yourself, then grab the chat id and input that and your bot token below
BOT_TOKEN = "" #mine is of the format 10 numbers : 35 characters
chat_id = "" #10 numbers
message = "IPHONE TIME HOMIE LET'S GOOOOOOOOOO"
url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={message}"


while iphone_question == False:
    now = datetime.datetime.now()
    print(f"Scanning... - {now.time()}")
    try:    
        temp_list = apple_scanner()
        if temp_list[0] == True:
            print(f"*** IPHONE FOUND - POST CODE: {temp_list[1]} ***")
            url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={temp_list[1]}"
            requests.get(url)
            #iphone_question = True
    except Exception as e:
        print(f"Something went wrong - Exception: {e}")
    time.sleep(60)