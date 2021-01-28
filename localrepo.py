import os
import sys
from github import Github
from environs import Env

env = Env()
env.read_env()  # read the .env file
commitMess = sys.argv[1]  # get the commit message in CamelCase
token = env("gt")  # get the token from the .env file
os.environ["ap"] = sys.argv[2]  # set the project path to the .env file
path = env("ap")  # get the project path from the .env file

g = Github(token)
user = g.get_user()
login = user.login

commands = [
            'git add *',
            'git status',
            'git branch -M main',
            f'git commit -m "{commitMess}"',
            'git push origin main',
        ]

if sys.argv[2] is not None:
    os.chdir(path)
    for c in commands:
        os.system(c)
