CREATE DATABASE testApi;

-- do we mean first name and amily name?
CREATE TABLE IF NOT EXISTS userDescription (
    ID serial PRIMARY KEY,
    Name VARCHAR (50) NOT NULL,
    Family VARCHAR (50) NOT NULL,
    Description TEXT, 
);

CREATE USER root WITH PASSWORD 'Vand^2VictoDataEngineerRoot';
ALTER USER root WITH SUPERUSER;
CREATE DATABASE userDescription;
GRANT ALL PRIVILEGES ON DATABASE userDescription TO root;


