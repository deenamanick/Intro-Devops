# 🏗️ Terraform Basics: Infrastructure as Code (IaC)

> Introduction to Terraform: This lesson covers Terraform fundamentals, architecture, installation, configuration, state management, variables, provisioners, data sources, loops, and modules. By the end, you will understand how to create and manage cloud infrastructure using code.

## 1. What is Terraform?

Terraform is an open-source Infrastructure as Code (IaC) tool created by HashiCorp in 2014. It allows you to define, provision, and manage cloud and on-premises infrastructure using configuration files.

Instead of manually creating servers, networks, or databases through a cloud console, you can describe your infrastructure using Terraform's HashiCorp Configuration Language (HCL).

Key Features of Terraform:

1. Infrastructure as Code: Manage infrastructure using reusable configuration files.
2. Declarative Configuration: Define the desired infrastructure, and Terraform determines the necessary changes.
3. Multi-Cloud Support: Works with AWS, Azure, Google Cloud, and other platforms.
4. State Management: Tracks infrastructure resources and their configuration.
5. Reusable Modules: Organize infrastructure into reusable components.

Why is Terraform popular?

Terraform reduces manual infrastructure configuration, improves consistency, supports automation, and helps teams manage multiple environments using the same configuration.

## 2. Terraform Architecture

Terraform's architecture consists of several important components.

### A. Terraform Core

Terraform Core is responsible for reading configuration files, calculating infrastructure changes, and executing Terraform operations.

### B. Providers

Providers are plugins that allow Terraform to communicate with external platforms such as AWS, Azure, Google Cloud, and Kubernetes.

```
provider "aws" {
  region = "ap-south-1"
}
```

### C. Resources

Resources represent infrastructure components such as virtual machines, storage buckets, networks, and databases.

```
resource "aws_instance" "web" {
  ami           = var.ami_id
  instance_type = "t3.micro"
}
```

### D. State

Terraform maintains a state file (`terraform.tfstate`) that maps resources in your configuration to actual infrastructure.

### E. Plugins

Plugins extend Terraform's capabilities, including provider integrations and additional functionality.

### Terraform Architecture Workflow

