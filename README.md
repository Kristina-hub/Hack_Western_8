# Hack Western 8

## Table of Contents
- [About](#About)
- [Tentative Goals](#Tentative-Goals)
- [Anticipated Impact](#Anticipated-Impact)
- [Possible Action Plan](#Possible-Action-Plan)
- [Steps](#Steps)
- [Deliverables](#Deliverables)
- [Installation](#Installation)
- [Demo](#Demo)
- [Git Reference](#Git-Reference)
- [AWS Reference](#AWS-Reference)

## About
about...

## Tentative Goals
1. 
2. 
3. 

## Anticipated Impact
impact...

## Installation
```shell script
$ pip3 install -r requirements.txt
```

## Demo
Created using: https://ezgif.com/maker<br/><br/>
  ![](./static/img/demo.gif)

## AWS Implementation
### Running Locally using Flask:
```shell script
$ touch application.py

from flask import Flask
application = Flask(__name__)
@application.route('/')
def hello_world():
	return 'Hello World'
```
```shell script
$ export FLASK_APP="application.py"
$ flask run
```
Now runs locally: <br/>
http://127.0.0.1:5000/<br/>

### AWS Elastic Beanstalk: 
```shell script
AWS -> Services -> Elastic beanstalk <br/>
Create New Application called syllabus-manager using Python <br/>
Create New Environment called syllabus-manager-env using Web Server Environment <br/>
```
### Link AWS Code Pipeline to Github for Continuous Deployment:
```shell script
Services -> Developer Tools -> CodePipeline
Create Pipeline called syllabus-manager
GitHub version 2 -> Connect to Github
Connection name is connection -> Install a New App -> Choose repo name -> Skip build stage -> Deploy to AWS Elastic Beanstalk
```
This link is no longer local: <br/>
http://hack-western-8-env.eba-a5injkhs.us-east-1.elasticbeanstalk.com/ <br/>

### Register an AWS Route 53 Domain:
```shell script
Route 53 -> Registered Domains -> Register Domain -> hack-western-8.com -> Check <br/>
Route 53 -> Hosted zones -> Create Record -> Route Traffic to IPv4 Address -> Alias -> Elastic Beanstalk -> hack-western-8-env -> Create Records
Create another record but with alias www.
```
Now we can load the website using:<br/>
[hack-western-8.com](hack-western-8.com)<br/>
www.hack-western-8.com<br/>
Note that it says "Not Secure" beside the link<br/>

### Add SSL Certificate to use HTTPS: 
```shell script
Certificate manager -> Request a Public Certificate -> Domain Name "hack-western-8.com" and "*.hack-western-8.com" -> DNS validation -> Request
dig +short CNAME in terminal -> no output? -> Certificate -> Domains -> Create Records in Route 53
Elastic Beanstalk -> Environments -> Configuration -> Capacity -> Enable Load Balancing
Load balancer -> Add listener -> Port 443 -> Protocol HTTPS -> SSL certificate -> Save -> Apply
```
Now we can load the website using:<br/>
https://hack-western-8.com<br/>
https://www.hack-western-8.com<br/>
Note that there is a lock icon beside the link to indicate that we are using a SSL certificate and so we are secure<br/>