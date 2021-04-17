DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'bratooldb',
        'USER': 'postgres',
        'PASSWORD': 'postgres_password',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

#################################################################
    ##  (CORS) Cross-Origin Resource Sharing Settings ##
#################################################################
CORS_ORIGIN_ALLOW_ALL = True