\#chatgpt-mermaid-\_r_23c\_{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:16px;fill:rgb(13, 13, 13);}@keyframes edge-animation-frame{from{stroke-dashoffset:0;}}@keyframes dash{to{stroke-dashoffset:0;}}#chatgpt-mermaid-\_r_23c\_ .edge-animation-slow{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 50s linear infinite;stroke-linecap:round;}#chatgpt-mermaid-\_r_23c\_ .edge-animation-fast{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 20s linear infinite;stroke-linecap:round;}#chatgpt-mermaid-\_r_23c\_ .error-icon{fill:rgb(243, 243, 243);}#chatgpt-mermaid-\_r_23c\_ .error-text{fill:rgb(13, 13, 13);stroke:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_23c\_ .edge-thickness-normal{stroke-width:1px;}#chatgpt-mermaid-\_r_23c\_ .edge-thickness-thick{stroke-width:3.5px;}#chatgpt-mermaid-\_r_23c\_ .edge-pattern-solid{stroke-dasharray:0;}#chatgpt-mermaid-\_r_23c\_ .edge-thickness-invisible{stroke-width:0;fill:none;}#chatgpt-mermaid-\_r_23c\_ .edge-pattern-dashed{stroke-dasharray:3;}#chatgpt-mermaid-\_r_23c\_ .edge-pattern-dotted{stroke-dasharray:2;}#chatgpt-mermaid-\_r_23c\_ .marker{fill:rgb(143, 143, 143);stroke:rgb(143, 143, 143);}#chatgpt-mermaid-\_r_23c\_ .marker.cross{stroke:rgb(143, 143, 143);}#chatgpt-mermaid-\_r_23c\_ svg{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:16px;}#chatgpt-mermaid-\_r_23c\_ p{margin:0;}#chatgpt-mermaid-\_r_23c\_ .label{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";color:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_23c\_ .cluster-label text{fill:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_23c\_ .cluster-label span{color:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_23c\_ .cluster-label span p{background-color:transparent;}#chatgpt-mermaid-\_r_23c\_ .label text,#chatgpt-mermaid-\_r_23c\_ span{fill:rgb(13, 13, 13);color:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_23c\_ .node rect,#chatgpt-mermaid-\_r_23c\_ .node circle,#chatgpt-mermaid-\_r_23c\_ .node ellipse,#chatgpt-mermaid-\_r_23c\_ .node polygon,#chatgpt-mermaid-\_r_23c\_ .node path{fill:rgb(222, 234, 251);stroke:rgb(83, 154, 248);stroke-width:1px;}#chatgpt-mermaid-\_r_23c\_ .rough-node .label text,#chatgpt-mermaid-\_r_23c\_ .node .label text,#chatgpt-mermaid-\_r_23c\_ .image-shape .label,#chatgpt-mermaid-\_r_23c\_ .icon-shape .label{text-anchor:middle;}#chatgpt-mermaid-\_r_23c\_ .node .katex path{fill:#000;stroke:#000;stroke-width:1px;}#chatgpt-mermaid-\_r_23c\_ .rough-node .label,#chatgpt-mermaid-\_r_23c\_ .node .label,#chatgpt-mermaid-\_r_23c\_ .image-shape .label,#chatgpt-mermaid-\_r_23c\_ .icon-shape .label{text-align:center;}#chatgpt-mermaid-\_r_23c\_ .node.clickable{cursor:pointer;}#chatgpt-mermaid-\_r_23c\_ .root .anchor path{fill:rgb(143, 143, 143)!important;stroke-width:0;stroke:rgb(143, 143, 143);}#chatgpt-mermaid-\_r_23c\_ .arrowheadPath{fill:rgb(143, 143, 143);}#chatgpt-mermaid-\_r_23c\_ .edgePath .path{stroke:rgb(143, 143, 143);stroke-width:1px;}#chatgpt-mermaid-\_r_23c\_ .flowchart-link{stroke:rgb(143, 143, 143);fill:none;}#chatgpt-mermaid-\_r_23c\_ .edgeLabel{background-color:rgb(252, 252, 252);text-align:center;}#chatgpt-mermaid-\_r_23c\_ .edgeLabel p{background-color:rgb(252, 252, 252);}#chatgpt-mermaid-\_r_23c\_ .edgeLabel rect{opacity:0.5;background-color:rgb(252, 252, 252);fill:rgb(252, 252, 252);}#chatgpt-mermaid-\_r_23c\_ .labelBkg{background-color:rgba(252, 252, 252, 0.5);}#chatgpt-mermaid-\_r_23c\_ .cluster rect{fill:rgb(243, 243, 243);stroke:rgba(0, 0, 0, 0.1);stroke-width:1px;}#chatgpt-mermaid-\_r_23c\_ .cluster text{fill:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_23c\_ .cluster span{color:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_23c\_ div.mermaidTooltip{position:absolute;text-align:center;max-width:200px;padding:2px;font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:12px;background:rgb(243, 243, 243);border:1px solid rgba(0, 0, 0, 0.1);border-radius:2px;pointer-events:none;z-index:100;}#chatgpt-mermaid-\_r_23c\_ .flowchartTitleText{text-anchor:middle;font-size:18px;fill:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_23c\_ rect.text{fill:none;stroke-width:0;}#chatgpt-mermaid-\_r_23c\_ .icon-shape,#chatgpt-mermaid-\_r_23c\_ .image-shape{background-color:rgb(252, 252, 252);text-align:center;}#chatgpt-mermaid-\_r_23c\_ .icon-shape p,#chatgpt-mermaid-\_r_23c\_ .image-shape p{background-color:rgb(252, 252, 252);padding:2px;}#chatgpt-mermaid-\_r_23c\_ .icon-shape .label rect,#chatgpt-mermaid-\_r_23c\_ .image-shape .label rect{opacity:0.5;background-color:rgb(252, 252, 252);fill:rgb(252, 252, 252);}#chatgpt-mermaid-\_r_23c\_ .label-icon{display:inline-block;height:1em;overflow:visible;vertical-align:-0.125em;}#chatgpt-mermaid-\_r_23c\_ .node .label-icon path{fill:currentColor;stroke:revert;stroke-width:revert;}#chatgpt-mermaid-\_r_23c\_ .node .neo-node{stroke:rgb(83, 154, 248);}#chatgpt-mermaid-\_r_23c\_ [data-look="neo"].node rect,#chatgpt-mermaid-\_r_23c\_ [data-look="neo"].cluster rect,#chatgpt-mermaid-\_r_23c\_ [data-look="neo"].node polygon{stroke:url(#chatgpt-mermaid-\_r_23c\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_23c\_ [data-look="neo"].swimlane.cluster rect{filter:none;}#chatgpt-mermaid-\_r_23c\_ [data-look="neo"].node path{stroke:url(#chatgpt-mermaid-\_r_23c\_-gradient);stroke-width:1px;}#chatgpt-mermaid-\_r_23c\_ [data-look="neo"].node .outer-path{filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_23c\_ [data-look="neo"].node .neo-line path{stroke:rgb(83, 154, 248);filter:none;}#chatgpt-mermaid-\_r_23c\_ [data-look="neo"].node circle{stroke:url(#chatgpt-mermaid-\_r_23c\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_23c\_ [data-look="neo"].node circle .state-start{fill:#000000;}#chatgpt-mermaid-\_r_23c\_ [data-look="neo"].icon-shape .icon{fill:url(#chatgpt-mermaid-\_r_23c\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_23c\_ [data-look="neo"].icon-shape .icon-neo path{stroke:url(#chatgpt-mermaid-\_r_23c\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_23c\_ .node text{font-size:14px;font-weight:600;letter-spacing:normal;fill:rgb(0, 79, 153);}#chatgpt-mermaid-\_r_23c\_ .edgeLabels text{font-size:13px;font-weight:600;letter-spacing:-0.08px;fill:rgb(0, 79, 153);}#chatgpt-mermaid-\_r_23c\_ .node tspan[font-weight="normal"],#chatgpt-mermaid-\_r_23c\_ .edgeLabels tspan[font-weight="normal"]{font-weight:600;}#chatgpt-mermaid-\_r_23c\_ .edgeLabel .label rect{opacity:1;rx:13px;ry:13px;fill:rgb(245, 250, 255);stroke:rgb(206, 219, 229);stroke-width:1px;}#chatgpt-mermaid-\_r_23c\_ .node rect,#chatgpt-mermaid-\_r_23c\_ .node circle,#chatgpt-mermaid-\_r_23c\_ .node ellipse,#chatgpt-mermaid-\_r_23c\_ .node polygon,#chatgpt-mermaid-\_r_23c\_ .node path{fill:rgb(229, 243, 255);stroke:rgba(0, 0, 0, 0.1);stroke-width:1px;}#chatgpt-mermaid-\_r_23c\_ .node rect{rx:16px;ry:16px;}#chatgpt-mermaid-\_r_23c\_ .mermaid-decision .label-container{fill:rgb(245, 250, 255);stroke:rgb(206, 219, 229);stroke-dasharray:2,2;}#chatgpt-mermaid-\_r_23c\_ .edgePaths .flowchart-link{stroke:rgb(143, 143, 143);stroke-width:1px;stroke-linecap:round;stroke-linejoin:round;}#chatgpt-mermaid-\_r_23c\_ .marker{fill:rgb(143, 143, 143);stroke:rgb(143, 143, 143);}#chatgpt-mermaid-\_r_23c\_ :root{--mermaid-font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";}Terraform Configuration (.tf)Terraform CoreProvider PluginsAWSAzureGoogle CloudTerraform State

