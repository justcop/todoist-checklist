import todoist
from todoist import TodoistAPI
api = todoist.TodoistAPI('5010e354fbb1e86dd6fff9f7ef9880324ce40989')
project = api.projects.get_by_id(checklist)
project.delete()
api.commit()
project = api.projects.add('checklist')
api.commit()
api.templates.import_into_project(128501470, '/share/Checklist.csv')
print(todoist.api.json_dumps(api))
