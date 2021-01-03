import sys
import requests
import json

def displayDetails():
	api = 'https://api.github.com/users/'
	user = input('Please enter the username to display data on: ')
	fullUrl = api+user
	response = (requests.get(fullUrl)).json()

	parsedResponse = json.loads(response)

	




	#print(response)
	#print(response['followers'])
	#769b9b7b98a1aacd52d7908d1d489614dc7d74dd
	#^access token

def main():
	displayDetails()
	
if __name__ == '__main__':
    main()

