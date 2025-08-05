

## 🐳 **Basic Docker Commands**

### 🔹 General Info
```bash
docker --version          # Show Docker version
docker info               # Display system-wide information
docker stats              # Live container resource usage
```

### 🔹 Working with Images
```bash
docker pull <image_name>:<tag>      # Pull specific version (default: latest)
docker images                       # List all images
docker rmi <image_id|image_name>    # Remove image
docker image history <image_name>   # Show image layer history
```

### 🔹 Working with Containers
```bash
docker run busybox                      # Run container
docker run -it --rm busybox bash          # Run interactively + auto-remove
docker ps
docker ps -a --format "table {{.ID}}\t{{.Names}}\t{{.Status}}"  # Custom format
docker stop $(docker ps -aq)                   # Stop all containers
docker rm $(docker ps -aq)                     # Remove all containers
docker top <container_name>                    # View running processes
```

### 🔹 Working with Volumes - Try this steps only on Vagrant Ubunut Linux 
```bash
• cd /opt
• mkdir data
• cd data
• docker run -d -v /opt/data:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=db_pass123 -p 3307:3306 --name mysql2 mysql
• docker exec mysql2 mysql -pdb_pass123 -e 'show databases'
• docker exec mysql2 mysql -pdb_pass123 -e 'use mysql;show tables'
• docker exec mysql2 mysql -pdb_pass123 -e 'create database sat'
• docker exec mysql2 mysql -pdb_pass123 -e 'show databases'
• docker exec mysql2 mysql -pdb_pass123 -e 'use sat;show tables'
• docker exec mysql2 mysql -pdb_pass123 -e 'use sat;create table student (name VARCHAR(30),age TINYINT,country TEXT)'
• docker exec mysql2 mysql -pdb_pass123 -e 'use sat;describe student‘
• docker exec mysql2 mysql -pdb_pass123 -e 'use sat;insert into student(name,age,country) values ("satheya",44,"singapore")'
• docker exec mysql2 mysql -pdb_pass123 -e 'use sat;insert into student(name,age,country) values ("satheyakumaar",44,"india")'
• docker exec mysql2 mysql -pdb_pass123 -e 'use sat;select * from student'
• docker stop mysql2
• docker run -d -v /opt/data:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=db_pass123 -p 3308:3306 --name mysql3 mysql
• docker exec mysql3 mysql -pdb_pass123 -e 'use sat;select * from student'
```

```

• docker run -it ubuntu
• apt-get update
• apt-get install mysql-client
• mysql -u root -h 192.168.0.23 -pdb_pass123

```
---

## 🧰 **Intermediate Docker Commands**

### 🔸 Named Containers & Environment
```bash
docker run --name bbox -d busybox sleep 50
dockr exec bbox ls
docker run -d --name my_container -e "ENV_VAR=value" busybox
docker exec -it my_container bash
docker logs -f my_container                    # Follow logs in real-time
docker exec -it my_container sh                # For Alpine-based images
```

### 🔸 Port Mapping & Volumes
```bash
docker run nginx
docker run -i busybox
docker run -it busybox
docker run --name nginx1 -d -p 80:80 nginx
docker run -p 8080:80 -p 443:443 nginx  # Multiple ports
docker run -d -e MYSQL_ROOT_PASSWORD=db_pass123 -p 3306:3306 --name mysqlbox mysql
```

### 🔸 Build & Tagging
```bash
docker build -t my_image:1.0 -f Dockerfile.prod .  # Specify Dockerfile
docker tag old_image:tag new_image:tag        # Retag an image
```

### 🔸 Image Management
```bash
docker save -o image.tar my_image:1.0         # Export image
docker load -i image.tar                      # Import image
docker image inspect my_image                 # Detailed image info
```

---

## 🧠 **Advanced Docker Commands**

### 🔸 Networking Deep Dive
```bash
docker network inspect bridge                 # Inspect default network
docker run --network=none <image>             # No network access
docker run --dns 8.8.8.8 <image>             # Custom DNS
```

### 🔸 Docker Compose (Production-Ready)

### Make sure the following package has been installed already.

```
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose

sudo yum install docker
sudo systemctl start docker
sudo chmod 777 /var/run/docker.sock
```



```yaml
version: '3.8'

services:
  db:
    image: mariadb:10.6
    container_name: wordpress_db
    restart: unless-stopped
    environment:
      MYSQL_ROOT_PASSWORD: your_root_password
      MYSQL_DATABASE: wordpress
      MYSQL_USER: wordpress
      MYSQL_PASSWORD: wordpress_password
    volumes:
      - db_data:/var/lib/mysql
    networks:
      - wordpress_network
    healthcheck:
      test: ["CMD", "mysqladmin", "ping", "-h", "localhost"]
      interval: 10s
      timeout: 5s
      retries: 5

  wordpress:
    image: wordpress:latest
    container_name: wordpress_app
    restart: unless-stopped
    depends_on:
      db:
        condition: service_healthy
    environment:
      WORDPRESS_DB_HOST: db
      WORDPRESS_DB_USER: wordpress
      WORDPRESS_DB_PASSWORD: wordpress_password
      WORDPRESS_DB_NAME: wordpress
    volumes:
      - wordpress_data:/var/www/html
    ports:
      - "80:80"
    networks:
      - wordpress_network
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost/wp-admin/install.php"]
      interval: 30s
      timeout: 10s
      retries: 3

  phpmyadmin:
    image: phpmyadmin:latest
    container_name: wordpress_phpmyadmin
    restart: unless-stopped
    depends_on:
      - db
    environment:
      PMA_HOST: db
      PMA_PORT: 3306
      PMA_ARBITRARY: 1
    ports:
      - "8080:80"
    networks:
      - wordpress_network

volumes:
  db_data:
  wordpress_data:

networks:
  wordpress_network:
    driver: bridge
```

```bash
docker-compose -f docker-compose.prod.yml up --build -d

## Verification
http://localhost:80
```

### 🔸 Multi-Stage Builds (Optimized Images)
```Dockerfile
# Dockerfile
FROM node:16 as builder
WORKDIR /app
COPY . .
RUN npm install && npm run build

FROM nginx:alpine
COPY --from=builder /app/dist /usr/share/nginx/html
```

---

## 🧪 **Troubleshooting & Optimization**

### 🔹 Debugging
```bash
docker events                            # Real-time container events
docker diff <container_name>            # Changed files in container
docker cp <container>:<path> <host_path> # Copy files from container
```

### 🔹 Resource Management
```bash
docker run --memory=1g --cpus=2 <image> # Limit resources
docker update --memory=2g <container>   # Update running container
```

### 🔹 Cleanup Script
```bash
# Remove all unused objects (careful!)
docker system prune -a --volumes
```

---

## 🏗 **Sample Dockerfile (Best Practices)**
```Dockerfile
FROM python:3.9-slim

# Security: Run as non-root
RUN useradd -m appuser && mkdir /app && chown appuser:appuser /app
USER appuser

WORKDIR /app

# Layer optimization: Install dependencies first
COPY --chown=appuser requirements.txt .
RUN pip install --user -r requirements.txt

COPY --chown=appuser . .

# Healthcheck and metadata
HEALTHCHECK --interval=5m --timeout=3s CMD curl -f http://localhost/ || exit 1
LABEL maintainer="your@email.com"

CMD ["python", "app.py"]
```

