
---

## **50 Linux Commands (Basic to Advanced)**

---

### **1. File and Directory Management**
1. **`pwd`** - Print the current working directory.
   ```bash
   pwd
   ```
2. **`ls`** - List files and directories.
   ```bash
   ls -l  # Long listing
   ls -a  # Include hidden files
   ```
3. **`cd`** - Change directory.
   ```bash
   cd /path/to/directory
   cd ..  # Move up one directory
   ```
4. **`mkdir`** - Create a directory.
   ```bash
   mkdir myfolder
   mkdir -p dir1/dir2/dir3  # Create nested directories
   ```
6. **`touch`** - Create an empty file or update timestamps.
   ```bash
   touch file.txt
   ```
7. **`cp`** - Copy files or directories.
   ```bash
   cp file.txt /path/to/destination
   cp -r dir1/ dir2/  # Copy directories recursively
   ```
8. **`mv`** - Move or rename files or directories.
   ```bash
   mv file.txt /path/to/destination
   mv oldname.txt newname.txt  # Rename a file
   ```
9. **`rm`** - Remove files or directories.
   ```bash
   rm file.txt
   rm -r dir/  # Remove directories recursively
   ```
10. **`find`** - Search for files or directories.
    ```bash
    find /path -name "file.txt"
    find /path -type f -mtime +7  # Find files modified more than 7 days ago
    ```

---

### **2. Text Processing**
11. **`cat`** - Display file content.
    ```bash
    cat file.txt
    ```
16. **`grep`** - Search text using patterns.
    ```bash
    grep "pattern" file.txt
    grep -i "pattern" file.txt  # Case-insensitive search
    ```

---

### **3. System Information**
21. **`uname`** - Display system information.
    ```bash
    uname -a  # Show all system information
    ```
22. **`df`** - Display disk space usage.
    ```bash
    df -h  # Human-readable format
    ```
23. **`du`** - Display directory space usage.
    ```bash
    du -sh /path/to/directory  # Summarize directory size
    ```
24. **`top`** - Display system processes.
    ```bash
    top
    ```
   
26. **`ps`** - Display running processes.
    ```bash
    ps aux
    ```
27. **`free`** - Display memory usage.
    ```bash
    free -h  # Human-readable format
    ```
28. **`uptime`** - Show system uptime.
    ```bash
    uptime
    ```
29. **`who`** - Display logged-in users.
    ```bash
    who
    ```
---

### **4. Networking**
31. **`ping`** - Test network connectivity.
    ```bash
    ping google.com
    ```
32. **`ifconfig`** - Display network interfaces (use `ip` on newer systems).
    ```bash
    ifconfig
    ```
33. **`netstat`** - Display network connections.
    ```bash
    netstat -tuln  # Show listening ports
    ```
34. **`ssh`** - Connect to a remote server.
    ```bash
    ssh user@remote_host
    ```
35. **`scp`** - Securely copy files between hosts.
    ```bash
    scp file.txt user@remote_host:/path/to/destination
    ```
36. **`wget`** - Download files from the web.
    ```bash
    wget https://example.com/file.zip
    ```
37. **`curl`** - Transfer data from or to a server.
    ```bash
    curl -O https://example.com/file.zip
    ```
38. **`nslookup`** - Query DNS records.
    ```bash
    nslookup google.com
    ```
39. **`dig`** - DNS lookup utility.
    ```bash
    dig google.com
    ```
40. **`traceroute`** - Trace the path packets take to a network host.
    ```bash
    traceroute google.com
    ```

---

### **5. User and Group Management**
41. **`useradd`** - Add a user.
    ```bash
    useradd username
    ```
42. **`usermod`** - Modify a user.
    ```bash
    usermod -aG groupname username  # Add user to a group
    ```
43. **`userdel`** - Delete a user.
    ```bash
    userdel username
    ```
44. **`groupadd`** - Add a group.
    ```bash
    groupadd groupname
    ```
45. **`groupmod`** - Modify a group.
    ```bash
    groupmod -n newgroupname oldgroupname
    ```
46. **`groupdel`** - Delete a group.
    ```bash
    groupdel groupname
    ```
