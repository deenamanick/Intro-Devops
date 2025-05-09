
### 🔰 **Basic Container Management Scenarios**

1. **Scenario: Check what’s currently running on your Docker host.**
   
    ➤ *Goal:* List running containers for debugging.
   
    ➤ *Command:* `docker ps`
   

3. **Scenario: You want to clean up the environment. List all containers, even stopped ones.**
   
   ➤ *Command:* `docker ps -a`

5. **Scenario: Your web server container crashed. Restart it. Make sure web-server container should be running already**
   ➤ *Command:* `docker start web-server`
   
   *Example* - `docker run -d --name web-server -p 8080:80 nginx`

7. **Scenario: You need to stop a misbehaving container.**
   
   ➤ *Command:* `docker stop web-server`

9. **Scenario: The app container needs a fresh restart after config change.**
    
   ➤ *Command:* `docker restart app-container`

11. **Scenario: Remove unnecessary containers to free space.**

   ➤ *Command:* `docker rm old_container`

14. **Scenario: Your manager asks you to launch a new NGINX server.**
    
   ➤ *Command:* `docker run -d --name web nginx`

16. **Scenario: You need shell access to a container to check logs manually.**
    
   ➤ *Command:* `docker exec -it web bash`

18. **Scenario: Investigate container logs for a failed deployment.**
    
    ➤ *Command:* `docker logs web`

---

### 📦 **Image Management Scenarios**

11. **Scenario: You want to check if the required image is available locally.**
    
    ➤ *Command:* `docker images`

13. **Scenario: Clean up unused images to save disk space.**
    
    ➤ *Command:* `docker image prune -a`

15. **Scenario: Pull a Redis image for an upcoming project.**
    
    ➤ *Command:* `docker pull redis`

17. **Scenario: Build a new Docker image from a project folder.**
    
    ➤ *Command:* `docker build -t myapp:latest .`

22. **Scenario: Check what's inside a custom image.**
    
    ➤ *Command:* `docker inspect myapp:latest`

24. **Scenario: Compare two images for differences.**
    
    ➤ *Command:* `docker history <image_id>`

26. **Scenario: Search for a lightweight Apache image.**
    
    ➤ *Command:* `docker search httpd`

---

28. **Scenario: Deploy NGINX and expose it on port 8080.**
    ➤ *Command:* `docker run -d -p 8080:80 nginx`

31. **Scenario: Inspect how a container sees the network.**
    
    ➤ *Command:* `docker exec -it web ping mysql`

---

### 📁 **Dockerfile & Compose Scenarios**

36. **Scenario: Build an image using Dockerfile for a Node.js app.**
    
    ➤ *Command:* `docker build -t nodeapp .`

38. **Scenario: Use Docker Compose to bring up a multi-container app.**
    
    ➤ *Command:* `docker-compose up -d`

40. **Scenario: Tear down the entire multi-container stack.**
    ➤ *Command:* `docker-compose down`

41. **Scenario: Rebuild only a specific service.**
    ➤ *Command:* `docker-compose build web`

42. **Scenario: Scale up the number of containers for load testing.**
    ➤ *Command:* `docker-compose up --scale web=3`

---

### 🔐 **Security and Resource Control Scenarios**

41. **Scenario: Limit memory usage of a container to 200MB.**
    ➤ *Command:* `docker run -d --memory=200m myapp`

42. **Scenario: Limit CPU usage of a container.**
    ➤ *Command:* `docker run -d --cpus=1 myapp`

43. **Scenario: Scan your image for vulnerabilities (Docker Desktop or Trivy).**
    ➤ *Command:* `trivy image myapp`

44. **Scenario: Run container as non-root user.**
    ➤ *Dockerfile Sample:*

    ```dockerfile
    FROM node  
    RUN useradd -m appuser  
    USER appuser  
    ```

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

50. **Scenario: You broke the container config. Roll it back using a new version tag.**
    ➤ *Command:*

    ```bash
    docker pull myapp:v1.1  
    docker run -d myapp:v1.1
    ```

---

Would you like this list as a downloadable PDF or formatted as a learning handout for students?
