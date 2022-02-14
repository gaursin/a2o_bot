import time
import schedule

import json
import os
import csv
import datetime
import cards



from webexteamssdk import WebexTeamsAPI

access_token = os.environ.get('WEBEX_TEAMS_ACCESS_TOKEN')
roomID = os.environ.get('ROOM_ID')

api = WebexTeamsAPI(access_token= access_token)


month_dict = dict({ 1 : "Jan", 2 : "Feb", 3 : "Mar", 4 : "Apr", 5 : "May", 6 : "Jun", 7 : "Jul", 8 : "Aug", 9 : "Sep", 10 : "Oct", 11 : "Nov", 12 : "Dec" })


bday_list = []
farewell_list = []



#Function to check Birthday's by reading the csv
def checkTodaysBirthdays():
    print("Checking Bdays...")
    #fileName = open(birthdayFile, 'r')
    isbday = False
    today = datetime.datetime.now()
    month = today.month

    month_name = month_dict[month]
    date = str(today.day)
    bday = date + "-" + month_name
    stri = "hi"
    flag = 0

    #csv_file = csv.reader(open(test_file, "r"), delimiter=",")



    with open('bdaysfile.json') as bdays_file_json:
        bday_file= json.load(bdays_file_json)


#loop through the csv list
    for row in bday_file:

        #if current rows 2nd value is equal to input, print that row
        if bday == row["Birthday"]:
            isbday = True
            bday_list.append({
            'Name' : row["Employee Name"],
            'email' : row["email"],

            })
            reminder_to_space(row)

        #else :
            #time.sleep(60)
            #checkTodaysBirthdays()


    if(isbday):
        time.sleep(30)
        bday_wish(bday_list,isbday)

    else :
            time.sleep(60)
            print("No Bdays")
            checkTodaysBirthdays()


# def checkTodaysFarwells():
#     print("Checking Farewells...")
#     #fileName = open(birthdayFile, 'r')
#     isfarewell = False
#     today = datetime.datetime.now()
#     month = today.month

#     month_name = month_dict[month]
#     date = str(today.day)
#     bday = date + "-" + month_name




#     with open('bdaysfile.json') as bdays_file_json:
#         bday_file= json.load(bdays_file_json)


# #loop through the csv list
#     for row in bday_file:

#         #if current rows 2nd value is equal to input, print that row
#         if bday == row["Birthday"]:
#             isfarewell = True
#             farewell_list.append({
#             'Name' : row["Employee Name"],
#             'email' : row["email"],

#             })
#             reminder_to_space(row)

#         #else :
#             #time.sleep(60)
#             #checkTodaysBirthdays()


#     if(isfarewell):
#         time.sleep(30)
#         farewell_wish(farewell_list,isfarewell)

#     else :
#             time.sleep(60)
#             print("No Farewells today")
#             checkTodaysFarwells()




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

# def farewell_wish(farewell_list,isfarewell):
#     f = open("Logs.txt", "a")
#     if(isfarewell):

#         for i in range(0,len(farewell_list)):

#             CARD_CONTENT_TO_FAREWELL_PERSON = cards.CARD_CONTENT_TO_FAREWELL_PERSON
#             CARD_CONTENT_TO_EVERYONE_FAREWELL = cards.CARD_CONTENT_TO_EVERYONE_FAREWELL

#             SUCCESS_CARD = cards.SUCCESS_CARD

#             #print(bday_list[i]['Name'])

#             name=farewell_list[i]['Name']
#             email=farewell_list[i]['email']
#             farewell_text_to_everyone = "It's " + name +"'s last day in our team."
#             farewell_text_to_person= "Hey "+name+","
#             CARD_CONTENT_TO_FAREWELL_PERSON["body"][1]["text"]=farewell_text_to_person

#             #sending message to bday person
#             f.write("\nCard sent to "+ farewell_list[i]['email'])
#             print("Its "+farewell_list[i]['email']+"'s last day in our team")
#             api.messages.create(toPersonEmail=farewell_list[i]['email'],
#             text="Farewell",
#             attachments=[{
#                     "contentType": "application/vnd.microsoft.card.adaptive",
#                     "content": CARD_CONTENT_TO_FAREWELL_PERSON
#                     }],)


#             #Bday notification to everyone
#             with open('bdaysfile.json') as bdays_file_json:
#                 bday_file= json.load(bdays_file_json)

#             count_checker = 0
#             f.write("Logs for "+ farewell_list[i]['Name']+"'s Farewell")
#             for row in bday_file:


#                 #print(row[3])
#                 if row["Employee Name"]!=farewell_list[i]['Name'] and row["email"]!="email":
#                     count_checker+=1
#                     print(count_checker)
#                     print(row["email"])

#                     recipient_name = row["Employee Name"]
#                     recipient_name_text = "Hey " + recipient_name + ","
#                     CARD_CONTENT_TO_EVERYONE_FAREWELL["body"][1]["text"]= recipient_name_text
#                     CARD_CONTENT_TO_EVERYONE_FAREWELL["body"][2]["text"]=farewell_text_to_everyone
#                     #print(CARD_CONTENT_TO_EVERYONE["body"][1]["text"])
#                     api.messages.create(toPersonEmail=row["email"],
#                                         text=farewell_text_to_everyone,
#                                         attachments=[{
#                                                         "contentType": "application/vnd.microsoft.card.adaptive",
#                                                         "content": CARD_CONTENT_TO_EVERYONE_FAREWELL
#                             }],
#                                         )

#                     f.write("\nCard sent to "+ row["email"])
#             #Successful card
#             print(count_checker)
#             if count_checker == len(bday_file) - len(bday_list):
#                 completed_text =  name=bday_list[i]['Name']+"'s Farewell reminders successfully sent to "+ str(count_checker) + " people."
#                 SUCCESS_CARD["body"][1]["text"]=completed_text
#                 api.messages.create(roomId= roomID,text=completed_text,
#                 attachments=[{
#                                                         "contentType": "application/vnd.microsoft.card.adaptive",
#                                                         "content": SUCCESS_CARD
#                             }],
#                                         )

#     f.close()






#Function to schedule
if __name__ == "__main__":
    # comment this when you scheduler is running else bday person will
    #receive 2 messages
    checkTodaysBirthdays()
    #checkTodaysFarwells()

    print("Starting Exection ....")
    #schedule.every().day.at("09:27").do(checkTodaysBirthdays)
    #schedule.every().day.at("23:44").do(bday_wish)

    #while True:
       #schedule.run_pending()
       #time.sleep(60) # wait one minute