## 3. Installing Terraform

Terraform is available for Linux, Windows, and macOS.

### Installation on Ubuntu/Linux

The following example installs Terraform using HashiCorp's official APT repository.

```
sudo apt-get update
sudo apt-get install -y gnupg software-properties-common wget

wget -O- https://apt.releases.hashicorp.com/gpg | \
  gpg --dearmor | \
  sudo tee /usr/share/keyrings/hashicorp-archive-keyring.gpg > /dev/null

echo "deb [signed-by=/usr/share/keyrings/hashicorp-archive-keyring.gpg] https://apt.releases.hashicorp.com $(lsb_release -cs) main" | \
  sudo tee /etc/apt/sources.list.d/hashicorp.list

sudo apt-get update
sudo apt-get install terraform
```

Verify the installation:

```
terraform version
```

## 4. Terraform Configuration Basics

Terraform uses `.tf` files written in HashiCorp Configuration Language (HCL).

Before creating infrastructure, understand these basic configuration elements.

### A. Blocks

Blocks define components such as providers, resources, variables, and outputs.

```
resource "aws_s3_bucket" "example" {
  bucket = "my-unique-terraform-demo-bucket"
}
```

### B. Arguments

Arguments assign values inside blocks.

```
instance_type = "t3.micro"
```

### C. Identifiers