47. **`passwd`** - Change user password.
    ```bash
    passwd username
    ```
48. **`su`** - Switch user.
    ```bash
    su username
    ```
49. **`sudo`** - Execute commands as a superuser.
    ```bash
    sudo command
    ```
50. **`id`** - Display user and group information.
    ```bash
    id username
    ```

---

### **6. Advanced Commands**
- **`tar`** - Archive files.
  ```bash
  tar -cvf archive.tar /path/to/files  # Create archive
  tar -xvf archive.tar  # Extract archive
  ```
- **`systemctl`** - Manage system services.
  ```bash
  systemctl start servicename
  systemctl enable servicename


### **Linux Filesystem Structure**  

The **Linux filesystem structure** follows the **FHS (Filesystem Hierarchy Standard)**, which organizes files and directories in a hierarchical manner starting from the **root directory (`/`)**.

### **Main Directories in Linux Filesystem:**

📂 **`/` (Root Directory)**  
- The **top-level** directory, from which all other directories branch out.

📂 **`/bin` (Binary Files)**  
- Contains **essential system binaries** (executables) like `ls`, `cp`, `mv`, `rm`, `cat`, etc.

📂 **`/sbin` (System Binaries)**  
- Stores **administrative commands** like `fdisk`, `ifconfig`, and `shutdown`.

📂 **`/etc` (Configuration Files)**  
- Contains **system-wide configuration files** like `/etc/passwd`, `/etc/hosts`, and `/etc/fstab`.

📂 **`/home` (User Home Directories)**  
- Stores **personal files and settings** for each user (`/home/user1`, `/home/user2`).

📂 **`/root` (Root User’s Home Directory)**  
- Home directory for the **superuser (root)**.

📂 **`/var` (Variable Data)**  
- Stores **logs (`/var/log`), mail, cache, and databases**.

📂 **`/usr` (User Programs & Utilities)**  
- Contains **user applications**, libraries, and documentation (`/usr/bin`, `/usr/lib`).

📂 **`/tmp` (Temporary Files)**  
- Holds **temporary files** that may be deleted after reboot.

📂 **`/dev` (Device Files)**  
- Represents **hardware devices** as files (`/dev/sda` for a hard disk, `/dev/null`).

📂 **`/proc` (Process Information Virtual Filesystem)**  
- A virtual filesystem that stores **system and process information** (`/proc/cpuinfo`, `/proc/meminfo`).

📂 **`/sys` (System Information Virtual Filesystem)**  
- Provides **kernel and hardware-related information**.

📂 **`/mnt` and `/media` (Mount Points)**  
- Used to mount **external storage devices**.

📂 **`/opt` (Optional Software)**  
- Contains **third-party software packages**.

📂 **`/lib` and `/lib64` (Libraries)**  
- Stores **shared libraries** required by system programs.

📂 **`/boot` (Boot Loader Files)**  
- Contains **kernel and boot-related files**, like `vmlinuz` and `grub`.

📂 **`/srv` (Service Data)**  
- Used for **data from network services**, like web servers.

Would you like a **detailed explanation** of any specific directory? 🚀

  ![image](https://github.com/user-attachments/assets/1bab34e0-8147-473d-a76b-7ea5148a6b92)


### **Types of Files in Linux (with Examples)**  

Linux treats everything as a **file**, and files are categorized into different types based on their purpose and behavior.

---

### **1️⃣ Regular Files (`-`)**  
These are the most common files and can contain text, binary data, or scripts.  
📌 **Example:**  
- **Text files:** `file.txt`, `notes.docx`
- **Binary files:** `program.exe`, `image.png`
- **Scripts:** `script.sh`, `program.py`

🔹 **Command to check file type:**  
```bash
ls -l
```
🔹 **Example output:**  
```
-rw-r--r-- 1 user user 1234 Mar 20 10:00 file.txt
```
(`-` at the beginning indicates a **regular file**.)

---

### **2️⃣ Directory Files (`d`)**  
A directory is a container that stores other files and directories.  

📌 **Example:**  
- `/home/user/`
- `/etc/`
- `/var/log/`

🔹 **Command to check directory type:**  
```bash
ls -l
```
🔹 **Example output:**  
```
drwxr-xr-x 2 user user 4096 Mar 20 10:05 Documents
```
(`d` at the beginning indicates a **directory**.)

---



### **Summary Table of Linux File Types**  

| **File Type**  | **Symbol** | **Example**                        |
|--------------|----------|--------------------------------|
| Regular File  | `-`        | `file.txt`, `script.sh`        |
| Directory File  | `d`        | `/home/user`, `/etc/`         |

### **`sudo` vs `su -` in Linux**  

Both `sudo` and `su -` are used to **gain superuser (root) privileges**, but they work differently.  

---

### **1️⃣ `sudo` (Superuser Do)**  
🔹 **Runs a single command as another user (default: root)**  
🔹 **Temporary** privilege escalation  
🔹 Users must be listed in the **sudoers file**  

📌 **Example:**  
```bash
sudo apt update
sudo systemctl restart apache2
```
✅ **Best for:** Running **specific admin tasks** without switching users.  
✅ **More secure** than `su -` (logs all activity).  
✅ **Session expires** after some time (default: 15 minutes).  

---

### **2️⃣ `su -` (Switch User to Root)**  
🔹 **Switches to the root user account completely**  
🔹 **Requires the root password**  
🔹 Loads the **root user's environment and profile**  

📌 **Example:**  
```bash
su -
```
Then, enter the **root password** to switch. Now, all commands run as root.  

✅ **Best for:** Performing **multiple admin tasks** in one session.  
❌ **Risky** if used carelessly, as you stay in root mode until exiting.  
❌ Requires knowing the **root password** (which might be disabled on some systems).  

---

### **Key Differences Table**  

| Feature         | `sudo`                          | `su -`                         |
|---------------|--------------------------------|--------------------------------|
| Execution Scope | Runs **one** command as root  | Switches **entire session** to root |
| Requires Root Password | ❌ No (uses user's password) | ✅ Yes (root password required) |
| Security      | ✅ More secure (logs actions) | ❌ Risky (full root access) |
| User Environment | Uses **current user's** environment | Loads **root's** environment |
| Best for      | Occasional **admin tasks** | Full **admin session** |

---

### **When to Use What?**
🔹 **Use `sudo`** for most administrative tasks (safer).  
🔹 **Use `su -`** only when performing multiple root actions.  

### **Soft Link vs Hard Link in Linux**  

Both **soft links (symbolic links)** and **hard links** allow multiple references to a file, but they function differently.  

---

### **1️⃣ Soft Link (Symbolic Link)**
🔹 A **shortcut** that points to the original file.  
🔹 If the original file is **deleted**, the soft link becomes **broken** (dangling).  
🔹 Can link to **files** or **directories** (unlike hard links).  
🔹 Created using:  
```bash
ln -s target_file soft_link_name
```

📌 **Example:**  
```bash
ln -s /home/user/file1.txt link1.txt
ls -l
```
**Output:**  
```
lrwxrwxrwx 1 user user   10 Mar 21 12:00 link1.txt -> file1.txt
```
✅ Used for **creating shortcuts** across different file systems.  
✅ Can link to **directories**.  

---



## **Package Managers: `yum`, `apt`, and `dnf`**
Package managers are used to install, update, and manage software packages in Linux.

---

### **1️⃣ `yum` (Yellowdog Updater, Modified)**
📌 **Used in:** RHEL, CentOS 7, Fedora (before DNF)  
📌 **Replaced by:** `dnf` in later versions  
📌 **Example Commands:**
```bash
# Install a package
sudo yum install httpd -y

