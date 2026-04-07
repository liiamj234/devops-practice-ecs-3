terraform {
  backend "s3" {
    bucket       = "liam-tfstate-devops-practice-2026-003"
    key          = "devops-practice-ecs/terraform.tfstate"
    region       = "ap-southeast-2"
    encrypt      = true
    use_lockfile = true
  }
}