
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

12. **Scenario: Clean up unused images to save disk space.**
    ➤ *Command:* `docker image prune -a`

13. **Scenario: Pull a Redis image for an upcoming project.**
    ➤ *Command:* `docker pull redis`

14. **Scenario: Build a new Docker image from a project folder.**
    ➤ *Command:* `docker build -t myapp:latest .`

15. **Scenario: You need to upload a custom image to Docker Hub.**
    ➤ *Command:*

    ```
    docker tag myapp yourdockerhub/myapp  
    docker push yourdockerhub/myapp
    ```

16. **Scenario: Download an image from a colleague as a tar file. Load it.**
    ➤ *Command:* `docker load -i myapp.tar`

17. **Scenario: Save your current Docker image to share offline.**
    ➤ *Command:* `docker save -o myapp.tar myapp:latest`

18. **Scenario: Check what's inside a custom image.**
    ➤ *Command:* `docker inspect myapp:latest`

19. **Scenario: Compare two images for differences.**
    ➤ *Command:* `docker history <image_id>`

20. **Scenario: Search for a lightweight Apache image.**
    ➤ *Command:* `docker search httpd`

---

### 🌐 **Networking Scenarios**

21. **Scenario: Check existing networks used by containers.**
    ➤ *Command:* `docker network ls`

22. **Scenario: Create a custom bridge network for isolated communication.**
    ➤ *Command:* `docker network create backend-net`

23. **Scenario: Launch a MySQL container inside a custom network.**
    ➤ *Command:* `docker run -d --name mysql --network backend-net mysql`

24. **Scenario: Connect a running container to another network.**
    ➤ *Command:* `docker network connect backend-net web`

25. **Scenario: Disconnect a container to isolate it.**
    ➤ *Command:* `docker network disconnect backend-net web`

26. **Scenario: Deploy NGINX and expose it on port 8080.**
    ➤ *Command:* `docker run -d -p 8080:80 nginx`

27. **Scenario: Run a local Flask app and bind two ports.**
    ➤ *Command:* `docker run -d -p 5000:5000 -p 8000:8000 myflaskapp`

28. **Scenario: You want maximum speed — use host network mode.**
    ➤ *Command:* `docker run --network host myservice`

29. **Scenario: Inspect how a container sees the network.**
    ➤ *Command:* `docker exec -it web ping mysql`

30. **Scenario: Check which containers are on a specific network.**
    ➤ *Command:* `docker network inspect backend-net`

---

### 🛠️ **Volumes and Persistent Data Scenarios**

31. **Scenario: Create a volume for persistent data.**
    ➤ *Command:* `docker volume create mydata`

32. **Scenario: Use the volume in a Postgres container.**
    ➤ *Command:*

    ```bash
    docker run -d --name pg \
      -e POSTGRES_PASSWORD=pass \
      -v mydata:/var/lib/postgresql/data postgres
    ```

33. **Scenario: Inspect what's inside the volume.**
    ➤ *Command:* `docker volume inspect mydata`

34. **Scenario: Remove a volume that’s no longer in use.**
    ➤ *Command:* `docker volume rm mydata`

35. **Scenario: List all volumes and clean unused ones.**
    ➤ *Command:*

    ```bash
    docker volume ls  
    docker volume prune -f
    ```

---

### 📁 **Dockerfile & Compose Scenarios**

36. **Scenario: Build an image using Dockerfile for a Node.js app.**
    ➤ *Command:* `docker build -t nodeapp .`

37. **Scenario: Use Docker Compose to bring up a multi-container app.**
    ➤ *Command:* `docker-compose up -d`

38. **Scenario: Tear down the entire multi-container stack.**
    ➤ *Command:* `docker-compose down`

39. **Scenario: Rebuild only a specific service.**
    ➤ *Command:* `docker-compose build web`

40. **Scenario: Scale up the number of containers for load testing.**
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
