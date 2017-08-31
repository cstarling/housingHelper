#!/usr/bin/env bash


cd housingHelper/
nohup python -u app.py > ../housingHelper.log 2>&1 &
