import todoist
from todoist.api import TodoistAPI
projectid = open("projectid", "r")
api = TodoistAPI('5010e354fbb1e86dd6fff9f7ef9880324ce40989')
api.sync()
project = api.projects.get_by_id(str(projectid.read))
try:       
       project.delete()
api.commit()
project = api.projects.add('checklist')
api.commit()
print(project["id"])
api.templates.import_into_project(project["id"], '/share/Checklist.csv')
with open(projectid, 'w') as f:
       f.write(project["id"])
