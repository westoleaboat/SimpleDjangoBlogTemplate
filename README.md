# SimpleDjangoBlogTemplate
simple template for a blog in Django (w/no styling)

![Screenshot_select-area_20230829002006](https://github.com/westoleaboat/SimpleDjangoBlogTemplate/assets/68698872/a2de13a1-9289-402f-b33b-235b05ed9cd0)



## To Test Locally
clone this repository
```
git clone https://github.com/westoleaboat/SimpleDjangoBlogTemplate.git

```
create a virtual environment (Optional but recommended)
```
python -m venv myenv

# activate env
source myenv/bin/activate
# on windows
myenv/Scripts/activate
```
Install dependencies
```
cd SimpleDjangoBlogTemplate
pip install -r requirements.txt
```

Apply migrations:
```
python manage.py makemigrations
python manage.py migrate
```
Create a SuperUser:
```
python manage.py createsuperuser
```
Start development Server:
```
python manage.py runserver
```
Access the site:
navigate to **http://localhost:8000**. The admin interface can be accessed at **http://localhost:8000/admin**


