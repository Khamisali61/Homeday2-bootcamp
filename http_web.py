import requests
#setup parameters to pass to the API
#Which are the latitude and longitude of Nairobi
parameters= {"lat": -1.29 ,"lon":36.82}

#make a request with the parameters
response = requests.get("http://api.open-notify.org/iss-pass.json", params=parameters)

#print the content of the response (data returned by the server)
print(response.content)

