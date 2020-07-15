# Get the total confirmed cases in a particular state in India
import requests
import json
data=requests.get('https://api.rootnet.in/covid19-in/stats/latest')
result=json.loads(data.text)
print(result['data']['regional'][19]['loc'])
print(result['data']['regional'][19]['confirmedCasesIndian']) 



# Get the total confirmed cases in a particular country in the world
import requests
import json
data=requests.get('https://api.covid19api.com/summary')
result=json.loads(data.text)
a=result
b=a['Countries']
c=b[76]
print(c['TotalConfirmed']) #For total confirmed cases in India
# print(a) #For global results
# print(c) #For India results
 
