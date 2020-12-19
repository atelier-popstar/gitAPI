import sys
import requests

def displayDetails():
	api = 'https://api.github.com/users/'
	user = input('Please enter the username to display data on: ')
	fullUrl = api+user
	response = (requests.get(fullUrl)).json()
	print(response)
	#print(response['followers'])

def main():
	displayDetails()
	
if __name__ == '__main__':
    main()