import sys
from pprint import pprint
from github import Github
from bokeh.plotting import figure
from bokeh.io import output_file, show
from array import *


def displayDetails():
	GIT_TOKEN = "REDACTED FOR GIT COMMIT"
	g = Github(GIT_TOKEN)

	user = input('Please enter the username to display data on: ')
	repo_str = input('Please enter the repo you wish to view metrics on: ')


	repo = g.get_repo(f"{user}/{repo_str}")

	#repo = g.get_repo("atelier-popstar/gitAPI")
	#repo = g.get_repo("bendunnegyms/github-api")
	commits = repo.get_commits()
	owner = repo.owner.login
	avatar_url = repo.owner.avatar_url
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
	
	cnt = 0

	for commit in commits:
		for i in Authors:
			if commit.author.login == Authors[cnt].name:
				Authors[cnt].commits += 1
			cnt += 1
		cnt = 0

	for i in Authors:
		print(i.name)
		print(i.commits)

	plot(Authors)



def plot(Authors):
	output_file("simple-bar-chart.html")

	x_axis_author_name = []
	y_axis_author_commits = []

	for Author in Authors:
		x_axis_author_name.append(Author.name)
		y_axis_author_commits.append(Author.commits)

	p = figure(x_range=x_axis_author_name, plot_height=250, title="Commits by Contributor", toolbar_location=None, tools="")

	p.vbar(x=x_axis_author_name, top= y_axis_author_commits, width=0.2)

	p.xgrid.grid_line_color = None
	p.y_range.start = 0

	show(p)
		

	#print(x_axis_author_name)
	#print(y_axis_author_commits)





class RepoContributor:
	def __init__(self, name, commits):
		self.name = name
		self.commits = commits

def main():
	displayDetails()
	
if __name__ == '__main__':
    main()