Identifiers give names to Terraform resources.

In `aws_instance.web`, `aws_instance` is the resource type and `web` is its local name.

### D. Comments

Terraform supports comments for explaining configurations.

```
# This creates an EC2 instance
resource "aws_instance" "web" {
  ami           = var.ami_id
  instance_type = "t3.micro"
}
```

## 5. Providers and Resource Blocks

### A. Provider Block

The provider block configures the platform Terraform will manage.

Example (`providers.tf`):

```
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 6.0"
    }
  }
}

provider "aws" {
  region = "ap-south-1"
}
```

### B. Resource Block

The resource block defines what Terraform should create.

Example (`main.tf`):

```
resource "aws_instance" "web_server" {
  ami           = var.ami_id
  instance_type = "t3.micro"

  tags = {
    Name = "Terraform-Web-Server"
  }
}
```

Here:

- `aws_instance` is the resource type.
- `web_server` is the resource name within Terraform.
- `ami` identifies the machine image.
- `instance_type` specifies the EC2 instance size.
- `tags` assigns metadata to the resource.

The AMI variable must contain a valid AMI ID for the selected AWS region.

## 6. Terraform Execution Phases

Terraform follows four main execution phases.

Step 1

Init

Step 2

Plan

Step 3

Apply

Step 4

Destroy

Initialize → Preview → Create or Update → Remove

### A. Initialization

Downloads the required provider plugins and prepares the working directory.

```
terraform init
```

### B. Planning

Displays the changes Terraform intends to make without applying them.

```
terraform plan
```

### C. Apply

Creates, modifies, or deletes resources to match the desired configuration.

```
terraform apply
```

### D. Destroy

Removes the infrastructure managed by the current Terraform configuration.

```
terraform destroy
```

Additional useful commands:

```
terraform validate   # Check configuration validity
terraform fmt        # Format Terraform files
terraform show       # Display state or a saved plan
terraform output     # Display output values
```

## 7. Putting It Together: A Basic Terraform Project

Create a project with the following structure:

```
terraform-project/
├── providers.tf
├── main.tf
├── variables.tf
├── terraform.tfvars
└── outputs.tf
```

### A. providers.tf

```
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 6.0"
    }
  }
}

provider "aws" {
  region = var.aws_region
}
```

### B. main.tf

```
resource "aws_instance" "web" {
  ami           = var.ami_id
  instance_type = var.instance_type

  tags = {
    Name = "Terraform-Demo"
  }
}
```

### C. variables.tf

```
variable "aws_region" {
  type    = string
  default = "ap-south-1"
}

variable "ami_id" {
  type = string
}

variable "instance_type" {
  type    = string
  default = "t3.micro"
}
```

### D. terraform.tfvars

```
ami_id        = "ami-xxxxxxxx"
instance_type = "t3.micro"
```

Replace `ami-xxxxxxxx` with a valid AMI ID.

### E. outputs.tf

```
output "instance_id" {
  value = aws_instance.web.id
}

output "public_ip" {
  value = aws_instance.web.public_ip
}
```

### Execute the Project

```
terraform init
terraform validate
terraform plan
terraform apply
terraform output
```

AWS credentials and appropriate permissions must be configured. AWS resources may incur charges.

## 8. Terraform Version Constraints

