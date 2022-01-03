
data "aws_iam_policy" "data_generator_policy" {
  name        = var.aws_iam_policy_name
}

data "aws_iam_role" "data_generator_role" {
  name = var.aws_iam_role_name
}
