# circle-see-why
This script helps fetch credit usage of a branch in Circle CI

Remember to set environmental variables in script.sh relating to your circle ci project

$WORKFLOW can be set as an environmental variable or passed in as an argument

## Variables
export VCS=

export ORG=

export REPO=

For these three see https://circleci.com/docs/2.0/api-developers-guide/#getting-started-with-the-api

export CIRCLE_TOKEN=<Personal API> https://circleci.com/docs/2.0/managing-api-tokens/

export WORKFLOW=

# Usage
Usage: ./script.sh \<branch name> ?\<workflow name>

# Example output
<img width="1422" alt="image" src="https://user-images.githubusercontent.com/97483533/164077578-590a58ab-df98-4e62-b95f-ebce2c7c2fdd.png">
