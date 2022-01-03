resource "aws_iam_instance_profile" "target-example-box" {
  name_prefix = "linux-example-target"
  role = data.aws_iam_role.data_generator_role.name

  tags = {
    Name  = var.aws_tag_instance_profile_name
    Owner = var.aws_tag_owner
  }
}

resource "aws_instance" "data_generator" {
  ami           = var.aws_ami
  instance_type = var.aws_instance_type
  key_name      = var.aws_key_name

  root_block_device {
    delete_on_termination = true
    encrypted             = true
    tags = {
      Name  = var.aws_tag_ebs_name
      Owner = var.aws_tag_owner
    }
    volume_size = 8
    volume_type = "gp2"
  }

  iam_instance_profile   = aws_iam_instance_profile.data_generator_profile.name
  vpc_security_group_ids = [aws_security_group.allow_ssh.id]

  tags = {
    Name  = var.aws_tag_instance_name
    Owner = var.aws_tag_owner
  }
}

resource "null_resource" "provisioner" {
  triggers = {
    public_ip = aws_instance.data_generator.public_ip
  }

  connection {
    type        = "ssh"
    user        = var.aws_instance_user
    host        = aws_instance.data_generator.public_ip
    private_key = file(var.aws_key_path)
  }

  provisioner "file" {
    source      = "scripts/box1_script.bh"
    destination = "/home/${var.aws_instance_user}/run.bh"
  }

  provisioner "remote-exec" {
    inline = [
      "chmod +x /home/${var.aws_instance_user}/run.bh",
      "/home/${var.aws_instance_user}/run.bh"
    ]
  }
}
