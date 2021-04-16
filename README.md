Simple backend api.

For a quick demo(swagger docs) go to:
```bash
http://172.105.111.30:8000/docs
```

To run the project locally:
```bash
docker-compose up --build --remove-orphans
```
Can run the tests while the container is running using:
```bash
docker-compose exec api pytest ../tests/mainTest.py -v
```
Time didn't allow me full integration with github actions.

FastApi has swagger documentation as part of its library and can be accessed(if ran locally) using:
```bash
http://localhost:8000/docs
```

Description of the journey:
Took roughly 30 hours since I never created a full api (only GET using flask for a small ML model). 

The approach was as follow:
  * learned about POST/GET/PATCH/DELETE using local variables,
  * dockerize the simple api and tested locally,
  * refactored the project. Incorporated sqlalchemy and a postgres container,
  * create docker-compose and tested locally for the communication between the api and its database,
  * began work on unitests,
  * use .env file to hide passwords and critical info (not working at the moment). Created so many issues on the db that I created a new branch and rollback the main branch (I am the only one working on that pre-production branch),
  * completed unitests and tested with docker-compose. (need to add it to github actions),
  * configured ubuntu server with my dot-files (automatically installs python, mongo,postgres, docker ,docker-compose, zsh, nvim, etc...),
  * wrote the documentation.

Known issues:
  * init.sql is not working (imported from a previous project) but the tables are created regardless because of sqlalchemy. More time required to investigate.
  * get all users returns a list of dictionaries.
  * datavalidation with pydantic and the orm model is weird and despite some fields being specified for strings they allow for ints and floats.
  * The code could always use more comments.
  * unittest functions are not being reused because I don't know how to do so just yet.
  * The first boot of docker-compose up can be problematic. Stopping and restarting the containers solves the db issue (do not delete containers).  
  
Future developments:
  * troubleshooting of .env and passwords.
