#! /usr/bin/env python3
import requests, json, todoist
from todoist.api import TodoistAPI
from configs import todoist_token, gsheets_ID, gsheets_GID

res=requests.get(url='https://docs.google.com/spreadsheets/d/' + gsheets_ID + '/export?format=csv&id=' + gsheets_ID + '&gid=' + gsheets_GID)
open('checklist.csv', 'wb').write(res.content)

api = TodoistAPI(todoist_token)
api.sync()
#try:
#       projectid = open("projectid", "r")
#       requests.delete("https://api.todoist.com/rest/v1/projects/" + str(projectid.read()), headers={"Authorization": "Bearer " + todoist_token})
#except:
#       pass
projectid = open("projectid", "r")
projectid = str(projectid.read())
print(projectid)

project = api.projects.get_by_id(projectid)
dir(project)
project = api.projects.add('Checklists')
project.update(color='31')
api.commit()
api.templates.import_into_project(project["id"], 'checklist.csv')
with open('projectid', 'w') as f:
       f.write(str(project["id"]))