Version constraints specify which Terraform or provider versions can be used.

```
terraform {
  required_version = ">= 1.5.0"

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 6.0"
    }
  }
}
```

Common version operators:

| Operator   | Meaning                          |
| ---------- | -------------------------------- |
| `= 1.5.0`  | Exactly version 1.5.0            |
| `>= 1.5.0` | Version 1.5.0 or higher          |
| `< 2.0.0`  | Any version below 2.0.0          |
| `~> 6.0`   | Compatible 6.x provider versions |

## 9. Terraform Variables

Variables make Terraform configurations reusable and flexible.

### Input Variables

```
variable "environment" {
  type    = string
  default = "development"
}
```

### Using Variables

```
resource "aws_instance" "web" {
  ami           = var.ami_id
  instance_type = var.instance_type

  tags = {
    Environment = var.environment
  }
}
```

### Variable Types

| Type    | Example                   |
| ------- | ------------------------- |
| String  | `"ap-south-1"`            |
| Number  | `3`                       |
| Boolean | `true`                    |
| List    | `["dev", "test", "prod"]` |
| Map     | `{ dev = "t3.micro" }`    |

Variables can be supplied through default values, `.tfvars` files, environment variables, or command-line arguments.

## 10. Terraform State

Terraform state is an important component that records the relationship between configuration resources and real infrastructure.

By default, Terraform stores state locally in:

```
terraform.tfstate
```

Why is Terraform State important?

1. Tracks resources created through Terraform.
2. Helps Terraform identify required changes.
3. Maintains resource IDs and attributes.
4. Supports updates and deletion of managed infrastructure.

### Remote State Storage

For team collaboration, Terraform state can be stored remotely using services such as AWS S3, Azure Storage, Google Cloud Storage, and HCP Terraform.

Example S3 backend:

```
terraform {
  backend "s3" {
    bucket       = "my-terraform-state-bucket"
    key          = "development/terraform.tfstate"
    region       = "ap-south-1"
    use_lockfile = true
    encrypt      = true
  }
}
```

The S3 bucket must already exist and the Terraform identity must have appropriate permissions.

### State Locking

State locking prevents conflicting operations from modifying the same state simultaneously.

For example, when one team member runs `terraform apply`, another operation requiring the same state lock must wait or fail until the lock is released.

## 11. Terraform Meta-Arguments

Meta-arguments control how Terraform creates and manages resources.

### A. count

Creates multiple instances of a resource.

```
resource "aws_instance" "web" {
  count         = 3
  ami           = var.ami_id
  instance_type = "t3.micro"
}
```

This defines three EC2 instances.

### B. for_each

Creates resources from a map or set.

```
resource "aws_instance" "web" {
  for_each = toset(["dev", "test", "prod"])

  ami           = var.ami_id
  instance_type = "t3.micro"

  tags = {
    Name = each.key
  }
}
```

### C. depends_on

Creates an explicit dependency between resources when necessary.

```
resource "aws_instance" "web" {
  ami           = var.ami_id
  instance_type = "t3.micro"

  depends_on = [aws_security_group.web_sg]
}
```

This example assumes `aws_security_group.web_sg` has been defined elsewhere.

### D. lifecycle

Controls certain resource management behaviors.

```
lifecycle {
  create_before_destroy = true
}
```

This lifecycle setting can be used inside a resource block to request replacement creation before destruction, where supported.

## 12. Terraform Provisioners

Provisioners allow Terraform to execute commands or transfer files during resource creation or destruction.

### A. local-exec

Runs a command on the machine executing Terraform.

```
resource "terraform_data" "example" {
  provisioner "local-exec" {
    command = "echo Terraform execution completed"
  }
}
```

### B. file

Copies a file to a remote machine.

```
provisioner "file" {
  source      = "app.conf"
  destination = "/tmp/app.conf"
}
```

### C. remote-exec

Executes commands on a remote machine.

```
provisioner "remote-exec" {
  inline = [
    "sudo apt-get update",
    "sudo apt-get install -y nginx"
  ]
}
```

The `file` and `remote-exec` examples are provisioner fragments. They require a supporting resource and remote connection configuration.

