# DataBytes Website
 DataBytes Company Landing Page.

## Foundations
### Requirements
* Python3
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
* DBweb - Django application
* /DBweb/templates - HTML template files
* /DBweb/static - assets for template files

## Running Server
`python manage.py runserver`
<br>
*Note: Must be within the /DB-Website/databytes directory to execute command.*
   
## Troubleshooting
### Editing models.py
After editing `models.py`, the Django project and the SQLite database must be updated.
Run `python manage.py makemigrations` and `python manage.py migrate`
