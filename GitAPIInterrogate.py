import sys
import requests
import json
import os
from pprint import pprint
from github import Github


def displayDetails():
	GIT_TOKEN = "REDACTED FOR COMMIT"
	g = Github(GIT_TOKEN)

	#user = input('Please enter the username to display data on: ')
	#repo_str = input('Please enter the repo you wish to view metrics on: ')


	#repo = g.get_repo(f"{user}/{repo_str}")

	repo = g.get_repo("torvalds/linux")
	commits = repo.get_commits()
	commitID = []
	commitAuthor = []
	commitNumber = 0

	for commit in commits:
		
		commitID.append(commit.sha)
		commitAuthor.append(commit.author)
		commitNumber += 1

		print(commit.sha)
		print(commit.author)
		print(commitNumber)

	
	







	# api = 'https://api.github.com/users/'
	# repos = '/repos'
	# 
	# fullUrl = api+user+repos
	# response = (requests.get(fullUrl)).json()

	
	# try:

	# 	parsedResponse = json.load(response)[0]
	# except json.decoder.JSONDecodeError:
	# 	print("Data could not be converted to JSON.")
	
	
	

	




	#print(response)
	#print(response['followers'])
	#^access token



def main():
	displayDetails()
	
if __name__ == '__main__':
    main()