> Provisioners should generally be a last resort. For instance configuration, prefer cloud-init, user data, or dedicated configuration management tools where appropriate.

## 13. Terraform Data Sources

Data sources allow Terraform to retrieve information about existing infrastructure without creating those resources.

For example, instead of hardcoding an AWS AMI ID, Terraform can retrieve an available image.

```
data "aws_ami" "ubuntu" {
  most_recent = true
  owners      = ["099720109477"]

  filter {
    name   = "name"
    values = ["ubuntu/images/hvm-ssd-gp3/ubuntu-noble-24.04-amd64-server-*"]
  }
}
```

Using the data source:

```
resource "aws_instance" "web" {
  ami           = data.aws_ami.ubuntu.id
  instance_type = "t3.micro"
}
```

Data sources help avoid hardcoded resource IDs and improve configuration reusability. For predictable production deployments, pin or validate the selected image rather than automatically adopting an unexpected new image.

## 14. Interpolation, Conditional Expressions, Functions, and Loops

### A. Interpolation

Interpolation inserts dynamic values into strings.

```
tags = {
  Name = "Server-${var.environment}"
}
```

### B. Conditional Expressions

Select a value based on a condition.

```
instance_type = var.is_dev ? "t3.micro" : "t3.large"
```

### C. Built-in Functions

Terraform provides functions for working with strings, lists, maps, and numbers.

```
locals {
  servers = ["web", "app", "db"]

  total_servers = length(local.servers)
  server_names  = join(",", local.servers)
}
```

### D. for Expressions

Transform a collection into another collection.

```
locals {
  environments = ["dev", "test", "prod"]

  upper_names = [
    for env in local.environments : upper(env)
  ]
}
```

### E. for_each

Create multiple resources with distinct names.

```
resource "aws_s3_bucket" "buckets" {
  for_each = toset([
    "my-unique-dev-bucket",
    "my-unique-test-bucket"
  ])

  bucket = each.key
}
```

S3 bucket names must be globally unique.

## 15. Terraform Modules

Modules allow you to organize and reuse Terraform configurations.

A module can contain resources, variables, outputs, and other Terraform configuration elements.

### Example Project Structure

```
terraform-project/
├── main.tf
├── variables.tf
└── modules/
    └── ec2/
        ├── main.tf
        ├── variables.tf
        └── outputs.tf
```

### Create a Module

`modules/ec2/main.tf`

```
resource "aws_instance" "server" {
  ami           = var.ami_id
  instance_type = var.instance_type
}
```

`modules/ec2/variables.tf`

```
variable "ami_id" {
  type = string
}

variable "instance_type" {
  type = string
}
```

### Call the Module

Root `main.tf`:

```
module "web_server" {
  source = "./modules/ec2"

  ami_id        = var.ami_id
  instance_type = "t3.micro"
}
```

Why use Terraform Modules?

1. Reuse configurations across projects.
2. Reduce code duplication.
3. Standardize infrastructure deployments.
4. Simplify complex configurations.
5. Manage development, testing, and production environments consistently.

## 16. Hands-On Practice

Complete the following exercises to strengthen your understanding of Terraform.

| Exercise | Task                                          |
| -------- | --------------------------------------------- |
| 1        | Install Terraform and verify its version      |
| 2        | Configure the AWS provider                    |
| 3        | Create a basic EC2 instance                   |
| 4        | Use variables for region and instance type    |
| 5        | Execute `terraform init`, `plan`, and `apply` |
| 6        | Retrieve an AMI using a data source           |
| 7        | Create multiple resources using `count`       |
| 8        | Create resources using `for_each`             |
| 9        | Organize an EC2 configuration into a module   |
| 10       | Destroy lab resources using Terraform         |

### Learning Outcomes

By the end of this lesson, students will be able to understand Terraform architecture, write HCL configurations, use providers and resources, manage variables and state, work with provisioners and data sources, apply loops and conditional expressions, and organize infrastructure using reusable modules.

Key takeaway: Terraform allows infrastructure to be defined, created, updated, and managed through code, making deployments more consistent, repeatable, and easier to maintain.
