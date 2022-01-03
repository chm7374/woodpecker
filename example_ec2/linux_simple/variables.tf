# AWS Region
variable "aws_region" {
  default = "us-east-2"
  type    = string
}

# AWS VPC ID
variable "aws_vpc_id" {
  default = "vpc-79c0a512"
  type    = string
}

variable "aws_ami" {
  default = "ami-0bae7412735610274"
  type = string
}

# AWS Instance type
variable "aws_instance_type" {
  default = "t2.micro"
  type    = string
}

# AWS SSH Keypair name
variable "aws_key_name" {
  default = "datagen"
  type    = string
}

# AWS SSH Key path
variable "aws_key_path" {
  default = "~/.ssh/datagen.pem"
  type    = string
}

# AWS IAM Policy Name
variable "aws_iam_policy_name" {
  default = "example-weak-policy"
  type    = string
}

# AWS IAM Policy Description
variable "aws_iam_policy_description" {
  default = "Allows EC2 instances to generate data on EBS volumes"
  type    = string
}

# AWS IAM Policy Tag Name
variable "aws_tag_iam_policy_name" {
  default = "Linux Example Target IAM Policy"
  type    = string
}

# AWS IAM Role Name
variable "aws_iam_role_name" {
  default = "linux-ex-target-iam-role"
  type    = string
}

# AWS IAM Role Tag Name
variable "aws_tag_iam_role_name" {
  default = "Linux Example Target IAM Role"
  type    = string
}

# Patrolaroid Repo Path
variable "patrolaroid_repo_path" {
  default = "../../../patrolaroid"
  type    = string
}

# AWS Instance user
variable "aws_instance_user" {
  default = "ubuntu"
  type    = string
}

# AWS Security Group Name
variable "aws_sg_name" {
  default = "box1-ssh-sg"
  type    = string
}

# Tag 'Name' value
variable "aws_tag_instance_profile_name" {
  default = "Linux Example Target Profile"
  type    = string
}

# Tag 'Name' value
variable "aws_tag_instance_name" {
  default = "Linux-Example-Target-box"
  type    = string
}

# Tag 'Name' value
variable "aws_tag_sg_name" {
  default = "Linux Example Target Limited SSH"
  type    = string
}

# Tag 'Name' value
variable "aws_tag_ebs_name" {
  default = "Linux Example Target Root Volume"
  type    = string
}

# Tag 'Owner' value
variable "aws_tag_owner" {
  default = "Cameron MacDonald"
  type    = string
}
