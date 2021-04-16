DROP DATABASE testApi IF EXISTS;
CREATE DATABASE testApi;

-- do we mean first name and amily name?
DROP TABLE user IF EXISTS;
CREATE TABLE IF user (
    id serial PRIMARY KEY,
    name VARCHAR (50) NOT NULL,
    family VARCHAR (50) NOT NULL,
    description TEXT);

CREATE USER root WITH PASSWORD 'Vand^2VictoDataEngineerRoot';
ALTER USER root WITH SUPERUSER;
GRANT ALL PRIVILEGES ON DATABASE testApi TO root;


