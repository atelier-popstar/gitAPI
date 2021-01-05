import sys
import requests
import json
import os
from pprint import pprint
from github import Github
from array import *


def displayDetails():
	GIT_TOKEN = "REDACTED FOR GIT COMMIT"
	g = Github(GIT_TOKEN)

	#user = input('Please enter the username to display data on: ')
	#repo_str = input('Please enter the repo you wish to view metrics on: ')


	#repo = g.get_repo(f"{user}/{repo_str}")

	repo = g.get_repo("atelier-popstar/gitAPI")
	commits = repo.get_commits()
	commitID = []
	commitAuthor = []
	commitNumber = 0

	for commit in commits:
		
		commitID.append(commit.sha)
		commitAuthor.append(commit.author.login)
		commitNumber += 1

		#print(commit.sha)
		#print(commit.author.login)
		#print(commitNumber)
	
	Authors = []
	trimmedAuthorNames = []
	for i in commitAuthor:
		if i not in trimmedAuthorNames:
			Authors.append(RepoContributor(i, 0))
			trimmedAuthorNames.append(i)
	
	for commit in commits:


	#for i in trimmedAuthors:
	#	print(i.name)
	#	print(i.commits)


	

	


	

	
	







class RepoContributor:
	def __init__(self, name, commits):
		self.name = name
		self.commits = commits

def main():
	displayDetails()
	
if __name__ == '__main__':
    main()

