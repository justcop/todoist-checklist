#! /usr/bin/env python3


import requests, json
import todoist
from todoist.api import TodoistAPI
from configs import api_token

projectid = open("projectid", "r")
api = TodoistAPI(api_token)
api.sync()
requests.delete("https://api.todoist.com/rest/v1/projects/" + str(projectid.read()), headers={"Authorization": "Bearer " + api_token})
project = api.projects.add('Checklists')
project.update(color='31')
api.commit()
api.templates.import_into_project(project["id"], '/share/Checklist.csv')
with open('projectid', 'w') as f:
       f.write(str(project["id"]))
