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

def create_env_file(creds):
    f = open(os.path.join(BASE_DIR,'simpletodo','.env'), 'w')
    txt = f"DJANGO_SECRET_KEY=django-insecure-q113-fz49lh6eg8qg=yd)#9v4a$lg%h0p#6uiz3(-&+f93l%h6"
    f.write(txt)
    f.close()
    print('Created .env file')

def main():
    try:
        create_migrations_dirs()
        unzip_static_files('static.zip')
        print('Done\n')
        print('Run the following command to install required packages:\n')
        print("pip install -r requirements.txt")
        print("\n")
        print('To create the required tables in the MySQL database, run the following commands:\n')
        print('- python manage.py makemigrations')
        print('- python manage.py migrate')
    except Exception as e:
        print("Could not complete setup")
        print(str(e))
if __name__ == "__main__":
    main()