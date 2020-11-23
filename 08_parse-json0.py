
import urllib.parse
import requests

main_api = 'https://www.mapquestapi.com/directions/v2/route?'

key = 'api_key'

while True:
    orig = input('Start location: ')
	if orig == 'q'
        break
    dest = input('Destination location: ')
    if dest == 'q':
        break

    url = main_api + urllib.parse.urlencode({"key":key, "from":orig, "to":dest})
    print("URL: " + url)
                                         
    json_data = requests.get(url).json()	

    json_status = json_data['info']['statuscode']
    if json_status == 0:
       print('API status: ' + str(json_status)+ " = a successful route call has done.")


