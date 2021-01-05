import sys
import pandas as pd
from math import pi
from pprint import pprint
from github import Github
from bokeh.plotting import figure
from bokeh.io import output_file, show
from bokeh.palettes import Category20c
from bokeh.transform import cumsum
from bokeh.layouts import row
from array import *


def displayDetails():
	GIT_TOKEN = "REDACTED FOR GIT COMMIT"
	g = Github(GIT_TOKEN)
	#repo = g.get_repo("atelier-popstar/gitAPI")
	repo = g.get_repo("bendunnegyms/github-api")

	#repo = takeUserInput()
	commits = repo.get_commits()
	owner = repo.owner.login
	avatar_url = repo.owner.avatar_url
	commitID = []
	commitAuthor = []
	commitNumber = 0
	languageData = repo.get_languages()


	


	print(languageData)

	for commit in commits:
		commitID.append(commit.sha)
		commitAuthor.append(commit.author.login)
		commitNumber += 1

		#print(commit.sha)
		#print(commit.author.login)
		#print(commitNumber)
	
	authors = []
	trimmedAuthorNames = []
	for i in commitAuthor:
		if i not in trimmedAuthorNames:
			authors.append(RepoContributor(i, 0))
			trimmedAuthorNames.append(i)
	
	cnt = 0

	for commit in commits:
		for i in authors:
			if commit.author.login == authors[cnt].name:
				authors[cnt].commits += 1
			cnt += 1
		cnt = 0

	for i in authors:
		print(i.name)
		print(i.commits)

	plot(authors, languageData)



def plot(authors, languageData):
	output_file("simple-bar-chart.html")

	x_axis_author_name = []
	y_axis_author_commits = []

	for author in authors:
		x_axis_author_name.append(author.name)
		y_axis_author_commits.append(author.commits)

	p1 = figure(x_range=x_axis_author_name, plot_height=250, title="Commits by Contributor", toolbar_location=None, tools="")

	p1.vbar(x=x_axis_author_name, top= y_axis_author_commits, width=0.2)

	p1.xgrid.grid_line_color = None
	p1.y_range.start = 0

	#show(p)

	data = pd.Series(languageData).reset_index(name='value').rename(columns={'index':'country'})
	data['angle'] = data['value']/data['value'].sum() * 2*pi
	data['color'] = Category20c[len(languageData)]

	p2 = figure(plot_height=350, title="Pie Chart", toolbar_location=None,
           tools="hover", tooltips="@country: @value", x_range=(-0.5, 1.0))

	p2.wedge(x=0, y=1, radius=0.4,
        start_angle=cumsum('angle', include_zero=True), end_angle=cumsum('angle'),
        line_color="white", fill_color='color', legend_field='country', source=data)

	p2.axis.axis_label=None
	p2.axis.visible=False
	p2.grid.grid_line_color = None

	show(row(p1, p2))
		

	#print(x_axis_author_name)
	#print(y_axis_author_commits)

def takeUserInput():
	token = input('Please enter a GitHub accesss token: ')
	user = input('Please enter the username to display data on: ')
	repo_str = input('Please enter the repo you wish to view metrics on: ')
	g = Github(token)
	repo = g.get_repo(f"{user}/{repo_str}")

	return repo



class RepoContributor:
	def __init__(self, name, commits):
		self.name = name
		self.commits = commits

def main():
	displayDetails()
	
if __name__ == '__main__':
    main()

