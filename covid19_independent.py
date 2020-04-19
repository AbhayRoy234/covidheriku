from plyer import notification
import requests
from bs4 import BeautifulSoup
import time
import csv
from flask import Flask, request, send_file
from twilio.twiml.messaging_response import MessagingResponse
import io
from datetime import datetime

main_list=list()
states=[]
count=1
state=[  str(x) for x in range(0,34)]
def getsite(url):
    r = requests.get(url)
    return r.text
appbot = Flask(__name__)


@appbot.route("/demo-reply", methods=["get", "post"])
def reply():

    ur_message = request.form.get("Body")
    un = request.form.get("From")
    sitehtml = getsite('https://www.mohfw.gov.in/')
        # print(sitehtml)
    soup = BeautifulSoup(sitehtml, 'html.parser')
    sitehtml = ""
    for tr in soup.find_all('table')[0].find_all('tr'):
        sitehtml += tr.get_text()
    sitehtml = sitehtml
    reqdata = sitehtml.split("\n\n")
    print(sitehtml)
    for item in reqdata[1:]:
        datalist = item.split("\n")
        main_list.append(datalist)
        # states.append(datalist[1])

    if ur_message=="States":
        msg = MessagingResponse()
        # for i in main_list:
            # states.append(count,i[1])
        states=["1.Andaman and Nicobar Islands ","2.Andhra Pradesh","3.Arunachal Pradesh","4.Assam","5.Bihar","6.Chandigarh","7.Chhattisgarh","8.Delhi","9.Goa","10.Gujarat","11.Haryana","12.Himachal Pradesh","13.Jammu and Kashmir","14.Jharkhand","15.Karnataka","16.Kerala","17.Ladakh","18.Madhya Pradesh","19.Maharashtra","20.Manipur","21.Meghalaya","22.Mizoram","23.Nagaland","24.Odisha","25.Puducherry","26.Punjab","27.Rajasthan","28.Tamil Nadu","29.Telengana","30.Tripura","31.Uttarakhand","32.Uttar Pradesh","33.West Bengal"]
        # states1=str(states).split("\n\n")
        states1='\n'.join(states)
        response = msg.message(str(states1))
        return (str(msg))

    if ur_message=="India":
        msg = MessagingResponse()
        # state=["Andaman and Nicobar Islands","Andhra Pradesh","Arunachal Pradesh"]
        response = msg.message("Total Confirm Cases in INDIA :"+str(main_list[len(main_list)-5][1])+"\nTotal Recovered till Now :"+str(main_list[len(main_list)-4][0])+"\nToatl Deaths till Now :"+str(main_list[len(main_list)-3][1]))
        return (str(msg))
    if ur_message in state:

        msg = MessagingResponse()
        response = msg.message("State: "+str(main_list[int(ur_message)-1][1]) +"\nTotal Confoirm Cases: "+str(main_list[int(ur_message)-1][2])+"\nTotal Death :"+str(main_list[int(ur_message)-1][3])+"\nTotal Recoverred Caess:"+str(main_list[int(ur_message)-1][4]))
        return (str(msg))
    else:
        msg=MessagingResponse()
        response=msg.message("please enter the valid Keyword\n1.'India'\n2.'States'(To See States Lists)\n3.To get States wise Upadtes")
        return str(msg)







if __name__ == '__main__':
    appbot.run()
    # appbot.run(reply1)