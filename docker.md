# 🐳 Complete Docker Beginner-to-Advanced Guide

> **Welcome to Docker!** This guide is designed to take you from zero to confident practitioner. Every concept is broken down with real-world analogies, flag explanations, step-by-step labs, and production-ready examples.

---

## 📌 Table of Contents
1. [💡 Core Concepts & Architecture](#-1-core-concepts--architecture)
2. [🔰 Phase 1: Essential Docker Commands](#-phase-1-essential-docker-commands)
3. [💾 Phase 2: Storage & Volumes (Hands-on Lab)](#-phase-2-storage--volumes-hands-on-lab)
4. [🌐 Phase 3: Docker Networking & Port Mapping](#-phase-3-docker-networking--port-mapping)
5. [🏗️ Phase 4: Dockerfile & Building Custom Images](#-phase-4-dockerfile--building-custom-images)
6. [🎼 Phase 5: Multi-Container Apps with Docker Compose](#-phase-5-multi-container-apps-with-docker-compose)
7. [🧪 Phase 6: Troubleshooting, Monitoring & Cleanup](#-phase-6-troubleshooting-monitoring--cleanup)
8. [📋 Quick Command Reference Table](#-quick-command-reference-table)

---

## 💡 1. Core Concepts & Architecture

### 🧠 What is a Container vs. Virtual Machine?

| Feature | Virtual Machine (VM) | Docker Container |
| :--- | :--- | :--- |
| **Architecture** | Includes full Guest OS + Hypervisor | Shares Host OS Kernel |
| **Startup Time** | Minutes | Milliseconds to seconds |
| **Resource Usage**| High (GBs of RAM & Disk per VM) | Ultra-lightweight (MBs) |
| **Portability** | Heavy image export | Works identically anywhere Docker runs |

```
  Virtual Machines (Heavy)            Docker Containers (Lightweight)
┌───────────────────────────────┐   ┌───────────────────────────────┐
│ App 1   │ App 2   │ App 3     │   │ App 1   │ App 2   │ App 3     │
├─────────┼─────────┼───────────┤   ├─────────┼─────────┼───────────┤
│ Guest OS│ Guest OS│ Guest OS  │   │ Bins/Libs│Bins/Libs│Bins/Libs │
├─────────┴─────────┴───────────┤   ├───────────────────────────────┤
│          Hypervisor           │   │         Docker Engine         │
├───────────────────────────────┤   ├───────────────────────────────┤
│            Host OS            │   │            Host OS            │
├───────────────────────────────┤   ├───────────────────────────────┤
│      Physical Hardware        │   │      Physical Hardware        │
└───────────────────────────────┘   └───────────────────────────────┘
```

---

### 🧩 The Four Pillars of Docker

1. **Dockerfile:** The text recipe / blueprint containing step-by-step instructions to create an image.
2. **Image:** The read-only package containing code, runtime, libraries, environment variables, and config files.
3. **Container:** A running, isolated instance created from an Image.
4. **Registry (e.g., Docker Hub):** A cloud storage repository to push and pull images.

---

## 🔰 Phase 1: Essential Docker Commands

### 1️⃣ System Information

```bash
docker --version          # Displays the installed Docker client version
docker info               # Shows system-wide details (containers count, OS, storage driver)
docker stats              # Displays live CPU, Memory, Network, and Disk I/O stream
```

---

### 2️⃣ Working with Images

An image is like a class in programming; a container is an object instantiated from it.

```bash
# 1. Download an image from Docker Hub:
docker pull nginx:latest

# 2. List all downloaded images stored on your machine:
docker images

# 3. View the layer history of an image:
docker history nginx:latest

# 4. Remove an image by name or ID:
docker rmi nginx:latest
```

---

### 3️⃣ Running & Managing Containers

#### 🔍 Anatomy of `docker run`
When you execute `docker run`, you can pass several helpful flags:
- `-d` (*Detached mode*): Runs container in the background so your terminal stays free.
- `--name <name>`: Gives your container a friendly custom name instead of a random generated one.
- `-p <host_port>:<container_port>`: Forwards traffic from your machine's port to the container.
- `-e KEY=value`: Passes an environment variable inside the container.
- `-it`: Opens an interactive terminal session inside the container.
- `--rm`: Automatically removes the container when it stops (great for one-off tasks).

#### 💻 Practical Examples:

```bash
# Example A: Run an NGINX web server in background with custom name and port 8080:
docker run -d --name my-web -p 8080:80 nginx

# Example B: Run an interactive lightweight Ubuntu shell and remove it on exit:
docker run -it --rm ubuntu bash

# Example C: Run a container with an environment variable:
docker run -d --name app-env -e "APP_ENV=production" -e "PORT=3000" node:18-alpine
```

---

### 4️⃣ Viewing & Controlling Container Lifecycle

```bash
# List only running containers:
docker ps

# List ALL containers (both running and stopped):
docker ps -a

# View container processes (like 'top' in Linux):
docker top my-web

# Stop a running container gracefully:
docker stop my-web

# Start a previously stopped container:
docker start my-web

# Restart a container:
docker restart my-web

# Remove a stopped container:
docker rm my-web

# Force stop and remove a running container in one step:
docker rm -f my-web
```

> 💡 **DevOps Tip: Bulk Container Cleanup**
> ```bash
> # Stop all running containers:
> docker stop $(docker ps -q)
> 
> # Remove all stopped containers:
> docker rm $(docker ps -aq)
> ```

---

### 5️⃣ Inspecting Logs & Executing Shells in Running Containers

```bash
# 1. View logs from a container:
docker logs my-web

# 2. Follow logs in real-time (like tail -f):
docker logs -f my-web

# 3. Execute a bash terminal inside a running container:
docker exec -it my-web bash

# 4. For lightweight Alpine images (which do not have bash, use 'sh'):
docker exec -it my-web sh
```

---

## 💾 Phase 2: Storage & Volumes (Hands-on Lab)

### ❓ Why do we need Volumes?
Containers are **ephemeral** (temporary). If a database container crashes or is deleted, all the database files stored inside the container will disappear!

A **Docker Volume** mounts a folder from the host machine directly into the container, ensuring your data survives even if the container is destroyed.

```
┌──────────────────────────────────────┐
│ Host Machine Directory               │
│ /opt/data                            │
└───────────────────▲──────────────────┘
                    │  Mounted via -v
┌───────────────────▼──────────────────┐
│ MySQL Container                      │
│ /var/lib/mysql                       │
└──────────────────────────────────────┘
```

---

### 🧪 Hands-On Lab: MySQL Database Persistence

Let's create a database, save records, delete the container, and verify data persists in a new container!

#### Step 1: Create a host directory for storage
```bash
sudo mkdir -p /opt/data
sudo chmod 777 /opt/data
cd /opt/data
```

#### Step 2: Run first MySQL container (`mysql1`) with host volume mounted
```bash
docker run -d \
  --name mysql1 \
  -p 3306:3306 \
  -v /opt/data:/var/lib/mysql \
  -e MYSQL_ROOT_PASSWORD=db_pass123 \
  mysql:8.0
```

#### Step 3: Connect and create a database with sample records
```bash
# Open interactive MySQL CLI inside container:
docker exec -it mysql1 mysql -u root -pdb_pass123

# Inside MySQL prompt, run:
CREATE DATABASE school;
USE school;
CREATE TABLE students (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(50), country VARCHAR(50));
INSERT INTO students (name, country) VALUES ("Sanjay", "India"), ("Alex", "Singapore");
SELECT * FROM students;
EXIT;
```

#### Step 4: Stop and delete the container (`mysql1`)
```bash
docker stop mysql1
docker rm mysql1
```

#### Step 5: Launch a brand new container (`mysql2`) attached to the SAME `/opt/data` volume
```bash
docker run -d \
  --name mysql2 \
  -p 3307:3306 \
  -v /opt/data:/var/lib/mysql \
  -e MYSQL_ROOT_PASSWORD=db_pass123 \
  mysql:8.0
```

#### Step 6: Verify all data is intact!
```bash
docker exec -it mysql2 mysql -u root -pdb_pass123 -e "USE school; SELECT * FROM students;"
```
*Result:* All rows are completely preserved! 🎉

---

### ⚠️ Common Gotcha: MySQL Socket Connection Error
If you run `docker exec` immediately after `docker run`, you might see:
```text
ERROR 2002 (HY000): Can't connect to local MySQL server through socket '/var/run/mysqld/mysqld.sock'
```
**Why it happens:** MySQL takes 10–15 seconds to initialize its database engine on first boot.  
**Fix:** Wait 10 seconds or check `docker logs mysql1` until you see `ready for connections`.

---

## 🌐 Phase 3: Docker Networking & Port Mapping

### 1️⃣ Port Mapping Demystified (`-p Host:Container`)

```bash
docker run -d -p 8080:80 --name web-server nginx
```
- `8080` is the **Host Port** (the port you open in your browser: `http://localhost:8080`).
- `80` is the **Container Port** (the internal port NGINX listens on inside its isolated space).

```
   User Browser Request ────► http://localhost:8080
                                      │
                                      ▼
                               Host Port: 8080
                                      │ (Forwarded by Docker)
                                      ▼
                            Container Port: 80 (NGINX)
```

---

### 2️⃣ Network Drivers & Commands

Docker comes with built-in network drivers:
- **`bridge` (default):** Isolated private network on the host. Containers can communicate using IP addresses or user-defined network names.
- **`host`:** Removes network isolation between the container and Docker host.
- **`none`:** Disables all networking for complete isolation.

```bash
# 1. List all Docker networks:
docker network ls

# 2. Create a custom bridge network:
docker network create my-app-net

# 3. Run two containers on the same network (they can communicate by container name!):
docker run -d --name database --network my-app-net -e MYSQL_ROOT_PASSWORD=root mysql:8.0
docker run -d --name backend --network my-app-net -p 5000:5000 my-backend-image

# 4. Inspect a network to see connected container IPs:
docker network inspect my-app-net
```

---

## 🏗️ Phase 4: Dockerfile & Building Custom Images

### 1️⃣ Essential Dockerfile Instructions

| Instruction | Purpose | Example |
| :--- | :--- | :--- |
| `FROM` | Sets the base image | `FROM python:3.9-slim` |
| `WORKDIR` | Sets current working directory inside container | `WORKDIR /app` |
| `COPY` | Copies files from host machine into container | `COPY . .` |
| `RUN` | Executes build commands during image creation | `RUN pip install -r requirements.txt` |
| `ENV` | Sets environment variables | `ENV PORT=8080` |
| `EXPOSE` | Documents the port intended to be published | `EXPOSE 8080` |
| `USER` | Switches user for security (avoid root!) | `USER appuser` |
| `CMD` | Default command executed when container starts | `CMD ["python", "app.py"]` |

---

### 2️⃣ Production-Ready Python Application Example

#### Project Files:
```text
my-python-app/
├── Dockerfile
├── requirements.txt
└── app.py
```

#### `app.py`:
```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from a Dockerized Flask Application!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

#### `requirements.txt`:
```text
flask==2.3.2
```

#### `Dockerfile` (Production Best Practices):
```dockerfile
# 1. Use a lightweight official base image
FROM python:3.9-slim

# 2. Security: Create a non-root user
RUN useradd -m appuser && mkdir /app && chown appuser:appuser /app
USER appuser

# 3. Set working directory
WORKDIR /app

# 4. Optimize Docker layer caching: Copy dependencies first
COPY --chown=appuser requirements.txt .
RUN pip install --no-cache-dir --user -r requirements.txt

# 5. Copy the rest of the application code
COPY --chown=appuser . .

# 6. Expose port and define runtime command
EXPOSE 5000
CMD ["python", "app.py"]
```

#### Build and Run:
```bash
# Build the image with tag 'my-flask-app:1.0':
docker build -t my-flask-app:1.0 .

# Run the container:
docker run -d --name flask-server -p 5000:5000 my-flask-app:1.0

# Test it:
curl http://localhost:5000
```

---

### 3️⃣ Multi-Stage Builds (Optimized Image Size)

Multi-stage builds allow you to use heavy tools (compilers, npm, maven) in a build stage, and copy **only the final built artifacts** into a tiny runtime image.

```dockerfile
# Stage 1: Build the React / Node app
FROM node:18-alpine AS builder
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build

# Stage 2: Serve with lightweight NGINX
FROM nginx:alpine
COPY --from=builder /app/dist /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
```
> 🚀 **Result:** Image size drops from **~1 GB** to **~25 MB**!

---

## 🎼 Phase 5: Multi-Container Apps with Docker Compose

### ❓ What is Docker Compose?
Instead of running 5 separate `docker run` commands with complex networks and volumes, **Docker Compose** lets you define your entire multi-service stack in a single `docker-compose.yml` file.

---

### 🌟 Full Production Example: WordPress + MariaDB + phpMyAdmin

Create `docker-compose.yml`:
```yaml
version: '3.8'

services:
  # Database Service
  db:
    image: mariadb:10.6
    container_name: wp_mariadb
    restart: unless-stopped
    environment:
      MYSQL_ROOT_PASSWORD: secret_root_pass
      MYSQL_DATABASE: wordpress_db
      MYSQL_USER: wp_user
      MYSQL_PASSWORD: wp_user_pass
    volumes:
      - db_data:/var/lib/mysql
    networks:
      - wp_network
    healthcheck:
      test: ["CMD", "mysqladmin", "ping", "-h", "localhost"]
      interval: 10s
      timeout: 5s
      retries: 5

  # WordPress Web Application
  wordpress:
    image: wordpress:latest
    container_name: wp_app
    restart: unless-stopped
    depends_on:
      db:
        condition: service_healthy
    environment:
      WORDPRESS_DB_HOST: db:3306
      WORDPRESS_DB_USER: wp_user
      WORDPRESS_DB_PASSWORD: wp_user_pass
      WORDPRESS_DB_NAME: wordpress_db
    volumes:
      - wp_data:/var/www/html
    ports:
      - "80:80"
    networks:
      - wp_network

  # Database Admin UI (phpMyAdmin)
  phpmyadmin:
    image: phpmyadmin:latest
    container_name: wp_phpmyadmin
    restart: unless-stopped
    depends_on:
      - db
    environment:
      PMA_HOST: db
      PMA_PORT: 3306
    ports:
      - "8080:80"
    networks:
      - wp_network

# Persistent Volumes
volumes:
  db_data:
  wp_data:

# Custom Network for Inter-Service Communication
networks:
  wp_network:
    driver: bridge
```

---

### 🎮 Docker Compose Commands:

```bash
# 1. Start all services in the background:
docker compose up -d

# 2. Check running services:
docker compose ps

# 3. View live logs from all services:
docker compose logs -f

# 4. View logs for a specific service:
docker compose logs -f wordpress

# 5. Stop and remove all containers, networks:
docker compose down

# 6. Stop and delete everything INCLUDING volumes:
docker compose down -v
```

🌐 **Access points:**
- WordPress: `http://localhost:80`
- phpMyAdmin: `http://localhost:8080`

---

## 🧪 Phase 6: Troubleshooting, Monitoring & Cleanup

### 1️⃣ Debugging Containers
```bash
# 1. View detailed JSON inspection of container config, IP address, state:
docker inspect my-web

# 2. Extract only the IP address of a container:
docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' my-web

# 3. Copy files between container and host machine:
docker cp my-web:/var/log/nginx/error.log ./local_error.log     # Container to Host
docker cp ./index.html my-web:/usr/share/nginx/html/index.html # Host to Container

# 4. View file changes inside container compared to base image:
docker diff my-web
```

---

### 2️⃣ Resource Limits & Management
```bash
# Limit container to 512MB RAM and 1 CPU core:
docker run -d --name constrained-app --memory="512m" --cpus="1.0" nginx

# Dynamically update resources of a running container:
docker update --memory="1g" --cpus="2.0" constrained-app
```

---

### 3️⃣ System Cleanup & Freeing Disk Space
```bash
# Safe cleanup: Removes stopped containers, unused networks, and dangling images:
docker system prune

# Deep cleanup: Removes ALL unused images, stopped containers, and volumes:
docker system prune -a --volumes
```

---

## 📋 Quick Command Reference Table

| Task | Command |
| :--- | :--- |
| **Download Image** | `docker pull <image>` |
| **List Images** | `docker images` |
| **Run Container** | `docker run -d --name <name> -p <host>:<container> <image>` |
| **List Running Containers** | `docker ps` |
| **List All Containers** | `docker ps -a` |
| **Stop Container** | `docker stop <name/id>` |
| **Start Container** | `docker start <name/id>` |
| **Remove Container** | `docker rm <name/id>` |
| **Remove Image** | `docker rmi <image>` |
| **Container Shell** | `docker exec -it <name> bash` *(or `sh`)* |
| **View Live Logs** | `docker logs -f <name>` |
| **Live Stats** | `docker stats` |
| **Build Image** | `docker build -t <name:tag> .` |
| **Start Compose Stack** | `docker compose up -d` |
| **Stop Compose Stack** | `docker compose down` |
| **Complete Cleanup** | `docker system prune -a --volumes` |

---
