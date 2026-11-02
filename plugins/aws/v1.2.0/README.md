# Syncany AWS Source Plugin (`v1.2.0`)

Multi-region **AWS** source plugin for Syncany (`18` tables across Account, IAM, S3, EC2, VPC, Route53, WAFv2, Lambda, DynamoDB, CloudFront, and Cognito).

## Included Tables (18)

| Table | Columns | Description |
| :--- | :---: | :--- |
| `aws_accounts` | 9 | AWS STS caller account metadata |
| `aws_cloudfront_distributions` | 15 | AWS CloudFront CDN distributions |
| `aws_cognito_user_pools` | 13 | AWS Cognito User Pools |
| `aws_dynamodb_tables` | 14 | AWS DynamoDB tables |
| `aws_ec2_images` | 13 | AWS EC2 Amazon Machine Images (AMIs) owned by the account |
| `aws_ec2_instances` | 18 | AWS EC2 compute instances across accounts and regions |
| `aws_ec2_network_interfaces` | 15 | AWS EC2 elastic network interfaces (ENIs) |
| `aws_ec2_route_tables` | 12 | AWS VPC route tables |
| `aws_ec2_security_groups` | 14 | AWS EC2/VPC security groups and ingress/egress rules |
| `aws_ec2_subnets` | 14 | AWS VPC subnets |
| `aws_ec2_volumes` | 16 | AWS EBS volumes |
| `aws_ec2_vpcs` | 12 | AWS Virtual Private Clouds (VPCs) |
| `aws_iam_users` | 13 | AWS IAM users, MFA posture, and access key metadata |
| `aws_lambda_functions` | 16 | AWS Lambda serverless functions |
| `aws_route53_hosted_zone_resource_record_sets` | 12 | AWS Route53 DNS resource record sets per hosted zone |
| `aws_route53_hosted_zones` | 11 | AWS Route53 public and private hosted zones |
| `aws_s3_buckets` | 12 | AWS S3 buckets and encryption/public-access posture |
| `aws_wafv2_web_acls` | 14 | AWS WAFv2 Regional and CloudFront Web ACLs |
