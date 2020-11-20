# rotate-ssh-aws
Lambda to rotate the SSH keys using Secrets Manager.

Initial code is taken from https://github.com/aws-samples/aws-secrets-manager-ssh-key-rotation/tree/master/lambda.
Code is modified to add SSH Public key to an S3 Object, which can be pulled by the new EC2 instances which come up (due to auto-scaling)

`cloudformation.yaml` is a Cloud Formation script to create the Lambda Function in AWS.

In cloudformation.yaml, please change few of the parameters (look for *FIXME* in `cloudformation.yaml`) based on your setup before providing the script to AWS Cloud Formation.

Following parameters need to be changed:

- S3 Bucket where Public key will be stored
- S3 object where Public key will be stored
- Usernames for the Linux User that is used to log into the Workers
- S3 URI of Lambda code
- ARN of S3 Bucket where Public key will be stored
- Security Group IDs
- Subset IDs

# blog
Please go though the following blog for detailed step by step procedure to setup
https://medium.com/@singhamrit/ec2-mfa-ssh-key-rotation-fddc807f9318
