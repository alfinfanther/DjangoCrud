# DjangoCrud

1. install > pip install -r requirements.txt
2. python manage.py makemigrations
3. python manage.py migrate


Note : change connection db in file (djangocrud/settings.py)


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'djangocrud',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}



url
1. /
2. /book/add/
3. /book/edit/<fid>/
4. /book/delete/<fid>/
