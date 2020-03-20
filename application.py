import requests
import sched, time
import threading

headers = {'Content-Type': 'application/json'}

# Send message with telegram bot
def bot_send_message(message):
    bot_link = "https://api.telegram.org/bot1141616070:AAHfA9xi3qe067xL4qBUUWfnn7x_ln6-rA8/sendMessage?chat_id=@coronavirusingreece&text="
    response = requests.get(bot_link + message).json()
    result = response["result"]
    message_id = result["message_id"]
    return message_id
 
def run_check():
    threading.Timer(60, run_check).start()
    response = reqiests.get("https://coron-api.azurewebsites.net/api/v1/stats?country=Greece")
    if response.status_code == 200:
        test = json.loads(response.content.decode('utf-8'))
      
        result = response["result"]
        total_cases = result["total_cases"]
        active_cases = result["active_cases"]
        new_cases = result["new_cases"]
        total_recovered = result["total_recovered"]
        serious_cases = result["serious_cases"]
        total_deaths = result["total_deaths"]
        new_deaths = result["new_deaths"]
        total_cases_per_mil = result["total_cases_per_mil"]
        
        bot_send_message("total cases: " + total_cases);
        bot_send_message("test: " + test);
        
    else:
        return None
    
 
run_check()
