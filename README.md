# github_report

Github Report is a project that generates a report of all opened, closed, and in progress pull requests in the last week for a given repository and prints an email summary

## Requirements

- Clone this repository
- Docker installed

## How to execute

This app is executed on Docker.
First you need to build the Docker image with this:

`docker image build -t github-report .`

Once you have created the docker image you can execute your container with:

`docker container run -e OWNER=<repo_owner> -e REPO=<repo_name> -e FROM=<from_email> -e TO=<to_email> github-report`

**OWNER:** owner of the repo you want to generate the report from

**REPO:** name of the repo you want to generate the report from

**FROM:** email sender

**TO:** email recipient
