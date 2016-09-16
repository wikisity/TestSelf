#---------> STEP4 CODE2040 CHALLENGE

# Description: THis python program requests a JSON object with two keys and values. 
#              the first value, of key, 'prefix', is a string. The second, of key,
#              'array', is an array of strings. The program POSTS a JSON to an
#              Endpoint API with one key of the JSON object paired to an array of
#              strings that do not start with that prefix.


import requests, json

# This method POSTS my token to an Endpoint API and returns a
# dictionary object
def get_dictionary():
    endpoint_url = "http://challenge.code2040.org/api/prefix"
    body = {"token": "770b31d581955134adc9c583414686f6"}
    response = requests.post(endpoint_url, data = body)
    result = json.loads(response.text)
    return (result)


def main():

    this_dict = get_dictionary() # Save my dictionary for usage
    print(type(this_dict)) # Making sure I received a dictionary object

    this_list = this_dict["array"]
    this_string = this_dict["prefix"]

    new_list = []
    print()  # To have a better display in the terminal

    # Building a new list with its elements ordered and similar to the old list
    # except that each string of the new list is different from prefix
    for strings in this_list:
        index = 0
        while index < len(this_string):
            if this_string[index] == strings[index]:
                found_prefix = True
                index += 1

            else:
                found_prefix = False
                index = len(this_string)
       
        if not(found_prefix):
            new_list.append(strings) # array of strings to be built


    print()
    print(new_list)
       

    # Post result to an Endpoint API for validation
    endpoint_url = "http://challenge.code2040.org/api/prefix/validate"
    response = requests.post(endpoint_url, json = {"token": "770b31d581955134adc9c583414686f6", "array": new_list})
       
    print()
    print(response.text) # Obtain response from the requests
       
       

main()