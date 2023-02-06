#!/bin/bash

source .env

port=$APP_PORT

uvicorn app.main:app --host 0.0.0.0 --port $port --reload
