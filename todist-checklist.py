#! /usr/bin/env python3
import requests, json
import todoist
import gspread
from todoist.api import TodoistAPI
from configs import api_token
from configs import gsheets_ID

res=requests.get(url='https://docs.google.com/spreadsheets/d/' + gsheets_ID + '/export?format=csv&id=' + gsheets_ID + '&gid=0'
open('checklist.csv', 'wb').write(res.content)

api = TodoistAPI(api_token)
api.sync()
try:
       projectid = open("projectid", "r")
       requests.delete("https://api.todoist.com/rest/v1/projects/" + str(projectid.read()), headers={"Authorization": "Bearer " + api_token})
except:
       pass
project = api.projects.add('Checklists')
project.update(color='31')
api.commit()
api.templates.import_into_project(project["id"], 'checklist.csv')
with open('projectid', 'w') as f:
       f.write(str(project["id"]))
