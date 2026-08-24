# Infrastructure as Code (Terraform)

> _2026-08-25_ | Category: **cloud**

Code your infrastructure.

Clicking through AWS console is bad: not reproducible, no history, prone to error.

```hcl
provider "aws" { region = "us-east-1" }

resource "aws_instance" "web" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t2.micro"
  tags = { Name = "HelloWorld" }
}

resource "aws_s3_bucket" "b" {
  bucket = "my-tf-test-bucket"
}
```

Commands:
`terraform init` (download plugins)
`terraform plan` (see what will change)
`terraform apply` (execute changes)

**State File**: Terraform keeps a `.tfstate` file mapping code to real resources. Store this securely in an S3 bucket!
