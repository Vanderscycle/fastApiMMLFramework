CREATE DATABASE testApi;

-- do we mean first name and amily name?
CREATE TABLE IF NOT EXISTS user (
    id serial PRIMARY KEY,
    name VARCHAR (50) NOT NULL,
    family VARCHAR (50) NOT NULL,
    description TEXT);

CREATE USER root WITH PASSWORD 'Vand^2VictoDataEngineerRoot';
ALTER USER root WITH SUPERUSER;
GRANT ALL PRIVILEGES ON DATABASE testApi TO root;


