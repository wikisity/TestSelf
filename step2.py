#-----------> STEP2 CODE2040 CHALLENGE

# Description: This python code requests a string from an API endpoint
#              then reverses that string and POST it back to a different API endpoint


import requests


# This function POSTS my API_TOKEN to the ENDPOINT_URL
# Obtain a response from the endpoint via a request line and return that response
def post_token():
    endpoint_url = "http://challenge.code2040.org/api/reverse"
    body = {"token": "770b31d581955134adc9c583414686f6"}

    # Request line to obtain the data from the server
    response = requests.post(endpoint_url, data = body)
    return response.text



def main():

    this_string = post_token() # Saving my string for usage
    print(this_string) # Display the obtained string
    reverse_string = this_string[::-1] # Reversing the string
    print(reverse_string) # Display the reverse string
   
    # I am posting some JSON to the target endpoint for validation
    # The JSON contains the reversed string that needs to be validated
    endpoint_url = "http://challenge.code2040.org/api/reverse/validate"
    this_body = {"token": "770b31d581955134adc9c583414686f6", "string": reverse_string.strip()}
   
    response = requests.post(endpoint_url, data = this_body)
    print(response.text)
       
   


main()