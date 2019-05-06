# Clean-Blog


### xampp
first click on this like and download xampp according to your OS 
```
https://www.apachefriends.org/download.html
```
after that visite in your directory where you Download this file

then open your terminal :- 
install this software from super user
```
jai@jai:~/Downloads$ sudo su
[sudo] password for jai:  
root@jai:/home/jai/Downloads# ./xampp-linux-x64-7.1.28-0-installer.run
```

### Flask-SQLAlchemy
If you want to read more about Flask-SQLalchemy so you can simply visit on this link :- 
```
http://flask-sqlalchemy.palletsprojects.com/en/2.x/
```

https://stackoverflow.com/questions/27766794/switching-from-sqlite-to-mysql-with-flask-sqlalchemy
**Helping to connect to the database**
```
pip install flask-sqlalchemy
```

if you found this type error :- 
```
    return __import__("MySQLdb")
ModuleNotFoundError: No module named 'MySQLdb'
```

so install it :
```
pip install pymysql
```

and change this like 
BEFORE
```
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/Navgurukul' 
```
to 
AFTER
```
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/Navgurukul'
```