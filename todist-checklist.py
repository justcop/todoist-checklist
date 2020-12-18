import todoist
from todoist.api import TodoistAPI
api = TodoistAPI('5010e354fbb1e86dd6fff9f7ef9880324ce40989')
api.sync()
#project = api.projects.get_by_id('checklist')
#project.delete()
#api.commit()
project = api.projects.add('checklist')
api.commit()
print(project["id"])
api.templates.import_into_project(project[0]["id"](), '/share/Checklist.csv')

