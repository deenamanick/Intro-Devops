
### 🔰 **Basic Container Management Scenarios**

1. **Scenario: Check what’s currently running on your Docker host.**
   
    ➤ *Goal:* List running containers for debugging.
   
    ➤ *Command:* `docker ps`
   

3. **Scenario: You want to clean up the environment. List all containers, even stopped ones.**
   
   ➤ *Command:* `docker ps -a`

5. **Scenario: Your web server container crashed. Restart it. Make sure web-server container should be running already**
   ➤ *Command:* `docker start web-server`
   
   *Example* - `docker run -d --name web-server -p 8080:80 nginx`

6. **Scenario: You need to stop a misbehaving container.**
   
   ➤ *Command:* `docker stop web-server`

7. **Scenario: The app container needs a fresh restart after config change.**
    
   ➤ *Command:* `docker restart app-container`

8. **Scenario: Remove unnecessary containers to free space.**

   ➤ *Command:* `docker rm old_container`

9. **Scenario: Your manager asks you to launch a new NGINX server.**
    
   ➤ *Command:* `docker run -d --name web nginx`

10. **Scenario: You need shell access to a container to check logs manually.**
    
   ➤ *Command:* `docker exec -it web bash`

11. **Scenario: Investigate container logs for a failed deployment.**
    
    ➤ *Command:* `docker logs web`

---

### 📦 **Image Management Scenarios**

12. **Scenario: You want to check if the required image is available locally.**
    
    ➤ *Command:* `docker images`

13. **Scenario: Clean up unused images to save disk space.**
    
    ➤ *Command:* `docker image prune -a`

14. **Scenario: Pull a Redis image for an upcoming project.**
    
    ➤ *Command:* `docker pull redis`

15. **Scenario: Build a new Docker image from a project folder.**
    
    ➤ *Command:* `docker build -t myapp:latest .`

16. **Scenario: Check what's inside a custom image.**
    
    ➤ *Command:* `docker inspect myapp:latest`

17. **Scenario: Compare two images for differences.**
    
    ➤ *Command:* `docker history <image_id>`

18. **Scenario: Search for a lightweight Apache image.**
    
    ➤ *Command:* `docker search httpd`

---

19. **Scenario: Deploy NGINX and expose it on port 8080.**
    
    ➤ *Command:* `docker run -d -p 8080:80 nginx`

21. **Scenario: Inspect how a container sees the network.**
    
    ➤ *Command:* `docker exec -it web ping mysql`

---

### 📁 **Dockerfile & Compose Scenarios**

36. **Scenario: Build an image using Dockerfile for a simple html app.**

```
FROM almalinux:8  
MAINTAINER deenamail2004@gmail.com

# Install necessary packages
RUN dnf install -y httpd zip unzip curl && \
    dnf clean all

# Set working directory
WORKDIR /var/www/html/

# Download and extract template
RUN curl -o football-card.zip -L "https://www.free-css.com/assets/files/free-css-templates/download/page36/football-card.zip" && \
    unzip football-card.zip && \
    cp -rvf football-card/* . && \
    rm -rf football-card football-card.zip

# Expose HTTP port
EXPOSE 80

# Start Apache in the foreground
CMD ["/usr/sbin/httpd", "-D", "FOREGROUND"]

```
  
➤ *Command:* `docker build -t web-site .`


38. **Scenario: Use Docker Compose to bring up a multi-container app.**

### **Running an Application Using Docker Compose (Simple Example)**  

Let’s say you have a **Python Flask app** that connects to a **Redis** database. Instead of running multiple `docker run` commands, you can use `docker-compose.yml` to define and manage both services together.  

---

## **Step 1: Project Structure**
```
my-flask-app/
├── app.py          # Flask application
├── requirements.txt
└── docker-compose.yml
```

### **1. `app.py` (Flask Application)**
```python
from flask import Flask
import redis

app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)

@app.route('/')
def hello():
    count = cache.incr('hits')
    return f"Hello! This page has been viewed {count} times."

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
```

### **2. `requirements.txt`**
```
flask
redis
```

---

## **Step 2: Create `docker-compose.yml`**
```yaml
version: '3.8'

services:
  web:
    build: .          # Builds from Dockerfile in current dir
    ports:
      - "5000:5000"   # Maps host:container port
    depends_on:
      - redis         # Ensures Redis starts first

  redis:
    image: "redis:alpine"  # Uses official Redis image
```

---

## **Step 3: Run the Application**
1. **Build and start services** (Flask + Redis):
   ```bash
   docker-compose up
   ```
   - Runs both services in the foreground (logs visible).  
   - Use `-d` to run in detached mode:  
     ```bash
     docker-compose up -d
     ```

2. **Check running services:**
   ```bash
   docker-compose ps
   ```
   Example output:
   ```
   Name                Command               State           Ports         
   ---------------------------------------------------------------------
   my-flask-app-web    python app.py         Up      0.0.0.0:5000->5000/tcp
   my-flask-app-redis  docker-entrypoint.sh  Up      6379/tcp
   ```

3. **Access the Flask app:**  
   Open `http://localhost:5000` in your browser.  
   Each refresh increments the Redis counter!

4. **Stop the services:**
   ```bash
   docker-compose down
   ```
   - Stops and removes containers, networks, and volumes (if any).

---

🚀 **Now try running your own multi-container app!** 🐳
    
    ➤ *Command:* `docker-compose up -d`

---

### 🔐 **Security and Resource Control Scenarios**

41. **Scenario: Limit memory usage of a container to 200MB.**
    ➤ *Command:* `docker run -d --memory=200m myapp`

42. **Scenario: Limit CPU usage of a container.**
    
    ➤ *Command:* `docker run -d --cpus=1 myapp`

---

### 🧹 **Troubleshooting & Maintenance Scenarios**

45. **Scenario: Container keeps crashing. Investigate exit code.**
    ➤ *Command:* `docker inspect <container_id> | grep ExitCode`

46. **Scenario: Monitor container resource usage.**
    ➤ *Command:* `docker stats`

47. **Scenario: Find IP address of a container.**
    ➤ *Command:* `docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' web`

48. **Scenario: Identify containers with high CPU.**
    ➤ *Command:* `docker stats --no-stream | sort -k3 -r`

49. **Scenario: Copy logs or config from container to host.**
    ➤ *Command:* `docker cp <container_id>:/app/logs ./logs`


