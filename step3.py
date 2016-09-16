#-----------> STEP3 CODE2040 CHALLENGE

# Description: This python code is a solution to the problem of 'Needle in a haystack'
#              The code obtain a dictionary of two values and keys from an API. One 
#              value of key 'needle' is a string and the other value of key 'haystack'
#              is an array of strings. The program POSTS back to an API of validation,  
#              the position of the Needle in the array




import requests  # import library to post request to my API endpoint
import json      # import library to convert objects to a dictionary format

# This method requests an Object from an Endpoint API and returns
# a dictionary object
def get_dictionary():
    endpoint_url = "http://challenge.code2040.org/api/haystack"
    body = {"token": "770b31d581955134adc9c583414686f6"}
    response = requests.post(endpoint_url, data = body)
    result = json.loads(response.text)
    return (result)

def main():
   
    this_dict = get_dictionary() # Save my dictionary for usage
    print(this_dict) # Display my dictionary for verification purpose
   
    this_list = this_dict["haystack"]
    this_string = this_dict["needle"]
   
    # Looking for the position of my string in the array
    for index in range(len(this_list)):
        if (this_string == this_list[index]):
            position_of_needle = index  # Save this position

    # Post result to an Endpoint API for validation
    endpoint_url = "http://challenge.code2040.org/api/haystack/validate"
    body = {"token": "770b31d581955134adc9c583414686f6", "needle": position_of_needle}
    response = requests.post(endpoint_url, data = body)
   
    print(response.text) # Obtain response from the requests
   

   
main()