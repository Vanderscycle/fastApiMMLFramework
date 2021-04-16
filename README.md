Simple backend api.
To run the project locally:
```bash
docker-compose up --build --remove-orphans
```
Can run the tests while the container is running using:
```bash
docker-compose exec api pytest ../tests/mainTest.py -v
```
Time didn't allow me full integration with github actions.

FastApi has swagger documentation as part of its library and can be accessed using:
```bash
http://localhost:8000/docs
```

Description of the journey:
Took roughly 30 hours since I never create a full api (only GET using flask). 

The approach was as follow:
  * learn about POST/GET/PATCH/DELETE using local variables,
  * dockerize the simple api and test locally,
  * refactor the project and add sqlalchemy and a postgres container,
  * create docker-compose and test locally for the communication between the api and its database,
  * begin work on unittest,
  * use .env file to hide passwords and critical info (not working at the moment)
