api_token='5010e354fbb1e86dd6fff9f7ef9880324ce40989'

import requests, json
import todoist
from todoist.api import TodoistAPI

projectid = open("projectid", "r")
api = TodoistAPI(api_token)
api.sync()
requests.delete("https://api.todoist.com/rest/v1/projects/" + str(projectid.read()), headers={"Authorization": "Bearer " + api_token})
project = api.projects.add('Checklist')
project.update(color='31')
print(project)
api.commit()
api.templates.import_into_project(project["id"], '/share/Checklist.csv')
with open('projectid', 'w') as f:
       f.write(str(project["id"]))
