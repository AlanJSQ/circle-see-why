#!/bin/bash

export VCS=
export ORG=
export REPO=
export CIRCLE_TOKEN=
export WORKFLOW=

Usage() {
    echo "Usage: ./script.sh <Branch name> Opt: <Workflow name>"
}

Help() {
    echo "This script helps fetch credit usage of a branch in Circle Ci"
    echo "Remember to set environmental variables in script.sh relating to your project"
    echo "WORKFLOW can be set as an environmental variable or passed in as an argument"
    Usage
}

while getopts ":h" option; do
   case $option in
      h) # display usage/help
         Help
         exit;;
   esac
done

if [ -z "$1" ]; then
    Usage
else 
    if [ -eq "$1" "help" ]; then
        Usage
    fi
    if [ -n "$2" ]; then 
        export WORKFLOW="$2"
    fi
    python3 circle.py $1 $WORKFLOW
fi

