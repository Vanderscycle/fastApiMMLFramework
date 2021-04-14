#!/bin/sh
# start the api (don't know why localhost has to be specified for it to run)
uvicorn main:app --reload --host 0.0.0.0 --port 80
