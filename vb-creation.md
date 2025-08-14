# Pre-built Vagrant Box - Docker + Ansible Ready

This approach uses an existing Debian box and customizes it. Works every time, takes 5 minutes.

## Quick Setup

```bash
# 1. Create project directory
mkdir vagrant-custom-box
cd vagrant-custom-box

# 2. Download base Debian box
vagrant box add debian/bookworm64 --provider virtualbox

# 3. Initialize and customize
vagrant init debian/bookworm64
```

## Custom Vagrantfile

Replace the generated `Vagrantfile` with this:

```ruby
Vagrant.configure("2") do |config|
  config.vm.box = "debian/bookworm64"
  
  # Allocate enough resources for Docker
  config.vm.provider "virtualbox" do |vb|
    vb.memory = "1024"
    vb.cpus = 2
  end
  
  # Install Docker and Ansible
  config.vm.provision "shell", inline: <<-SHELL
    set -e
    export DEBIAN_FRONTEND=noninteractive
    
    echo "=== Updating system ==="
    apt-get update
    apt-get upgrade -y
    
    echo "=== Installing essential packages ==="
    apt-get install -y \\
      curl \\
      wget \\
      git \\
      vim \\
      htop \\
      unzip \\
      build-essential \\
      software-properties-common \\
      apt-transport-https \\
      ca-certificates \\
      gnupg \\
      lsb-release \\
      python3-pip \\
      python3-venv \\
      python3-dev
    
    echo "=== Installing Docker ==="
    # Remove old docker packages
    for pkg in docker.io docker-doc docker-compose podman-docker containerd runc; do 
        apt-get remove $pkg -y 2>/dev/null || true
    done
    
    # Add Docker's official GPG key
    install -m 0755 -d /etc/apt/keyrings
    curl -fsSL https://download.docker.com/linux/debian/gpg | gpg --dearmor -o /etc/apt/keyrings/docker.gpg
    chmod a+r /etc/apt/keyrings/docker.gpg
    
    # Add Docker repository
    echo "deb [arch="$(dpkg --print-architecture)" signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/debian "$(. /etc/os-release && echo "$VERSION_CODENAME")" stable" | tee /etc/apt/sources.list.d/docker.list > /dev/null
    
    # Install Docker
    apt-get update
    apt-get install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
    
    # Add vagrant user to docker group
    usermod -aG docker vagrant
    
    # Enable Docker service
    systemctl enable docker
    systemctl start docker
    
    # Install docker-compose standalone
    COMPOSE_VERSION="v2.21.0"
    curl -L "https://github.com/docker/compose/releases/download/${COMPOSE_VERSION}/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
    chmod +x /usr/local/bin/docker-compose
    
    echo "=== Installing Ansible ==="
    # Install Ansible via pip
    pip3 install ansible
    
    # Install collections as vagrant user
    sudo -u vagrant ansible-galaxy collection install community.docker
    sudo -u vagrant ansible-galaxy collection install community.general
    sudo -u vagrant ansible-galaxy collection install ansible.posix
    
    echo "=== Cleaning up ==="
    apt-get autoremove -y
    apt-get autoclean
    apt-get clean
    
    echo "=== Installation Summary ==="
    docker --version
    docker compose version
    ansible --version
    
    echo "=== Setup completed successfully! ==="
  SHELL
end
```

## Build Your Custom Box

```bash
# 4. Start VM and run provisioning
vagrant up

# This will:
# - Download Debian 12 base box (~300MB)
# - Boot the VM
# - Install Docker + Ansible
# - Takes about 5-8 minutes total

# 5. Test everything works
vagrant ssh -c "docker --version && ansible --version"

# You should see:
# Docker version 24.0.x
# ansible [core 2.15.x]

# 6. Package your custom box
vagrant package --output debian-docker-ansible.box

# 7. Add to your local boxes
vagrant box add --name "student-dev-box" debian-docker-ansible.box --force

# 8. Clean up the temp VM
vagrant destroy
```

## Test Your Custom Box

```bash
# Create a test directory
mkdir test-custom-box
cd test-custom-box

# Initialize with your custom box
vagrant init student-dev-box

# Start and test
vagrant up
vagrant ssh

# Inside the VM, test everything:
docker run hello-world
ansible --version
docker compose version
```

## Upload to Vagrant Cloud (Optional)

```bash
# 1. Create account at https://app.vagrantup.com
# 2. Create new box (e.g., yourname/debian-dev)
# 3. Upload your .box file
# 4. Students can then use:

# In student instructions:
vagrant box add yourname/debian-dev
vagrant init yourname/debian-dev
vagrant up
```

## What Students Get

**Box Contents:**
- Debian 12 (bookworm) - stable and lightweight
- Docker CE with docker-compose plugin
- Docker Compose standalone binary  
- Ansible with common collections
- Essential development tools (git, vim, curl, etc.)
- Pre-configured vagrant user with docker permissions

**Box Specs:**
- Size: ~500-600MB (reasonable for features included)
- RAM: 1GB allocated (adjustable)
- Boot time: 15-20 seconds
- All services ready to use

## Student Vagrantfile Template

Give your students this simple `Vagrantfile`:

```ruby
Vagrant.configure("2") do |config|
  config.vm.box = "yourname/debian-dev"
  
  # Optional: customize resources
  config.vm.provider "virtualbox" do |vb|
    vb.memory = "2048"  # 2GB RAM
    vb.cpus = 2
  end
  
  # Optional: port forwarding for web apps
  config.vm.network "forwarded_port", guest: 80, host: 8080
  config.vm.network "forwarded_port", guest: 3000, host: 3000
  
  # Optional: shared folder for projects
  config.vm.synced_folder "./projects", "/home/vagrant/projects"
end
```

## Expected Timeline

- **Download base box**: 2-3 minutes (one time)
- **VM boot + provisioning**: 5-8 minutes
- **Package custom box**: 1-2 minutes
- **Upload to Vagrant Cloud**: 3-5 minutes (optional)

**Total**: 10-15 minutes vs hours of debugging Packer!

This approach gives you a production-ready box that your students can use immediately for Docker and Ansible practice.
