#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import sched, time
import threading
import json
from flask import Flask

#app = Flask(__name__)

#headers = {'Content-Type': 'application/json'}

greece = {"country":"Greece","total_cases":"0","active_cases":"0","new_cases":"0","total_recovered":"0","serious_cases":"0","total_deaths":"0","new_deaths":"0","total_cases_per_mil":"0"}

# Send message with telegram bot
def bot_send_message(message):
    bot_link = "https://api.telegram.org/bot1141616070:AAHfA9xi3qe067xL4qBUUWfnn7x_ln6-rA8/sendMessage?chat_id=@coronavirusingreece&text="
    response = requests.get(bot_link + message).json()
    result = response["result"]
    message_id = result["message_id"]
    return message_id
 
def run_check():

    threading.Timer(60, run_check).start()
    response = requests.get("https://coron-api.azurewebsites.net/api/v1/stats?country=Greece")
    if response.status_code == 200:
        json_res = json.loads(response.content.decode('utf-8'))
        
        total_cases = json_res["total_cases"]
        active_cases = json_res["active_cases"]
        new_cases = json_res["new_cases"]
        total_recovered = json_res["total_recovered"]
        serious_cases = json_res["serious_cases"]
        total_deaths = json_res["total_deaths"]
        new_deaths = json_res["new_deaths"]
        total_cases_per_mil = json_res["total_cases_per_mil"]
        
        if(sorted(greece.items()) != sorted(json_res.items())):

            greece['total_cases'] = json_res['total_cases']
            greece['active_cases'] = json_res['active_cases']
            greece['new_cases'] = json_res['new_cases']
            greece['total_recovered'] = json_res['total_recovered']
            greece['serious_cases'] = json_res['serious_cases']
            greece['total_deaths'] = json_res['total_deaths']
            greece['new_deaths'] = json_res['new_deaths']
            greece['total_cases_per_mil'] = json_res['total_cases_per_mil']
            string = "Συνολικά κρούσματα: "
            string += greece['total_cases'].encode("utf-8")
            string += "%0AΕνεργά κρούσματα: "
            string += greece['active_cases'].encode("utf-8")
            string += "%0AΝέα κρούσματα: "
            string += greece['new_cases'].encode("utf-8")
            string += "%0AΈχουν αναρρώσει: "
            string += greece['total_recovered'].encode("utf-8")
            string += "%0AΣοβαρά περιστατικά: "
            string += greece['serious_cases'].encode("utf-8")
            string += "%0AΣυνολικοί θάνατοι: "
            string += greece['total_deaths'].encode("utf-8")
            string += "%0AΝέοι θάνατοι: "
            string += greece['new_deaths'].encode("utf-8")
            string += "%0AΚρούσματα ανά 1.000.000 πλυθησμού: "
            string += greece['total_cases_per_mil'].encode("utf-8")
            print(string)
            bot_send_message(string)
        
    else:
        return None
    
if __name__ == '__main__':
    run_check()
    #app.run()
