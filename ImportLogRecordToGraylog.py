import requests
from datetime import datetime

# this code will write a single record to graylog using the http gelf input
# note this is going over http - do not use this in production


headers = {'Content-Type':'application/json'}


now = datetime.now()
yrint = now.year #2020
mint = 3
dint = 15
hrint = 13
minint = 37
secint = 51
#print(yrint)
a = "dominos"
b = "want pizza?"

dt = datetime(yrint,mint,dint, hrint, minint, secint)

timestamp = (dt - datetime(1970, 1, 1)).total_seconds()
#print(timestamp)
strtimestamp = str(timestamp)

data = '{"version":"1.1","host":"' + a + '","short_message": "' + b +'", "level":5, "_some_info":"foo", "timestamp":"' + strtimestamp + '"}'
#print(data)
response = requests.post("http://10.0.0.253:12201/gelf",headers=headers,data=data)
print(response)




