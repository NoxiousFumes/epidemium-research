from joglwrapper import Reader
from joglwrapper import Project
from joglwrapper import Output
from pathlib import Path

# reader = Reader()
# reader.save_all()

output = Output()

output.generate_project(1, 'test')

output.generate_all_users(1)

output.generate_user(671, 'test')

project = Project(1)

