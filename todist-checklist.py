#! /usr/bin/env python3
import requests, json
import todoist
import gspread
from todoist.api import TodoistAPI
from configs import api_token

#f = requests.get("https://docs.google.com/spreadsheets/d/1xzHvUuTLteQDt0mgByuj7Zypnv-7LUQmPP2Ij-mq5IY/gviz/tq?tqx=out:csv")
#print(str(f.content))

csv_url='https://docs.google.com/spreadsheets/d/169AMdEzYzH7NDY20RCcyf-JpxPSUaO0nC5JRUb8wwvc/export?format=csv&id=169AMdEzYzH7NDY20RCcyf-JpxPSUaO0nC5JRUb8wwvc&gid=0'
res=requests.get(url=csv_url)
open('google.csv', 'wb').write(res.content)

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
api.templates.import_into_project(project["id"], '')
with open('projectid', 'w') as f:
       f.write(str(project["id"]))
