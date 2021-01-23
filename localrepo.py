import os
import sys
from github import Github
from environs import Env

env = Env()
env.read_env()  # read the .env file
repoName = sys.argv[1]  # get the repo name
token = env("gt")  # get the token from the .env file
rp = os.environ["ap"] = sys.argv[2]  # set the project path to the .env file
path = env("ap")  # get the project path from the .env file

g = Github(token)
user = g.get_user()
login = user.login
repo = user.create_repo(repoName)

commands = [
            f'echo"# {repo.name}" >> README.md',
            'git init',
            'git add *',
            'git commit -m "Initial Commit"',
            'git branch -M main',
            f'git remote add origin https://github.com/{login}/{repoName}.git',
            'git push -u origin main',
        ]

if sys.argv[2] is not None:
    os.chdir(path)
    for c in commands:
        os.system(c)
