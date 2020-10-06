#!/bin/bash
docker-compose down
docker-compose -f docker-compose.yml -f production.yml up --build 2>&1 >logs.txt
