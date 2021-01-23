**Python Project To automate creating repository process**<br/>
**This Script works only in Windows OS**<br/>
**The name of the folder should be without spaces or any "_" write the name in CamelCase way**<br/>
1:<br/>
    install python if you haven't.<br/>
    git clone https://github.com/AlwaleedAlroomi/Python_Automate_Projetc-.git<br/>
2:<br/>
    Open the project folder in cmd or cmder and type:<br/>
        pip install -r requirements.txt<br/>
3:<br/>
    open the .env file and enter the information but do not enter any information in 'ap' field<br/>
4:<br/>
    to make the .bat file works good you need to open environment variables.<br/>
    click on new button.<br/>
    enter a variable name.<br/>
    then click browse file and choose the create.bat file.<br/>
5:<br/>
    there are two ways to use this script<br/>
        first one:<br/>
            if you want to make a new folder and make it the repository then in the command line type:<br/>
                create.bat <the name of the folder><br/>
            but if you want to make a repository from a project folder in your pc or laptop then type:<br/>
                create.bat <the name of the repository> -l<br/>