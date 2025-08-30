# Tools

1. Install python3
2. Install pip3 (it was not working out of the box on ubuntu)
3. Install django globally with python3 -m pip install
```bash
django-admin startproject my_app
```

### Run project locally

```bash
python3 manage.py runserver
```


### Projects && Apps
We create one project at start.

django project is divided into "apps". First app is created at beggining.
We want to create our apps alongside it. (It can be also thought about as modules)


Apps are usually related to features of the app. I.E purchesing of something (domains?)

### venv
helps us maintain specific versions for python app

creating venv
```bash
 python3 -m venv venv
```

running one of the venvs
```bash
source tutorial-env/bin/activate
```

exiting venv
```bash
deactivate
```