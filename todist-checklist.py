import todoist
from todoist.api import TodoistAPI
api = TodoistAPI('5010e354fbb1e86dd6fff9f7ef9880324ce40989')
api.sync()
print(api.state['projects'])
project = api.projects.get_by_id('checklist')
project.delete()
api.commit()
project = api.projects.add('checklist')
print(project)
api.commit()
api.templates.import_into_project(128501470, '/share/Checklist.csv')

