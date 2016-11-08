#!/bin/bash

# this script is used to remove all pyc temp files from the project
find ./ -name *.pyc | xargs rm -rf
