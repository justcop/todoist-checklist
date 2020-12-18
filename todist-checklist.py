import requests, json
import todoist
from todoist.api import TodoistAPI

projectid = open("projectid", "r")
api = TodoistAPI('5010e354fbb1e86dd6fff9f7ef9880324ce40989')
api.sync()
#project = api.projects.get_by_id(str(projectid.read()))
requests.delete("https://api.todoist.com/rest/v1/projects/" + str(projectid.read()), headers={"Authorization": "Bearer 5010e354fbb1e86dd6fff9f7ef9880324ce40989"})
#try:       
#       project.delete()
#       api.commit()
#except:
#       pass
#project.delete()
#api.commit()
project = api.projects.add('checklist')
api.commit()
api.templates.import_into_project(project["id"], '/share/Checklist.csv')
with open('projectid', 'w') as f:
       f.write(str(project["id"]))