# Remove a package
sudo yum remove httpd -y

# Update all packages
sudo yum update -y

# List installed packages
yum list installed

# Search for a package
yum search nginx
```

---


---

### **3️⃣ `apt` (Advanced Package Tool)**
📌 **Used in:** Debian, Ubuntu, and their derivatives  
📌 **Example Commands:**
```bash
# Update package list
sudo apt update

# Upgrade all installed packages
sudo apt upgrade -y

# Install a package
sudo apt install apache2 -y

# Remove a package
sudo apt remove apache2 -y

# List installed packages
apt list --installed

# Search for a package
apt search nginx
```

---

## **Key Differences**
| Feature      | `yum` (Old) | `dnf` (New) | `apt` |
|-------------|------------|-------------|-------|
| Used In     | RHEL 7, CentOS 7 | RHEL 8+, Fedora 22+ | Debian, Ubuntu |
| Speed       | Slower     | Faster, better dependency resolution | Moderate |
| Replacement | Replaced by `dnf` | Current default | Still used |
| Command Syntax | Similar to `dnf` | Improved over `yum` | Different |



### **Standard Input (`stdin`), Standard Output (`stdout`), and Standard Error (`stderr`) in Linux**  

Linux and Unix-based operating systems use three standard data streams for input and output operations:  

---

### **1️⃣ Standard Input (`stdin`)**
📌 **Definition**:  
- `stdin` (Standard Input) is the default source for receiving input data.  
- Typically, it comes from the keyboard but can also be redirected from a file or another command.

📌 **Example:**
```bash
cat > file.txt
# Now type some text, then press Ctrl+D to save and exit.
```
📌 **Using `stdin` from a file:**
```bash
cat < file.txt  # Reads input from file.txt instead of keyboard
```

---

### **2️⃣ Standard Output (`stdout`)**
📌 **Definition**:  
- `stdout` (Standard Output) is the default stream where programs send their output.  
- By default, it displays on the terminal but can be redirected to a file.

📌 **Example:**
```bash
echo "Hello, World!"
```
📌 **Redirecting `stdout` to a file:**
```bash
ls > output.txt  # Saves output of ls to output.txt
```

---

### **3️⃣ Standard Error (`stderr`)**
📌 **Definition**:  
- `stderr` (Standard Error) is used for error messages and diagnostics.  
- It is separate from `stdout` to prevent errors from mixing with normal output.

📌 **Example:**
```bash
ls /nonexistent_directory 2> error.log  # Redirects error to error.log
```

---

### **Redirection Operators**
| Symbol | Description | Example |
|--------|------------|---------|
| `>` | Redirect `stdout` to a file (overwrite) | `ls > file.txt` |
| `>>` | Append `stdout` to a file | `ls >> file.txt` |
| `<` | Redirect `stdin` from a file | `cat < file.txt` |
| `2>` | Redirect `stderr` to a file | `ls /wrongpath 2> errors.txt` |
| `&>` | Redirect both `stdout` and `stderr` to a file | `ls &> output.txt` |
| `2>&1` | Merge `stderr` into `stdout` | `ls > output.txt 2>&1` |


### **1️⃣ Source Command (`source` or `.`)**
📌 **Definition**:  
- The `source` command is used to execute commands from a file in the **current shell** instead of starting a new shell.  
- It is commonly used to reload environment variables and scripts.

📌 **Syntax:**
```bash
source filename
# or
. filename  # (dot command does the same thing)
```

📌 **Example:**
```bash
source ~/.bashrc  # Reloads shell configuration without logging out
```
- If we run a script normally (`bash script.sh`), it runs in a **new shell**.  
- But if we run it with `source script.sh`, it executes **in the same shell**, affecting environment variables.

---

### **2️⃣ Shell Scripting (`.sh` scripts)**
📌 **Definition**:  
- Shell scripting is writing a series of commands in a file (`.sh`) to automate tasks in Linux.

📌 **Basic Script Example (`script.sh`)**
```bash
#!/bin/bash
echo "Hello, $USER!"
date
```
📌 **Making the script executable:**
```bash
chmod +x script.sh
```
📌 **Running the script:**
```bash
./script.sh  # Runs in a new shell
source script.sh  # Runs in the current shell
```

---

### **3️⃣ Key Differences: `source` vs `sh` vs `./script.sh`**
| Command | Effect |
|---------|--------|
| `source script.sh` | Runs the script in the **same shell**, so variables and changes persist. |
| `sh script.sh` | Runs the script in a **new shell**, changes do not persist. |
| `./script.sh` | Runs the script in a new shell, but requires execute permission (`chmod +x`). |

Would you like more scripting examples? 🚀

---

