# Hack Western 8

## Table of Contents
- [About](#About)
- [Impact](#Impact)
- [Installation](#Installation)
- [Demo](#Demo)
- [Flask](#Flask)
- [AWS Elastic Beanstalk](#AWS-Elastic-Beanstalk)
- [AWS CodePipeline ](#AWS-CodePipeline )
- [AWS Route 53](#AWS-Route-53)
- [AWS Certificate Manager](#AWS-Certificate-Manager)

## About
The majority of students do not have a lot of spare cash so it can be challenging for them to choose between investing in their own future or the causes that they believe in to build a better future for others. What if I told you that there is a way to support your favourite charities while also saving money? Students no longer need to choose between investing and donating!<br/><br/>
Our mission is to encourage students to invest in companies that make donations to charities on their behalf.<br/><br/>
Large companies have the capital needed to make sizeable donations but many of these acts go unnoticed. That's why we created a platform that connects students to companies that make donations to the charities that they are interested in. Students will be able to support charities they believe in by investing in companies that are driven to make donations to such causes.<br/><br/>
Students will be able to not only learn more about financial planning but also help support various philanthropic services.<br/>

## Impact
1. Promote financial planning to students
2. Encourage companies to support charities
3. Encourage students to support companies that make these contributions

## Installation
```shell script
$ python list
$ python3 -m venv .venv
$ source .venv/bin/activate
$ pip3 install --upgrade pip
$ pip3 install -r requirements.txt
$ pip3 install google
$ python -m spacy download en_core_web_sm
```

## Demo
Created using: https://ezgif.com/maker<br/><br/>
  ![](./static/img/demo.gif)

## Flask
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

## AWS Elastic Beanstalk
Create a Web Server Environment: 
```shell script
AWS -> Services -> Elastic beanstalk
Create New Application called hack-western-8 using Python
Create New Environment called hack-western-8-env using Web Server Environment
```
## AWS CodePipeline
Link to Github for Continuous Deployment:
```shell script
Services -> Developer Tools -> CodePipeline
Create Pipeline called hack-western-8
GitHub Version 2 -> Connect to Github
Connection Name -> Install a New App -> Choose Repo Name -> Skip Build Stage -> Deploy to AWS Elastic Beanstalk
```
This link is no longer local: <br/>
http://hack-western-8-env.eba-a5injkhs.us-east-1.elasticbeanstalk.com/ <br/>

## AWS Route 53
Register a Domain:
```shell script
Route 53 -> Registered Domains -> Register Domain -> hack-western-8.com -> Check
Route 53 -> Hosted zones -> Create Record -> Route Traffic to IPv4 Address -> Alias -> Elastic Beanstalk -> hack-western-8-env -> Create Records
Create another record but with alias www.
```
Now we can load the website using:<br/>
[hack-western-8.com](http://hack-western-8.com)<br/>
www.hack-western-8.com<br/>
http://hack-western-8.com<br/>
http://www.hack-western-8.com<br/>
Note that it says "Not Secure" beside the link<br/>

## AWS Certificate Manager
Add SSL to use HTTPS: 
```shell script
AWS Certificate Manager -> Request a Public Certificate -> Domain Name "hack-western-8.com" and "*.hack-western-8.com" -> DNS validation -> Request
$ dig +short CNAME -> No Output? -> Certificate -> Domains -> Create Records in Route 53
Elastic Beanstalk -> Environments -> Configuration -> Capacity -> Enable Load Balancing
Load balancer -> Add listener -> Port 443 -> Protocol HTTPS -> SSL certificate -> Save -> Apply
```
Now we can load the website using:<br/>
https://hack-western-8.com<br/>
https://www.hack-western-8.com<br/>
Note that there is a lock icon beside the link to indicate that we are using a SSL certificate so we are secure<br/>

## FavIcon
Created icon for tab using:<br/>
https://realfavicongenerator.net/<br/>
Where we obtained the image:<br/>
https://www.svgrepo.com/svg/223838/growth-investment<br/>

## References
Pictures used for charities:<br/>
Animals: https://www.pexels.com/photo/photo-of-elephants-on-grass-3551498/<br/>
Health: https://www.pexels.com/photo/person-in-white-long-sleeve-shirt-holding-injection-3985166/<br/>
Education: https://www.pexels.com/photo/close-up-of-apple-on-top-of-books-256520/<br/>
Community: https://www.pexels.com/photo/house-lights-turned-on-106399/<br/>
Environment: https://www.pexels.com/photo/green-leafed-trees-302804/<br/>
Human Rights: https://www.pexels.com/photo/boy-wearing-green-crew-neck-shirt-jumping-from-black-stone-on-seashore-939702/<br/>

Pictures for home page:<br/>
https://www.vecteezy.com/photo/3334027-the-man-show-of-money-in-glass-with-plant-growing<br/>
https://www.vecteezy.com/photo/2928574-save-money-with-stack-coin-growing-your-business-concept-young-plant-growing-in-money-stack-coin<br/>

