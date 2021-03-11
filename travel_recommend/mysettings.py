# for security 
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'test',
        'USER': 'root',
        'PASSWORD':'123',
        'HOST': 'localhost',
        'PORT': '3306',

    }
}
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '=vu8pbo=hu_*3)o7rimcc&d(q91q157w&2l#1++*m3^8owo_17'
