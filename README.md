# pycubedata
Rest Apis usingh flask and database operations

Project to read json file and store data into NoSQl Database.

I have used mongodb here.

Prerequisites install mongodb at local.

Steps to install mongodb :-

Download mongodb from the https://fastdl.mongodb.org/linux/mongodb-linux-x86_64-ubuntu1604-3.6.23.tgz

```
wget https://fastdl.mongodb.org/linux/mongodb-linux-x86_64-ubuntu1604-3.6.23.tgz
```

Download the project at local using 

```
git clone https://github.com/mindcrusher11/cubedata.git
```

I have used Scala here as currently I am using java and scala more, I also added apis with python as well.

***Project Structure imn the app folder***
```

controllers - for the apis.
 
modela - model class objects are defined here.

repository - database repositories are defined here.

service - business logic is defined here.

iservice - it contains interface for implementation of services.

```
 
***Database Setup***

```
Unzip tar file downloaded for ubuntu

tar -xzf mongodb-linux-x86_64-ubuntu1604-3.6.23.tgz

cd mongodb-linux-x86_64-ubuntu1604-3.6.23/bin

./mongod

Server Started

Access the client using client 

./mongo

Database is up and running

Create Text Index in mongodb 

```

Prerequisites for installing dependencies

```
pip install Flask-PyMongo
pipenv install flask-restplus
pipenv install flask-marshmallow
pipenv install flask-sqlalchemy
pipenv install marshmallow-sqlalchemy
```

Run application

```
export FLASK_APP=app.main.controller.legislationroutes
flask run
```

Output will be 

```
(venv) gaur@rigu:~/PycharmProjects/cubedata$ flask run
 * Serving Flask app 'app.main.controller.legislationroutes' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
^C(venv) gaur@rigu:~/PycharmProjects/cubedata$ git clone https://github.com/mindcrusher11/pycubedata.git
Cloning into 'pycubedata'...
remote: Enumerating objects: 5, done.
remote: Counting objects: 100% (5/5), done.
remote: Compressing objects: 100% (5/5), done.
remote: Total 5 (delta 0), reused 0 (delta 0), pack-reused 0
Unpacking objects: 100% (5/5), done.
```

Text index on Mondgodb after inserting data into mongodb

** Testing and logging pending


