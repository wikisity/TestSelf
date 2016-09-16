#---------> STEP5 CODE2040 CHALLENGE

# Description: The goal of this python code is to work with dates and times.
#              one of the goals is to get a dictionary from an API. The value for the key, datestamp. is a string
#              formatted as an ISO 8601 datestamp. The value for interval, is a number of seconds.
#              I have to add the interval to the date, then return the resulting date to the API. 


import requests, json, datetime
from dateutil.parser import parse
from dateutil.relativedelta import relativedelta


# This method POSTS my token to an Endpoint API and returns a
# dictionary object
def get_dictionary():
    endpoint_url = "http://challenge.code2040.org/api/dating"
    body = {"token": "770b31d581955134adc9c583414686f6"}
    response = requests.post(endpoint_url, data = body)
    result = json.loads(response.text)
    return (result)



def main():

    this_dict = get_dictionary() # Save my dictionary for usage
    # To make sure I received a dictionary object
    print(this_dict) 
    print(type(this_dict)) 


    this_string = this_dict["datestamp"]
    this_seconds = this_dict["interval"]

    # Parsing the ISO 8601 date format I received from the server
    this_date = parse(this_string)
    print(this_date)

    this_date += relativedelta(seconds = this_seconds) # Adding seconds to the datestamp by using relativedelta library
    iso_format = this_date.isoformat() # Converting the result to an iso format date
    print(iso_format[:-6] + "Z") # Slicing my iso format, so it is formatted the same way as the one the API gave me.
   

    
    # Post result to an Endpoint API for validation
    endpoint_url = "http://challenge.code2040.org/api/dating/validate"
    response = requests.post(
        endpoint_url, 
        json = {
            "token": "770b31d581955134adc9c583414686f6",
            "datestamp": (iso_format[:-6] + "Z")}
        )
     
    print(response.text) # Obtain response from the requests
    


main()