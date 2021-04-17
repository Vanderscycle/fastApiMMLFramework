Simple backend api.

I am having issues with kinsing and kdevtmpfsi attacks on the linode server so you will have to create an env file at the root of the folder, input the desired username,password and dbName.

Because I can't get the postgres environment variables working proprely, you will have to modify the docker-compose file and manually input the values.

Lastly, your cryptocurrency is going up because we are in a bull market and I can't wait to buy a gpu when it finally crashes :) 

For a quick demo(swagger docs) go to:
```bash
# please send me an email to request the new ip
```

To run the project locally:
```bash
docker-compose up --build --remove-orphans
or
bash start.sh
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
It took roughly 30 hours since I never created a full API (only a single POST/GET using flask for a small ML model). 

The approach was as follow:
  * learned about POST/GET/PATCH/DELETE using local variables,
  * dockerize the simple API and tested locally,
  * refactored the project. Incorporated sqlalchemy and a Postgres container,
  * create docker-compose and tested locally for the communication between the API and its database,
  * began work on unit tests,
  * use .env file to hide passwords and critical info (not working at the moment). Created so many issues on the DB that I created a new branch and rollback the main branch (I am the only one working on that pre-production branch),
  * completed unit tests and tested with docker-compose. (need to add it to GitHub actions),
  * configured ubuntu server with my dot-files (automatically installs python, mongo,Postgres, Docker ,docker-compose, zsh, nvim, etc...),
  * wrote the documentation.

Known issues:
  * init.sql is not working (imported from a previous project), but the tables are created regardless because of sqlalchemy—more time is required to investigate.
  * get all users returns a list of dictionaries.
  * data validation with Pydantic and the ORM model is weird, and despite some fields being specified for strings, they allow for ints and floats.
  * The code could always use more comments.
  * unit tests functions are not reused because I don't know how to do so just yet.
  * The first boot of docker-compose up can be problematic. Stopping and restarting the containers solves the DB issue (do not delete containers).  
  
Future developments:
  * troubleshooting of .env and passwords.
