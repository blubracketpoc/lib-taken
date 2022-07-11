resource "aws_s3_bucket" "bucket" {
  bucket = "my-tf-test-bucket"
  acl    = "public-read"
  tags = {
    Name                 = "My bucket"
    Environment          = "Dev"
    git_commit           = "9ac2d7f1a2f856767de5a2ef3722ef85067e256d"
    git_file             = "infraascode.tf"
    git_last_modified_at = "2021-07-20 22:45:36"
    git_last_modified_by = "59456239+mauricecevans@users.noreply.github.com"
    git_modifiers        = "59456239+mauricecevans"
    git_org              = "BluDemoGH"
    git_repo             = "terragoat"
    yor_trace            = "42594d92-a0fb-4c47-bd49-c8d27d452857"
  }
}
