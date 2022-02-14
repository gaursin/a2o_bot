import time
import schedule
import json
import os
import csv
import datetime
import cards
from webexteamssdk import WebexTeamsAPI

access_token = os.environ.get('WEBEX_TEAMS_ACCESS_TOKEN')
# MDJhMDgxZjctNzdmNy00NDIyLWEyZDQtMmQzYmI4NzM2MzI5NzYxNzY5MDctYWFm_PF84_1eb65fdf-9643-417f-9974-ad72cae0e10f
roomID = os.environ.get('ROOM_ID')
#
api = WebexTeamsAPI(access_token= access_token)


month_dict = dict({ 1 : "Jan", 2 : "Feb", 3 : "Mar", 4 : "Apr", 5 : "May", 6 : "Jun", 7 : "Jul", 8 : "Aug", 9 : "Sep", 10 : "Oct", 11 : "Nov", 12 : "Dec" })


bday_list = []
farewell_list = []



#Function to check Birthday's by reading the csv
def checkTodaysBirthdays():
    print("Checking Bdays...")
    isbday = False
    today = datetime.datetime.now()
    month = today.month

    month_name = month_dict[month]
    date = str(today.day)
    bday = date + "-" + month_name
    stri = "hi"
    flag = 0
    with open('bdaysfile.json') as bdays_file_json:
        bday_file= json.load(bdays_file_json)
    for row in bday_file:

        #if current rows 2nd value is equal to input, print that row
        if bday == row["Birthday"]:
            isbday = True
            bday_list.append({
            'Name' : row["Employee Name"],
            'email' : row["email"],

            })
            reminder_to_space(row)

    if(isbday):
        time.sleep(30)
        bday_wish(bday_list,isbday)

    else :
            time.sleep(60)
            print("No Bdays")
            checkTodaysBirthdays()

def reminder_to_space(bday):
     #Reminder to space
        print("Sending Reminder...")
        REMINDER_CARD = cards.REMINDER_CARD
        reminder_text = "It's " +bday['Employee Name']+"'s Birthday today. I will wish them at 10:00 am."
        REMINDER_CARD["body"][2]["text"]=reminder_text
        api.messages.create(roomId= roomID,text=reminder_text,
        attachments=[{
                        "contentType": "application/vnd.microsoft.card.adaptive",
                        "content": REMINDER_CARD
                        }],
                    )
def bday_wish(bday_list,isbday) :
    f = open("Logs.txt", "a")
    if(isbday):

        for i in range(0,len(bday_list)):

            CARD_CONTENT_TO_BDAY_PERSON = cards.CARD_CONTENT_TO_BDAY_PERSON
            CARD_CONTENT_TO_EVERYONE = cards.CARD_CONTENT_TO_EVERYONE

            SUCCESS_CARD = cards.SUCCESS_CARD

            #print(bday_list[i]['Name'])




            # To find a bday person's room id
            x = bday_list[i]['email']
            bday_person_cec= x.split("@")
            #print(bday_person_cec)
            personId = bday_person_cec[i]
            #print(personId)
            person_url = "https://webexapis.com/v1/people?email="+x
            #print(person_url)


            name=bday_list[i]['Name']
            email=bday_list[i]['email']
            bday_text_to_everyone = "It's " + name +"'s Birthday."
            bday_text_to_person= "Hey "+name+","
            CARD_CONTENT_TO_BDAY_PERSON["body"][1]["text"]=bday_text_to_person

            #sending message to bday person
            f.write("\nCard sent to "+ bday_list[i]['email'])
            print("Its "+bday_list[i]['email']+"'s Birthday")
            api.messages.create(toPersonEmail=bday_list[i]['email'],
            text="Happy Birthday",
            attachments=[{
                    "contentType": "application/vnd.microsoft.card.adaptive",
                    "content": CARD_CONTENT_TO_BDAY_PERSON
                    }],)


            #Bday notification to everyone
            with open('bdaysfile.json') as bdays_file_json:
                bday_file= json.load(bdays_file_json)

            count_checker = 0
            f.write("Logs for "+ bday_list[i]['Name']+"'s Birthday")
            for row in bday_file:


                #print(row[3])
                if row["Employee Name"]!=bday_list[i]['Name'] and row["email"]!="email":
                    count_checker+=1
                    print(count_checker)
                    print(row["email"])

                    recipient_name = row["Employee Name"]
                    recipient_name_text = "Hey " + recipient_name + ","
                    CARD_CONTENT_TO_EVERYONE["body"][1]["text"]= recipient_name_text
                    CARD_CONTENT_TO_EVERYONE["body"][2]["text"]=bday_text_to_everyone
                    #print(CARD_CONTENT_TO_EVERYONE["body"][1]["text"])
                    api.messages.create(toPersonEmail=row["email"],
                                        text=bday_text_to_everyone,
                                        attachments=[{
                                                        "contentType": "application/vnd.microsoft.card.adaptive",
                                                        "content": CARD_CONTENT_TO_EVERYONE
                            }],
                                        )

                    f.write("\nCard sent to "+ row["email"])
            #Successful card
            print(count_checker)
            if count_checker == len(bday_file) - len(bday_list):
                completed_text =  name=bday_list[i]['Name']+"'s Birthday reminders successfully sent to "+ str(count_checker) + " people."
                SUCCESS_CARD["body"][1]["text"]=completed_text
                api.messages.create(roomId= roomID,text=completed_text,
                attachments=[{
                                                        "contentType": "application/vnd.microsoft.card.adaptive",
                                                        "content": SUCCESS_CARD
                            }],
                                        )

    f.close()

#Function to schedule
if __name__ == "__main__":
    checkTodaysBirthdays()
    print("Starting Exection ....")
