<h2 align="center">Fortunei</h2>

## Requisitos
```
# Python 3 (Probado en 3.10.1)
# Django 4 (Probado en 4.0.1)
# MySQL
# pip (Probado en 21.3.1)
# Numpy (Puedes instalarlo con pip install numpy)
# mysqlclient (Puedes instalarlo con pip install mysqlclient)
```

## Clonar el proyecto
Primero se debe clonar el proyecto a tu dispositivo desde la terminal o en archivo zip. Posteriormente, abres una terminal y te ubicas dentro de la carpeta del proyecto. 

## Configurar la base de datos

Una vez descargado el proyecto, se configura la conexión a MySQL, mediante el user y password, puedes cambiar el nombre que va a llevar la base de datos, por defecto se llama "fortunei"

```
# Variables de la base de datos
'default': {
      'ENGINE': 'django.db.backends.mysql',
      'NAME': 'fortunei',
      'USER': 'root',
      'PASSWORD': '',
      'HOST': '127.0.0.1',
      'OPTIONS': {
          'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
      },
  }
```

## Database configuration

Una vez que configuraste la conexión, se crea la base de datos y se corren las migraciones.

```
python manage.py migrate
```

## Inicia el servidor

Una vez configurado el proyecto y la base de datos, se inicia el servidor local. Por defecto se accede mediante 127.0.0.1:8000, pero puedes cambiar el puerto del servidor.

```
python manage.py runserver
```

<h2>Disfruta</h2>
