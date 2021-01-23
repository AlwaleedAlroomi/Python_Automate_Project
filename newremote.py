import os
import sys
from github import Github
from environs import Env

env = Env()
env.read_env()  # read the .env file
folderName = str(sys.argv[1])  # to get the folder name
path = env("pp")  # to get the path from .env file
token = env('gt')  # to get the github token form .env file
_dir = path + '\\' + folderName  # the path into the folder that the command made and will be the repo

g = Github(token)  # the main class to access github API
user = g.get_user()  # methods for login and get your account
login = user.login
repo = user.create_repo(folderName)  # to make a new repo in your github account

# the commands that will print inside the folder
commands = [
            f'echo"# {repo.name}" >> README.md',
            'git init',
            'git add README.md',
            'git commit -m "Initial Commit"',
            'git branch -M main',
            f'git remote add origin https://github.com/{login}/{folderName}.git',
            'git push -u origin main',
            'code .',
        ]


if sys.argv[1] is not None:
    os.chdir(path)  # change the directory into the path you have entered
    os.mkdir(folderName)  # make a new folder in it
    os.chdir(_dir)  # to enter the folder

    # a For loop to print the commands
    for c in commands:
        os.system(c)
else:
    print("error")
