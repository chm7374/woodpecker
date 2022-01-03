# Allow SSH
resource "aws_security_group" "allow_ssh" {
  name        = var.aws_sg_name
  description = "Allow SSH inbound traffic from the runners IP"
  vpc_id      = data.aws_vpc.main.id

  ingress {
    description = "SSH from the test runner"
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["${chomp(data.http.myip.body)}/32"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name  = var.aws_tag_sg_name
    Owner = var.aws_tag_owner
  }
}
