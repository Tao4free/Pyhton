# This is a simple example for deploying an app in Google Cloud App Engine

## Steps to do this
1. upload this folder to gcp
2. Kick-start by running the code `dev_appserver.py ./`
3. Preview by choosing `Web preview -> Preview on port 8080`
4. deploy by enter `gcloud app deploy app.yaml`
   choose the region and after deployment the URL will show
5. check log by `gcloud app logs tail -s default`
