# EC2

An EC2 instance is simply a virtual server in Amazon Web Services terminology.

EC2 metadata: Instance metadata is data about your instance that you can use to configure or manage the running instance. Instance metadata includes the following:

metadata endpoint: used to list all reports and retrieve report details such as row and
column selections.

the directory structure will be something like this:
`http://169.254.169.254/latest/meta-data/iam/security-credentials/admin`

[IAM](https://github.com/detelin/aws/blob/master/ec2-instance-metadata.md)
