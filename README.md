# IMLP 2017

Workout plan for IMLP 2017

# S3 Upload Set Up
1. Set up and activate virtual env with python 3
2. Install requirements: `pip install -r requirements.txt`
3. Set up AWS credentials: `aws configure --profile imlp-2017`
3. Execute script to update S3 bucket website with `public` folder contents: `./sync-s3`
