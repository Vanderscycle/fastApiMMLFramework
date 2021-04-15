#!/bin/bash
# Local .env
if [ -f ./src/.env ]; then
    # Load Environment Variables
    export $(cat ./src/.env | grep -v '#' | awk '/=/ {print $1}')
    # For instance, will be example_kaggle_key
    echo $PGUSER
fi
docker-compose up --build --remove-orphans
