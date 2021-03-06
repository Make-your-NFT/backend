# Make Your NFT Django

## π οΈ Language & Tools  π οΈ
![Python: Version](https://img.shields.io/badge/Python-3.10.4-3776AB.svg?logo=Python&logoColor=white)
![Django: Version](https://img.shields.io/badge/Django-4.0.5-092E20.svg?logo=Django&logoColor=white)
![MariaDB](https://img.shields.io/badge/MariaDB-003545.svg?logo=MariaDB&logoColor=white)
![Heroku](https://img.shields.io/badge/Heroku-430098.svg?logo=Heroku&logoColor=white)
<!--![Travis CI](https://img.shields.io/badge/TravisCI-3EAAAF.svg?logo=travis-ci&logoColor=white)-->

## π§ Setup π§

- κ°μ νκ²½μ μμ±ν ν κ°μ νκ²½μ μ§μν©λλ€.
  ```sh
  mkdir venvs
  cd venvs
  python -m venv myn
  cd myn/Scripts
  activate
  ```
<br>

- μνλ μμΉλ‘ μ΄λνμ¬ νλ‘μ νΈλ₯Ό cloneν©λλ€.
  ```sh
  $ git clone https://github.com/yeseong31/Django_MYN.git
  $ cd Django_MYN
  ```

<br>

- νλ‘μ νΈμ νμν ν¨ν€μ§λ₯Ό μ€μΉν©λλ€.
  ```sh
  (myn)$ pip install -r requirements.txt
  ```

  - μ΄λ νλ‘¬ννΈ μ°½μ `(myn)` νμλ `python -m venv` λͺλ Ήμ΄λ₯Ό ν΅ν΄ μμ±λ mynμ΄λΌλ μ΄λ¦μ κ°μ νκ²½μ μ§μν μνλ₯Ό μλ―Έν©λλ€. 
  
<br>

- ν¨ν€μ§ μ€μΉ μ΄ν νλ‘μ νΈ λ΄ `config/settings` μμΉλ‘ μ΄λνμ¬ `my_settings.py` νμΌμ μμ±ν©λλ€.
  ```python
  """my_settings.py"""
  
  # ----- Django settings -----
  DJANGO_SECRET_KEY =         # Django νλ‘μ νΈμ SECRET_KEY
  # ----- MariaDB(MySQL) settings -----
  DB_NAME =  		    # λ°μ΄ν°λ² μ΄μ€ μ΄λ¦
  DB_USER =   		    # λ°μ΄ν°λ² μ΄μ€ User μ΄λ¦
  DB_PASSWORD = 		    # λ°μ΄ν°λ² μ΄μ€ λΉλ°λ²νΈ
  # ----- Email settings -----
  EMAIL_HOST_USER =  	    # μ΄λ©μΌ μ£Όμ(μΈμ¦ λ§ν¬ λ°μ‘)
  EMAIL_HOST_PASSWORD = 	    # μ΄λ©μΌ λΉλ°λ²νΈ(μΈμ¦ λ§ν¬ λ°μ‘) - λ³λ μ€μ  νμ
  # ----- end of settings -----
  
  # SECURITY WARNING: keep the secret key used in production secret!
  SECRET_KEY = {
      'secret': DJANGO_SECRET_KEY,
      'algorithm': 'HS256',
  }

  DATABASES = {
      'default': {
          'ENGINE': 'django.db.backends.mysql',
          'NAME': DB_NAME,
          'USER': DB_USER,
          'PASSWORD': DB_PASSWORD,
          'HOST': '127.0.0.1',
          'PORT': '3306',
      }
  }

  # Email Authentication
  EMAIL = {
      'EMAIL_BACKEND': 'django.core.mail.backends.smtp.EmailBackend',
      'EMAIL_USE_TLS': True,
      'EMAIL_PORT': '587',
      'EMAIL_HOST': 'smtp.gmail.com',
      'EMAIL_HOST_USER': EMAIL_HOST_USER,
      'EMAIL_HOST_PASSWORD': EMAIL_HOST_PASSWORD,
      'SERVER_EMAIL': 'MYN',
      'REDIRECT_PAGE': 'http://127.0.0.1:8000/'
  }
  ```

<br>

- λͺ¨λ  μ€μ  μλ£ μ λ€μμ λͺλ Ήμ΄λ‘ λ‘μ»¬ μλ²λ₯Ό μ€νν  μ μμ΅λλ€.
  ```sh
  (myn)$ set DJANGO_SETTINGS_MODULE=config.settings.local
  (myn)$ python manage.py runserver
  Watching for file changes with StatReloader
  Performing system checks...

  System check identified no issues (0 silenced).
  June 30, 2022 - 14:00:15
  Django version 4.0.5, using settings 'config.settings.local'
  Starting development server at http://127.0.0.1:8000/
  Quit the server with CTRL-BREAK.
  ```
