import os
from pathlib import Path


BASE_DIR = BASE_DIR = Path(__file__).resolve().parent

def create_migrations_dirs():
    try:
        os.system(f"mkdir {os.path.join(BASE_DIR,'simpletodo','migrations')}")
        os.system(f"mkdir {os.path.join(BASE_DIR,'tasks','migrations')}")
        os.system(f"mkdir {os.path.join(BASE_DIR,'user_auth','migrations')}")
        f1 = open(os.path.join(BASE_DIR,'simpletodo','migrations','__init__.py'),'w')
        f1.write("")
        f1.close()
        print(f"Created {os.path.join(BASE_DIR,'simpletodo','migrations','__init__.py')}")
        f2 = open(os.path.join(BASE_DIR,'tasks','migrations','__init__.py'),'w')
        f2.write("")
        f2.close()
        print(f"Created {os.path.join(BASE_DIR,'tasks','migrations','__init__.py')}")
        f3 = open(os.path.join(BASE_DIR,'user_auth','migrations','__init__.py'),'w')
        f3.write("")
        f3.close()
        print(f"Created {os.path.join(BASE_DIR,'user_auth','migrations','__init__.py')}")
    except Exception as e:
        print(f'Encountered an error:\n{e}')

def unzip_static_files(path):
    from zipfile import ZipFile
    f = ZipFile(path)
    f.extractall()
    f.close()
    print('Extracted static files to /static folder')

def mysql_db_setup(creds):
    print("MySQL Database Setup:")
    MYSQL_DATABASE_NAME = creds['MYSQL_DATABASE_NAME']
    MYSQL_DATABASE_USER = creds['MYSQL_DATABASE_USER']
    MYSQL_DATABASE_PASSWORD = creds['MYSQL_DATABASE_PASSWORD']
    MYSQL_DATABASE_HOST = creds['MYSQL_DATABASE_HOST']
    MYSQL_DATABASE_PORT = creds['MYSQL_DATABASE_PORT']
    mysql_installed =  False
    try:
        try:
            import mysql.connector
            mysql_installed = True
        except:
            mysql_installed = False
            os.system('pip install mysql-connector-python')
            import mysql.connector

        mydb = mysql.connector.connect(
        host=f"{MYSQL_DATABASE_HOST}",
        user=f"{MYSQL_DATABASE_USER}",
        password=f"{MYSQL_DATABASE_PASSWORD}"
        )
        print('Connected to MySQL successfully')

        mycursor = mydb.cursor()
        mycursor.execute(f"CREATE DATABASE {MYSQL_DATABASE_NAME}")
        print('Created MySQL database successfully')
        if not mysql_installed:
            os.system('pip uninstall mysql-connnector-python')
    except Exception as e:
        print(e)

def create_env_file(creds):
    MYSQL_DATABASE_NAME = creds['MYSQL_DATABASE_NAME']
    MYSQL_DATABASE_USER = creds['MYSQL_DATABASE_USER']
    MYSQL_DATABASE_PASSWORD = creds['MYSQL_DATABASE_PASSWORD']
    MYSQL_DATABASE_HOST = creds['MYSQL_DATABASE_HOST']
    MYSQL_DATABASE_PORT = creds['MYSQL_DATABASE_PORT']
    f = open(os.path.join(BASE_DIR,'simpletodo','.env'), 'w')
    txt = f"DJANGO_SECRET_KEY=django-insecure-q113-fz49lh6eg8qg=yd)#9v4a$lg%h0p#6uiz3(-&+f93l%h6\nMYSQL_DATABASE_NAME={MYSQL_DATABASE_NAME}\nMYSQL_DATABASE_USER={MYSQL_DATABASE_USER}\nMYSQL_DATABASE_PASSWORD={MYSQL_DATABASE_PASSWORD}\nMYSQL_DATABASE_HOST={MYSQL_DATABASE_HOST}\nMYSQL_DATABASE_PORT={MYSQL_DATABASE_PORT}"
    f.write(txt)
    f.close()
    print('Created .env file')

def main():
    create_migrations_dirs()
    unzip_static_files('static.zip')
    MYSQL_DATABASE_NAME = input('Enter a name for your database: ') #personal_simpletodo
    MYSQL_DATABASE_USER = input('Enter user (type in "root" if unsure): ') #root
    MYSQL_DATABASE_PASSWORD = input('Enter your MySQL password: ') #utkarsh
    MYSQL_DATABASE_HOST = input('Enter host (commonly localhost): ')#localhost
    MYSQL_DATABASE_PORT = input('Enter Port (probably 3306 in most cases): ')#3306
    MYSQL_CREDS = {
            'MYSQL_DATABASE_NAME' : MYSQL_DATABASE_NAME,
            'MYSQL_DATABASE_USER' : MYSQL_DATABASE_USER,
            'MYSQL_DATABASE_PASSWORD' : MYSQL_DATABASE_PASSWORD,
            'MYSQL_DATABASE_HOST' : MYSQL_DATABASE_HOST,
            'MYSQL_DATABASE_PORT' : MYSQL_DATABASE_PORT,
    }
    mysql_db_setup(MYSQL_CREDS)
    create_env_file(MYSQL_CREDS)
    print('Done\n')
    print('Run the following command to install required packages:\n')
    print("pip install -r requirements.txt")
    print("\n")
    print('To create the required tables in the MySQL database, run the following commands:\n')
    print('- python manage.py makemigrations')
    print('- python manage.py migrate')

if __name__ == "__main__":
    main()