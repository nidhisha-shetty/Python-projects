# Get the total confirmed cases in a particular state in India
import requests
import json
data=requests.get('https://api.rootnet.in/covid19-in/stats/latest')
result=json.loads(data.text)
print(result['data']['regional'][19]['loc'])    #get the state name; Maharashtra
print(result['data']['regional'][19]['totalConfirmed']) #get the total number of cases in that(line 6) state



# Get the total confirmed cases of a particular country in the world
import requests
import json
data=requests.get('https://api.covid19api.com/summary')
result=json.loads(data.text)
a=result
b=a['Countries']
c=b[76]
print(c['TotalConfirmed']) #get the total confirmed cases in India

 
