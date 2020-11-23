
import urllib.parse
import requests

main_api = 'https://www.mapquestapi.com/directions/v2/route?'

key = '8zd1yc'

while True:
    orig = input('Start location: ')
    if orig == 'q':
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
       print("Direction from " + orig + " to " + dest)
       print("Duration: " + json_data['route']['formattedTime'])
       print("Kilometers: " + str("{:.1f}".format(json_data['route']['distance']*1.61)))
       print("Fuel used (Ltr): " + str("{:.1f}".format(json_data['route']['fuelUsed']*3.78)))
       print("=====================================================")
       for each in json_data['route']['legs'][0]['maneuvers']:
           print((each['narrative']) + " (" + str("{:.2f}".format((each['distance'])*1.61) + " km)"))
       print("=====================================================") 
    elif json_status == 402:
       print("=====================================================") 
       print('API status: ' + str(json_status)+ ", invalid user inputs.")
       print("=====================================================")
    else:
       print("=====================================================")
       print('API status: ' + str(json_status)+ ", please refer to:")	   
       print('https://https://github.com/nyukers/APIC-EM')
       print("=====================================================")