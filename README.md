**Python Project To automate creating repository process**
**This Script works only in Windows OS**
1:
    install python if you haven't.
    git clone 
2:
    Open the project folder in cmd or cmder and type:
        pip install -r requirements.txt
3:
    open the .env file and enter the information but do not enter any information in 'ap' field
4:
    to make the .bat file works good you need to open environment variables.
    click on new button.
    enter a variable name.
    then click browse file and choose the create.bat file.
5:
    there are two ways to use this script
        first one:
            if you want to make a new folder and make it the repository then in the command line type:
                create.bat <the name of the folder>
            but if you want to make a repository from a project folder in your pc or laptop then type:
                create.bat <the name of the repository> -l