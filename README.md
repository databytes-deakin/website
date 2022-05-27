# DataBytes Website
 DataBytes Company Landing Page.

## Foundations
### Requirements
* Python v3.8 (or newer)
* Django v4.04 (or newer)

### Installation 
`pip install -r requirements.txt`

### Files and Folders
* manage.py - Command Line tool to manage Django project
* models.py - Database management tool
* urls.py - Holds and manages the URL extensions for all template files
* views.py - Renders HTML templates and loads data from databases
* settings.py - Config file for Django
* db-databytes.sqlite3 - Database file
* /DBweb - Django application directory
* /DBweb/templates - HTML template directory
* /DBweb/static - assets for template directory

## Running Server
`python manage.py runserver`
<br>

**Note: Must be within the `/DB-Website/databytes` directory to execute command.**

## Accessing Admin Panel
When running server, go to http://127.0.0.1:8000/admin
<br>

Log in using `admin` and `databytes` for quick backend access
<br>

For superuser access, add a user: `python manage.py createsuperuser` and follow prompts
   
## Troubleshooting
### Editing models.py
After editing `models.py`, the Django project and the SQLite database must be updated.
Run `python manage.py makemigrations` and `python manage.py migrate`
