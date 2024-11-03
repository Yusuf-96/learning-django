Steps:
=> Create the main folder-> carry the project
   => create virtual env for the python project like node_module in Js
      -command run >> python3 -m venv <name_env>. Example python3 -m venv venv.
      -For every project requires it own env and packages
      - Activate the virtual env, command >> source venv/bin/activate
    
   => Install Django and other supporting packages, example Django, django-restframework, decouple, database engines like postgres. You can find them on official documents. Using pip command example pip install <package_name>

   => Initialize the django project: command >> django-admin startproject <project_name> (optional (.)-> to initialize on the existing or current dir).

   => Create an app or module; command >>> python3 manage.py startapp <app_name>. example python3 manage.py startapp firts

