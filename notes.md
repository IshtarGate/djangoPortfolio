# Notes For Myself

### List of Comands
- `python -m django --version`
- `python manage.py runserver`
- `django-admin startproject mysite`
- `python manage.py startapp polls`
- for migrations
    - Change your models (in models.py).
    - Run `python manage.py makemigrations` to create migrations for those changes
    - Run `python manage.py migrate` to apply those changes to the database.
- `python manage.py shell`
    - more db commands can be found here: [database api](https://docs.djangoproject.com/en/1.10/topics/db/queries/)

### What's Next
    - https://docs.djangoproject.com/en/1.10/intro/tutorial03/#raising-a-404-error

### Check These Out:
    - https://virtualenv.pypa.io/en/stable/userguide/
    - https://virtualenvwrapper.readthedocs.io/en/latest/install.html
    - learn regex
    
### Todo:
- setup virtualenv wrapper

### bullet train terminal launch
```

BULLETTRAIN_GIT_BG=none
BULLETTRAIN_GIT_FG='white'
BULLETTRAIN_DIR_BG=none
BULLETTRAIN_DIR_FG='white'
BULLETTRAIN_VIRTUALENV_BG=none
BULLETTRAIN_VIRTUALENV_FG='white'
BULLETTRAIN_CONTEXT_BG=none
BULLETTRAIN_CONTEXT_FG='white'
BULLETTRAIN_TIME_BG=none
BULLETTRAIN_TIME_FG='white'
BULLETTRAIN_STATUS_BG=none
BULLETTRAIN_STATUS_FG='white'
. ~/.virtualenvs/djangodev/bin/activate


```
