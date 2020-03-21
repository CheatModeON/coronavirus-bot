#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import sched, time
import threading
import json

#headers = {'Content-Type': 'application/json'}

greece = {
    "active_cases": "498", 
  "country": "Greece", 
  "new_cases": "+35", 
  "new_deaths": "+3", 
  "serious_cases": "15", 
  "total_cases": "530", 
  "total_cases_per_mil": "51", 
  "total_deaths": "13", 
  "total_recovered": "19"
}

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
            
            total_cases_string = "%0AΣυνολικά κρούσματα: "
            total_cases_string += json_res['total_cases'].encode("utf-8")
            if(greece['total_cases'] != json_res['total_cases'] and json_res['total_cases'] != "No Data"):
                total_cases_string += " [NEO]"
                
            active_cases_string = "%0AΕνεργά κρούσματα: "
            active_cases_string += json_res['active_cases'].encode("utf-8")
            if(greece['active_cases'] != json_res['active_cases'] and json_res['active_cases'] != "No Data"):
                active_cases_string += " [NEO]"
                
            new_cases_string = "%0AΝέα κρούσματα: "
            new_cases_string += json_res['new_cases'].encode("utf-8")
            if(greece['new_cases'] != json_res['new_cases'] and json_res['new_cases'] != "No Data"):
                new_cases_string += " [NEO]"
                
            total_recovered_string = "%0AΈχουν αναρρώσει: "
            total_recovered_string += json_res['total_recovered'].encode("utf-8")
            if(greece['total_recovered'] != json_res['total_recovered'] and json_res['total_recovered'] != "No Data"):
                total_recovered_string += " [NEO]"
                
            serious_cases_string = "%0AΣοβαρά περιστατικά: "
            serious_cases_string += json_res['serious_cases'].encode("utf-8")
            if(greece['serious_cases'] != json_res['serious_cases'] and json_res['serious_cases'] != "No Data"):
                serious_cases_string += " [NEO]"
                
            total_deaths_string = "%0AΣυνολικοί θάνατοι: "
            total_deaths_string += json_res['total_deaths'].encode("utf-8")
            if(greece['total_deaths'] != json_res['total_deaths'] and json_res['total_deaths'] != "No Data"):
                total_deaths_string += " [NEO]"
                
            new_deaths_string = "%0AΝέοι θάνατοι: "
            new_deaths_string += json_res['new_deaths'].encode("utf-8")
            if(greece['new_deaths'] != json_res['new_deaths'] and json_res['new_deaths'] != "No Data"):
                new_deaths_string += " [NEO]"
                
            total_cases_per_mil_string = "%0AΚρούσματα ανά 1.000.000 πλυθησμού: "
            total_cases_per_mil_string += json_res['total_cases_per_mil'].encode("utf-8")
            if(greece['total_cases_per_mil'] != json_res['total_cases_per_mil'] and json_res['total_cases_per_mil'] != "No Data"):
                total_cases_per_mil_string += " [NEO]"
                
            string = "Έκτακτη Ενημέρωση"
            string += total_cases_string
            string += active_cases_string
            string += new_cases_string
            string += total_recovered_string
            string += serious_cases_string
            string += total_deaths_string
            string += new_deaths_string
            string += total_cases_per_mil_string
            print(string)
            bot_send_message(string)
            
            greece['total_cases'] = json_res['total_cases']
            greece['active_cases'] = json_res['active_cases']
            greece['new_cases'] = json_res['new_cases']
            greece['total_recovered'] = json_res['total_recovered']
            greece['serious_cases'] = json_res['serious_cases']
            greece['total_deaths'] = json_res['total_deaths']
            greece['new_deaths'] = json_res['new_deaths']
            greece['total_cases_per_mil'] = json_res['total_cases_per_mil']
        
    else:
        return None
    
    
if __name__ == '__main__':
    run_check()

