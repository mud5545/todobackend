INSTALLED_APPS = [
.
.

‘rest_framework’,
‘corsheaders’,
‘todo1’
]
.
.
MIDDLEWARE_CLASSES = [
‘django.middleware.security.SecurityMiddleware’,
‘corsheaders.middleware.CorsMiddleware’,
]

#Cors Settings do not do it in production
CORS_ORIGIN_ALLOW_ALL = True
