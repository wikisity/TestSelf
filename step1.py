#---------> STEP1 CODE2040 CHALLENGE

# Description: This python code POSTS  new information to an Enpoint API
#              as a step of registration to the Endpoint  


import requests


def main():

	endpoint_url = "http://challenge.code2040.org/api/register"
	body = {"token": "770b31d581955134adc9c583414686f6", "github": "https://github.com/wikisity/TestSelf"}

	# Request line to POST my info to the EnDpoint API.
	response = requests.post(endpoint_url, data = body) 
	print(response.text)  # Check response form the request
	

main()