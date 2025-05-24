

---

# **Basic Networking Concepts for DevOps Engineer**

## **1. Introduction to Networking**
A **computer network** is a group of interconnected computers that communicate with each other to share resources, data, and applications. Each device in a network is assigned an **IP address**, which serves as its unique identifier.

### **Types of Networks**
1. **Personal Area Network (PAN)** – Small network for personal use (e.g., Bluetooth).

![image](https://github.com/user-attachments/assets/e5d3d37f-c838-4916-a2b0-1961264eafb2)



2. **Local Area Network (LAN)** – Covers a small geographic area like a home, office, or school.

![image](https://github.com/user-attachments/assets/ac793c5d-b451-4905-9af8-965560b5ca6e)



3. **Metropolitan Area Network (MAN)** – Covers a city or town.

![image](https://github.com/user-attachments/assets/99c34bf6-e75a-433e-8ac8-46aa66414b91)



4. **Wide Area Network (WAN)** – Spans large areas like countries or continents (e.g., the Internet).

![image](https://github.com/user-attachments/assets/693ce589-84cb-46df-a609-affaf583ff06)





5. **Virtual Private Network (VPN)** – Secures private communications over public networks.



![image](https://github.com/user-attachments/assets/eb2f5dc9-5a63-495c-b0b6-566bdf80736c)


---

## **2. OSI and TCP/IP Models**
### **OSI Model (7 Layers)**

![image](https://github.com/user-attachments/assets/1419f69e-76ca-4e9d-a73c-fdec35976515)


1. **Physical Layer** – Deals with physical transmission (e.g., cables, radio waves). ![image](https://github.com/user-attachments/assets/a3b5e29b-1bec-433a-95ef-156262d98331)

2. **Data Link Layer** – Handles MAC addressing and error detection.
3. **Network Layer** – Manages IP addressing and routing. ![image](https://github.com/user-attachments/assets/7fac8029-6b10-45db-bb45-2d71d4303f38)

4. **Transport Layer** – Ensures reliable communication using TCP/UDP. ![image](https://github.com/user-attachments/assets/d10b14a6-a2a2-4e9a-87fc-8fae62e7d1bb)

5. **Session Layer** – Maintains communication sessions.
6. **Presentation Layer** – Converts data formats (e.g., encryption).
7. **Application Layer** – Provides network services to users (e.g., HTTP, FTP). ![image](https://github.com/user-attachments/assets/39971bbf-6936-424a-92bb-eb90dd3d6a88)

   

### **TCP/IP Model (4 Layers)**

![image](https://github.com/user-attachments/assets/a28a325e-1925-4d2e-b520-3345bdf23af3)



1. **Network Access Layer** – Combines OSI’s Physical & Data Link layers.
2. **Internet Layer** – Equivalent to OSI’s Network Layer (IP addressing & routing).
3. **Transport Layer** – Uses TCP (reliable) or UDP (fast but unreliable).
4. **Application Layer** – Includes HTTP, FTP, SMTP, etc.

---

## **3. IP Addressing and Subnetting**
An **IP address** is a numerical label assigned to each device connected to a network.

### **IPv4 Address Classes**
| Class | Range | Default Subnet Mask | No. of Networks | No. of Hosts |
|--------|--------------|----------------|--------------|--------------|
| A | 1.0.0.0 - 126.255.255.255 | 255.0.0.0 | 128 | 16 million |
| B | 128.0.0.0 - 191.255.255.255 | 255.255.0.0 | 16,384 | 65,536 |
| C | 192.0.0.0 - 223.255.255.255 | 255.255.255.0 | 2 million | 256 |
| D | 224.0.0.0 - 239.255.255.255 | - | Multicast | - |
| E | 240.0.0.0 - 255.255.255.255 | - | Reserved | - |

### **Private vs Public IP Addresses**
- **Private IPs:** Used within a LAN (e.g., 192.168.x.x, 10.x.x.x, 172.16.x.x).
- **Public IPs:** Routable on the Internet, assigned by ISPs.

### **Subnetting**
Subnetting divides a large network into smaller networks.

- **Subnet Mask:** Defines network and host portions.
- **CIDR Notation:** `/8`, `/16`, `/24` indicate how many bits are for the network.
- Example:  
  - `192.168.1.0/24` (Subnet mask: 255.255.255.0) → 256 total IPs, 254 usable.
  - `192.168.1.0/26` (Subnet mask: 255.255.255.192) → 64 total IPs, 62 usable.

---

## **4. Network Devices**
### **Router**

A router connects different networks and directs data between them using routing. Routing creates paths for data to travel across networks. Routers work at Layer 3 of the OSI model and often include interfaces for setting rules like port forwarding and firewalling.

- Connects different networks.
- Uses IP addresses to route data.
- Example: Home router connects your LAN to the Internet.

  ![image](https://github.com/user-attachments/assets/dccf643f-642b-4feb-a593-d7e2e021f5b2)
  ![image](https://github.com/user-attachments/assets/ff1e3949-0ff1-40c8-927a-0b8001c05c03)



### **Switch**
- Connects devices within a LAN.
- Uses MAC addresses to forward data efficiently.

  ![image](https://github.com/user-attachments/assets/05777874-065f-43fe-abe8-ba8a824d0399)

![image](https://github.com/user-attachments/assets/131f2802-5fc2-4a45-93d1-8ca8231d2d75)

---

## **5. Subnetting Practice**

![image](https://github.com/user-attachments/assets/25973873-65fd-442d-ab9b-3040b06a8e47)


### **Example 1:**
- Given: **192.168.1.0/26**
- Subnet Mask: **255.255.255.192**
- **Network ID:** `192.168.1.0`
- **Broadcast Address:** `192.168.1.63`
- **Usable IPs:** `192.168.1.1` to `192.168.1.62`
- **Total Hosts:** 64, **Usable Hosts:** 62

### **Example 2:**
- Given: **10.0.0.0/30**
- **Subnet Mask:** `255.255.255.252`
- **Usable IPs:** 2 (for point-to-point links)
- 


## **6. Types of Routing**

### **Types of Routing:**  

1. **Static Routing:**  
   - A technique where the network administrator manually adds routes to the routing table.  
   - It does not change automatically if the network topology changes.  
   - Suitable for small, stable networks with minimal route changes.  

2. **Default Routing:**  
   - A method where a router is configured to forward all packets to a predetermined next-hop device, regardless of the destination network.  
   - Commonly used when a router has only one exit path to an external network (e.g., connecting a local network to the internet).  

3. **Dynamic Routing:**  
   - A routing technique that uses dynamic protocols (e.g., RIP, OSPF, BGP) to automatically discover and update routes.  
   - Adapts to network topology changes without manual intervention.  
   - Suitable for large and complex networks.  


### What is a Protocol? 

● A system that allows two parties to communicate

● A protocol is designed with a set of properties

● Depending on the purpose of the protocol

● TCP, UDP, HTTP, gRPC, FTP

![Uploading image.png…]()


## Protocol Properties

Here's a detailed breakdown of each networking concept with examples:

---

### **1. Data Format**
Defines how data is structured before transmission.

#### **a. Text-based Formats**
- **Plain Text**: Simple human-readable format.
  - Example: Sending an email using SMTP.
  
- **JSON (JavaScript Object Notation)**: Lightweight data-interchange format, widely used in APIs.
  - Example: REST API responses from a weather service (`{"temperature": 30, "unit": "Celsius"}`).

- **XML (Extensible Markup Language)**: Used for structured data exchange.
  - Example: SOAP web services (`<weather><temperature>30</temperature><unit>Celsius</unit></weather>`).

#### **b. Binary Formats**
- **Protocol Buffers (Protobuf)**: Compact and efficient data serialization format developed by Google.
  - Example: gRPC communication between microservices.

- **RESP (Redis Serialization Protocol)**: Used by Redis for data exchange.
  - Example: Sending a Redis command: `SET key value`.

- **h2 (HTTP/2) & h3 (HTTP/3)**: Use binary framing for efficient web communication.
  - Example: Faster loading of web pages using HTTP/2 multiplexing.

---

### **2. Transfer Mode**
Defines how data is transferred over the network.

#### **a. Message-based Transfer**
- **UDP (User Datagram Protocol)**: Lightweight, connectionless communication.
  - Example: Video streaming services like YouTube Live or VoIP (Skype, Zoom).

- **HTTP (Hypertext Transfer Protocol)**: Request-response protocol for web communication.
  - Example: A user requesting a webpage (`GET /index.html` from a browser).

#### **b. Stream-based Transfer**
- **TCP (Transmission Control Protocol)**: Reliable, ordered, and error-checked streaming.
  - Example: A file download using FTP (File Transfer Protocol).

- **WebRTC (Web Real-Time Communication)**: Peer-to-peer streaming of audio/video.
  - Example: Google Meet video calls.

---

### **3. Addressing System**
Defines how devices are identified in the network.

- **DNS Name**: Human-readable domain names resolved to IP addresses.
  - Example: `www.google.com` → `142.250.183.78`.

- **IP Address**: Unique identifier assigned to devices on a network.
  - Example: `192.168.1.1` for a router in a home network.

- **MAC Address**: Unique hardware address of a network device.
  - Example: `00:1A:2B:3C:4D:5E` for a laptop’s Wi-Fi adapter.

---

### **4. Directionality**
Defines how data flows in communication.

#### **a. Bidirectional Communication**
- **TCP (Transmission Control Protocol)**: Allows full two-way communication.
  - Example: SSH remote login, where both client and server can send data.

#### **b. Unidirectional Communication**
- **HTTP (Hypertext Transfer Protocol)**: One-way request-response.
  - Example: A user submits a search query on Google, and Google returns results.

#### **c. Full-Duplex vs Half-Duplex**
- **Full Duplex**: Data can be sent and received simultaneously.
  - Example: A telephone call where both parties can talk at the same time.

- **Half Duplex**: Data can be sent in only one direction at a time.
  - Example: Walkie-talkies, where one person talks while the other listens.
 
Here's a breakdown of each networking concept with explanations and examples:

---

## **5. State Management**
Defines whether a communication session maintains state information.

### **a. Stateful Communication**
Maintains session information across multiple requests.

- **TCP (Transmission Control Protocol)**  
  - Example: SSH session, where state is maintained to ensure ordered and reliable data transfer.
  
- **gRPC (Google Remote Procedure Call)**  
  - Example: A client-server system where a client sends multiple requests over a persistent connection.

- **Apache Thrift**  
  - Example: A microservices framework that maintains session information between client and server for efficient communication.

### **b. Stateless Communication**
Does not retain session state; each request is treated independently.

- **UDP (User Datagram Protocol)**  
  - Example: A DNS query, where a request for `www.google.com` is sent and a response is received without maintaining any session state.

- **HTTP (Hypertext Transfer Protocol)**  
  - Example: A browser requesting a webpage (`GET /index.html`), where each request is independent.

---

## **2. Routing**

Operates at network layer (Layer 3)

Makes forwarding decisions based on IP addresses

- **Example**: Internet routers directing packets

### **a. Proxies**
Acts as an intermediary between clients and servers.
Operates at application layer (Layer 7)

- **Example**: A company using an HTTP proxy to filter and monitor employee web traffic.

### **b. Gateways**
Translates communication between different network protocols.
Specialized type of proxy with protocol translation capabilities
Often implements business logic beyond simple forwarding

- **Example**: An API gateway that translates HTTP REST requests into gRPC calls for microservices.

- ![image](https://github.com/user-attachments/assets/51ea10fd-04bc-493a-a3f2-011dd3431def)

- API Gateways:

- Front door for external API consumers

- Handles versioning, rate limiting, authentication

- Example: Amazon API Gateway, Kong


---

## **3. Flow & Congestion Control**
Regulates data transfer rates to prevent network congestion.

### **a. TCP (Flow & Congestion Control)**
- Uses **window size adjustments** and **slow start** to prevent packet loss.
- Example: A file transfer using **FTP**, where TCP adjusts speed based on network conditions.

### **b. UDP (No Control)**
- Does not provide flow or congestion control, leading to potential packet loss.
- Example: **Live streaming** where lost packets are ignored rather than retransmitted.

---

## **4. Error Management**
Handles communication failures using predefined mechanisms.

### **a. Error Codes**
- Standard codes indicate specific issues.
- Example:  
  - **404 Not Found** (Webpage does not exist)  
  - **500 Internal Server Error** (Server-side failure)  

### **b. Retries and Timeouts**
- Retries: The client resends the request if no response is received.
- Timeouts: A predefined wait time before declaring failure.

- **Example (Retries)**:  
  - A payment gateway resending a failed transaction request.

- **Example (Timeouts)**:  
  - A browser waiting 30 seconds before showing a “Request Timeout” error.


 ---
 ### **Understanding Source and Destination Ports in Communication in UDP**

When **App1 (10.0.0.1)** sends data to **AppX (10.0.0.2)** using **Destination Port 53**, it follows these steps:

1. **App1 initiates a request**:  
   - Source IP: `10.0.0.1`  
   - Destination IP: `10.0.0.2`  
   - **Source Port**: `5555` (Randomly chosen by the OS)  
   - **Destination Port**: `53` (Well-known port for DNS)  

2. **AppX receives the request on Port 53** and processes it.

3. **AppX sends a response back to App1**, reversing the ports:  
   - Source IP: `10.0.0.2`  
   - Destination IP: `10.0.0.1`  
   - **Source Port**: `53` (Same as the destination port in the request)  
   - **Destination Port**: `5555` (Same as the source port in the request, so App1 knows where to receive the response)  

### **Key Takeaways**
- **Source Port**: Chosen dynamically by the client (e.g., `5555`).
- **Destination Port**: Well-known or registered port (e.g., `53` for DNS).
- **Response uses the original source port** so that the client application can correctly receive the data.

This process ensures proper **bidirectional communication** in **protocols like UDP (DNS requests) and TCP (HTTP, SSH, etc.).** 🚀

![image](https://github.com/user-attachments/assets/2776afc0-6f81-4a06-90c4-62109e1bfb15)

---

### **TCP Three-Way Handshake Explained (Connection Establishment)**  

When **App1 (10.0.0.1)** wants to establish a **TCP connection** with **AppX (10.0.0.2)**, the **three-way handshake** process ensures reliable communication:

---

### **Step 1: SYN (Synchronize)**
- **App1 (Client) → AppX (Server)**
- App1 sends a **SYN** packet to AppX to initiate the connection.
- The packet includes:  
  - **Source IP**: `10.0.0.1`
  - **Destination IP**: `10.0.0.2`
  - **Source Port**: Randomly chosen (e.g., `5555`)
  - **Destination Port**: Application-specific (e.g., `80` for HTTP)
  - **SYN flag**: Set to **1**
  - **Sequence Number**: `X` (randomly generated)
  
  **Example Packet:**  
  ```
  [SYN] 10.0.0.1:5555 → 10.0.0.2:80 (Seq=X)
  ```

---

### **Step 2: SYN-ACK (Acknowledge + Synchronize)**
- **AppX (Server) → App1 (Client)**
- AppX responds with a **SYN-ACK** packet, acknowledging App1’s SYN and synchronizing its own sequence.
- The packet includes:
  - **SYN flag**: Set to **1**
  - **ACK flag**: Set to **1**
  - **Sequence Number**: `Y` (randomly generated)
  - **Acknowledgment Number**: `X + 1` (confirms receipt of App1's SYN)
  
  **Example Packet:**  
  ```
  [SYN-ACK] 10.0.0.2:80 → 10.0.0.1:5555 (Seq=Y, Ack=X+1)
  ```

---

### **Step 3: ACK (Acknowledge)**
- **App1 (Client) → AppX (Server)**
- App1 sends an **ACK** packet, confirming receipt of AppX’s SYN.
- The packet includes:
  - **ACK flag**: Set to **1**
  - **Sequence Number**: `X + 1`
  - **Acknowledgment Number**: `Y + 1`
  
  **Example Packet:**  
  ```
  [ACK] 10.0.0.1:5555 → 10.0.0.2:80 (Seq=X+1, Ack=Y+1)
  ```

---

### **Connection Established ✅**
- Now, **App1 and AppX can exchange data over TCP** securely and reliably.
- The handshake ensures both parties are **ready to communicate** and establishes **initial sequence numbers**.

---

### **Key Takeaways**
- The **three-way handshake** prevents connection failures and ensures both sides agree on **initial sequence numbers**.
- Used in **TCP-based applications** like **HTTP, SSH, FTP, and SMTP**.
- **If one party does not respond**, the connection **times out** or retries before failing.



![image](https://github.com/user-attachments/assets/944dffa0-0a7f-41a2-b8c5-774ceb833fe8)


---

### **7. What Does the Ping Command Do?**  

The **ping** command is a network utility used to test the connectivity between two network devices. It sends ICMP (Internet Control Message Protocol) echo request packets to a specified IP address or hostname and waits for a response. This helps determine:  
- Whether a device is reachable on the network.  
- The response time (latency) between the source and destination.  
- Packet loss, which indicates network issues.  

### **8. What is a NIC (Network Interface Card)?**  
A **Network Interface Card (NIC)** is a hardware component that enables a computer to connect to a network. It can be wired (Ethernet) or wireless (Wi-Fi).  

#### **Key Features of a NIC:**  
- Each NIC has a unique **MAC (Media Access Control) address**, which identifies the device on the network.  
- It allows communication between computers in a **Local Area Network (LAN)** or over the internet.  
- NICs are commonly used in **desktop computers, laptops, and servers** for network connectivity.  


Your definitions of **Public Address** and **Private Address** are mostly correct but could be refined for better clarity and readability. Here’s an improved version:  

---

### **9) Public Address**  
A **Public IP Address** (also known as an **external address**) is assigned by an **Internet Service Provider (ISP)** and is used to communicate outside the local network. It allows devices to access the internet and be reached from remote locations.  

#### **Key Characteristics:**  
- **Global Scope** – Public IP addresses are unique and can be accessed over the internet.  
- **Assigned by ISP** – Internet providers allocate public IP addresses.  
- **Not Free** – Public IPs are provided by ISPs at a cost.  
- **Enables Remote Access** – It allows external users to connect to a device or server inside the network (e.g., hosting a home server).  

---

### **10) Private Address**  
A **Private IP Address** (also known as an **internal address**) is used within a **Local Area Network (LAN)** to communicate between devices. It cannot be accessed directly from the internet and helps maintain network security.  

#### **Key Characteristics:**  
- **Local Scope** – Only used within a private network (e.g., home or office network).  
- **Used for LAN Communication** – Enables communication between devices like computers, printers, and smartphones inside a network.  
- **Free of Cost** – Private IPs do not require ISP allocation and are available for free.  
- **Not Routed on the Internet** – Traffic from the internet cannot directly reach private IP addresses.  
- **Finding Private IP Address** – Use the command `ipconfig` (Windows) or `ifconfig` (Linux/macOS) to view the private IP of your device.  

### **11) What is a Proxy Server?**  
**Ans:** A **proxy server** is an **intermediary** between a user's device and the internet. It forwards requests from clients to web servers and then returns the requested data to the client.  

### **Key Functions of a Proxy Server:**  
- **Hides the Client's IP Address** – Enhances privacy and security.  
- **Filters Web Content** – Blocks restricted websites and harmful content.  
- **Caches Data** – Speeds up web browsing by storing frequently accessed resources.  
- **Improves Security** – Acts as a firewall by preventing direct connections to potentially harmful sites.  
- **Provides Anonymity** – Helps users stay anonymous by masking their real IP address.  


### **What is a Firewall?**  

A **firewall** is a **network security system** that monitors and controls incoming and outgoing network traffic based on **predefined security rules**. It acts as a **barrier** between a trusted internal network (e.g., a company’s private network) and an untrusted external network (e.g., the internet).  

![image](https://github.com/user-attachments/assets/daf06065-e6d2-4834-9b4f-3995cece334a)


### **Functions of a Firewall:**  
✅ **Monitors network traffic** – Inspects data packets entering or leaving a network.  
✅ **Blocks unauthorized access** – Prevents hackers and malicious traffic from entering the system.  
✅ **Implements security policies** – Enforces rules to allow or deny specific types of traffic.  
✅ **Prevents malware attacks** – Detects and blocks suspicious activity.  
✅ **Filters content** – Restricts access to certain websites or applications.  

### **Types of Firewalls:**  
1️⃣ **Packet Filtering Firewall (Layer 4)** – Works at the network and transport layers, filtering packets based on IP addresses, ports, and protocols.  
2️⃣ **Stateful Inspection Firewall** – Monitors active connections and makes decisions based on connection states.  
3️⃣ **Proxy Firewall (Layer 5 - Application Gateway)** – Acts as an intermediary between users and the internet, filtering requests based on content.  
4️⃣ **Next-Generation Firewall (NGFW)** – Uses advanced features like deep packet inspection, intrusion detection, and threat intelligence.  


### **Interconnection of ISPs (Internet Service Providers)**
  
ISPs (Internet Service Providers) interconnect to enable global internet communication. This interconnection allows data to travel from one network to another, ensuring seamless internet access for users worldwide.  

---

## **1️⃣ Types of ISP Interconnections**
There are three primary ways ISPs connect to each other:  

### **1.1 Peering (ISP-to-ISP Connection)**
- **Definition:** Direct connection between two ISPs to exchange traffic without a third party.
- **Types:**
  - **Public Peering:** Happens at an **Internet Exchange Point (IXP)**.
  - **Private Peering:** Direct connection between two ISPs using a dedicated link.
- **Example:** Two ISPs (e.g., Airtel and Jio) agree to exchange traffic **without** paying each other.

### **1.2 Transit (Smaller ISP Buying Internet from Larger ISP)**
- **Definition:** A smaller ISP pays a larger ISP (Tier 1) to access the global internet.
- **Example:** A local ISP in a small city buys internet connectivity from a national-level ISP.

### **1.3 Content Delivery Network (CDN) Peering**
- **Definition:** ISPs interconnect with CDNs to cache frequently accessed content closer to users.
- **Example:** Netflix, YouTube, and Cloudflare use CDN peering with ISPs to reduce latency.

---

## **2️⃣ ISP Hierarchy (Tiers of ISPs)**
ISPs are categorized into **three tiers** based on their network reach and interconnection model.

| **Tier** | **Description** | **Example ISPs** |
|----------|----------------|------------------|
| **Tier 1** | Largest ISPs with global network reach, forming the backbone of the internet. They do not pay for transit. | AT&T, Tata Communications, CenturyLink |
| **Tier 2** | Regional ISPs that buy internet transit from Tier 1 providers but may also peer with others. | Airtel, Jio, Vodafone |
| **Tier 3** | Local ISPs that buy internet from Tier 2 providers and serve end-users. | Small-town ISPs, broadband providers |

---

## **3️⃣ How ISPs Connect to the Global Internet**
- **IXPs (Internet Exchange Points):** Locations where multiple ISPs exchange traffic to improve efficiency.
- **BGP (Border Gateway Protocol):** The routing protocol ISPs use to communicate and exchange routes.
- **Undersea Fiber Optic Cables:** Used for international connectivity between ISPs across continents.

---

## **4️⃣ Real-World Example of ISP Interconnection**
1. A **local ISP** in a city connects to a **regional Tier 2 ISP** for internet access.
2. The **Tier 2 ISP** connects to a **Tier 1 ISP** for global internet access.
3. Tier 1 ISPs interconnect with each other using **peering agreements** to form the backbone of the internet.

---

![image](https://github.com/user-attachments/assets/cc4fa6d1-31f1-498f-9281-44ebf1f6877b)

### **Explanation of ISP Interconnection Diagram**  


---

## **1️⃣ Key Components in the Diagram**  

### **1. Tier 1 ISP (Top Level)**
- These are **global backbone ISPs** that provide internet access to lower-tier ISPs.
- They do **not pay** for transit as they peer with each other.
- Example: AT&T, Tata Communications, CenturyLink.

### **2. Internet Exchange Points (IXP)**
- **IXPs (gray boxes)** serve as **hubs** where ISPs exchange traffic efficiently.
- They help **reduce costs and improve speed** by enabling ISPs to connect directly instead of using intermediaries.

### **3. Regional ISPs (Middle Layer)**
- **Regional ISPs** buy internet transit from **Tier 1 ISPs** and distribute it further.
- They may also peer with **IXPs and Content Providers** for better performance.

### **4. Access ISPs (Bottom Layer)**
- These are **local ISPs** that provide internet to **end-users (homes, businesses, etc.).**
- They rely on **Regional ISPs** for internet connectivity.

### **5. Content Providers (e.g., Google, Netflix)**
- **Content providers** set up direct connections with ISPs and IXPs to serve users faster.
- Example: Google, YouTube, Netflix, Facebook (Meta).

---

## **2️⃣ How Data Flows in the Internet**
1. **User requests a website (e.g., Google.com).**
2. The request travels from the **Access ISP** → **Regional ISP** → **Tier 1 ISP**.
3. The **Tier 1 ISP** routes the request to **Google's servers**.
4. Google's response follows the same route back, ensuring fast content delivery.

---

## **3️⃣ Importance of ISP Interconnections**
✅ **Reduces Internet Costs** – Direct peering at **IXPs** avoids expensive transit fees.  
✅ **Improves Latency** – Content providers like **Google and Netflix** set up direct connections.  
✅ **Enhances Redundancy** – Multiple connections between ISPs prevent network failures.  

---


![image](https://github.com/user-attachments/assets/f7e29fae-4f06-4af0-9346-692f6088e5dd)


### **Explanation of the Distributed Denial-of-Service (DDoS) Attack Diagram**  

This diagram illustrates a **Distributed Denial-of-Service (DDoS) attack**, a cyberattack that overwhelms a victim's system with excessive traffic, causing service disruption.

---

## **1️⃣ Key Components in the Diagram**  

### **1. Attacker (Botmaster)**  
- The main hacker or attacker initiates the attack.
- They **send commands** to compromised systems (slaves/bots) to start the attack.  

### **2. Slave (Botnet) Computers**  
- These are infected computers (also called **zombies**) controlled by the attacker.  
- They send excessive requests or malicious traffic to the victim.  
- Often compromised through malware or security vulnerabilities.  

### **3. Victim (Target Server)**  
- The system under attack (e.g., a website, network, or server).  
- Overwhelmed by traffic from multiple slave computers, causing **slowdown or service failure**.  

### **4. Network Infrastructure**  
- The victim is often connected via a **router, firewall, or load balancer**.  
- The attack may overwhelm these devices, making legitimate access impossible.

---

## **2️⃣ How the DDoS Attack Works**  
1️⃣ **Attacker sends a command** to multiple compromised computers (**slaves/bots**).  
2️⃣ **Slaves generate a flood of traffic** (requests, data packets, or malicious connections).  
3️⃣ The **victim’s network or server gets overloaded** and becomes slow or completely unavailable.  

---

## **3️⃣ Types of DDoS Attacks**  
✅ **Volumetric Attacks** – Overloads bandwidth with excessive data traffic.  
✅ **Protocol Attacks** – Targets network components (e.g., SYN Flood, Ping of Death).  
✅ **Application Layer Attacks** – Overwhelms web applications (e.g., HTTP Flood).  

---

## **4️⃣ How to Defend Against DDoS Attacks**  
🔹 **Use Firewalls & Intrusion Prevention Systems (IPS).**  
🔹 **Enable Rate Limiting to limit excessive requests.**  
🔹 **Deploy a DDoS Mitigation Service (e.g., Cloudflare, Akamai).**  
🔹 **Monitor Traffic & Detect Anomalies using AI-based security tools.**  


---

![image](https://github.com/user-attachments/assets/da9292bc-1699-4105-93b6-93900d6f42bd)


### How DNS Works: From `/etc/hosts` to `resolv.conf` and Top-Level Domains  

DNS (Domain Name System) is responsible for translating human-readable domain names (e.g., `example.com`) into IP addresses that computers use to communicate. Here’s how it works from local configuration files to the global DNS hierarchy:

---

### **1. Local Name Resolution: `/etc/hosts` File**  
- Before querying external DNS servers, a Linux system first checks the `/etc/hosts` file.
- This file contains mappings of domain names to IP addresses.
- Example:
  ```bash
  127.0.0.1   localhost
  192.168.1.10   myserver.local
  ```
- If a domain is found in `/etc/hosts`, the system does not query a DNS server.

---

### **2. DNS Resolver and `resolv.conf`**
- If the requested domain is not found in `/etc/hosts`, the system checks `/etc/resolv.conf` to find which DNS servers to query.
- This file specifies the nameservers (DNS servers) to be used for domain resolution.
- Example:
  ```bash
  nameserver 8.8.8.8
  nameserver 1.1.1.1
  ```
- The system will query these servers in order until one responds.

---

### **3. Querying the DNS Hierarchy**
If the domain is not cached locally, the system queries the configured DNS servers. The process follows a hierarchical structure:

#### **a) Root DNS Servers**
- The request starts at one of the **13 root DNS servers**.

  ![image](https://github.com/user-attachments/assets/cda3d705-c87d-4023-95ed-65f531e8f8d2)

- Root servers direct queries to the relevant **Top-Level Domain (TLD) servers**.

#### **b) Top-Level Domain (TLD) Servers**
- TLD servers handle domains based on their extensions, such as:
  - `.com` (commercial) → `com DNS servers`
  - `.org` (organizations) → `org DNS servers`
  - `.edu` (education) → `edu DNS servers`
- The TLD server directs the query to the appropriate domain’s authoritative name server.

#### **c) Authoritative DNS Servers**
- These servers store specific domain records.
- Example:
  - For `amazon.com`, the authoritative DNS server provides the actual IP address.
  - This information is returned to the client.

---

### **4. Caching and Response**
- Once the IP is resolved, the system stores it in a **DNS cache** to speed up future queries.
- Cached results reduce network traffic and response time.

  ![image](https://github.com/user-attachments/assets/55a2246d-7d88-49c4-b798-8f1192e6352b)


---

### **Summary of DNS Resolution Flow**
1. **Check `/etc/hosts`** → If found, use the mapped IP.
2. **Check `/etc/resolv.conf`** → Identify external DNS servers.
3. **Query Root DNS Servers** → Directs to the TLD DNS server.
4. **Query TLD DNS Server** → Directs to authoritative DNS.
5. **Query Authoritative DNS Server** → Returns the actual IP.
6. **Cache the result** for future use.



---

### **Understanding Mutual TLS (mTLS) in a Simple Way**  

## **What is TLS?**  
- **TLS (Transport Layer Security)** is like a **secret conversation** between your web browser and a website.  
- It keeps **hackers from listening** to your data and **ensures the website is real** (not fake).  
- TLS replaced **SSL (an older version)** and is mostly used in **HTTPS websites** (like online banking or shopping).  

### **Understanding Secure Communication: HTTP, HTTPS, and TLS**  

### **1. Vanilla HTTP (Unencrypted)**
- **Hypertext Transfer Protocol (HTTP)** transmits data in **plain text**.
- **No encryption**, making it vulnerable to:
  - **Eavesdropping** (Attackers can read data)
  - **Man-in-the-Middle (MITM) attacks**
  - **Data modification**
- **Example:**  
  - `http://example.com`
  - Browsers mark it as **"Not Secure"** ⚠️.
 
    ![image](https://github.com/user-attachments/assets/5076ee21-32d5-4280-8f38-70979ec9b34c)


---

### **2. HTTPS (Secure HTTP)**
- **Hypertext Transfer Protocol Secure (HTTPS)** = **HTTP + TLS/SSL encryption**.
- Uses **Transport Layer Security (TLS)** for:
  - **Encryption:** Protects data from being intercepted.
  - **Integrity:** Ensures data is not altered in transit.
  - **Authentication:** Uses SSL/TLS certificates to verify server identity.
- **Example:**  
  - `https://example.com`
  - Used for **secure banking, logins, online shopping**.
 
![image](https://github.com/user-attachments/assets/e1a83795-672e-4073-9a51-858ec3cd95f9)


---

### **3. TLS 1.2 Handshake (Older Secure Communication Standard)**
- Used for HTTPS encryption.
- Steps:
  1. **Client Hello** → Client sends supported cipher suites & TLS version.
  2. **Server Hello** → Server picks a cipher suite & sends its certificate.
  3. **Key Exchange**:
     - Uses **RSA or Diffie-Hellman** to securely share keys.
  4. **Finished** → Both sides confirm encryption keys and secure communication starts.
- **Issues with TLS 1.2**:
  - **Slow handshake** due to multiple round trips.
  - **RSA vulnerabilities** (Less forward secrecy).
  - **More attack surface (e.g., BEAST, POODLE attacks)**.
  - 
![image](https://github.com/user-attachments/assets/35eb642c-26ea-4016-b727-a68d9c4c9cd1)



---

### **4. Diffie-Hellman Key Exchange (Used in TLS 1.2 & 1.3)**
- **Ensures secure key sharing over an untrusted network**.
- **Mathematical principle:**  
  - Both parties create a **shared secret key** without transmitting it directly.
  - Example:
    - Alice and Bob each choose a private number.
    - They exchange partial values and compute the same **shared secret**.
- **Advantages:**
  - Provides **Forward Secrecy** (A past session remains secure even if a key is stolen).
- **Example Usage:**  
  - **TLS with ephemeral Diffie-Hellman (DHE) for secure HTTPS connections**.
 
    ![image](https://github.com/user-attachments/assets/202f6aa1-151d-43cf-96ea-5dfd9f67e3a1)


---

### **5. TLS 1.3 (Improvements Over TLS 1.2)**
✅ **Faster Handshake**:  
- Reduces round trips from **2 → 1**, improving speed.  

✅ **Better Security**:  
- **Removes RSA key exchange**, only uses **Ephemeral Diffie-Hellman (ECDHE)** for **Forward Secrecy**.  

✅ **Removes Old Weak Ciphers**:  
- Eliminates **MD5, SHA-1, RC4**, reducing vulnerabilities.  

✅ **Zero Round Trip Time (0-RTT) Resumption**:  
- Allows **faster reconnections** by remembering previous sessions.  


![image](https://github.com/user-attachments/assets/f94be0a9-9612-4eb7-8e53-5636c82fb356)

---

### **Key Takeaways**
| Protocol | Encryption | Key Exchange | Speed |
|----------|------------|----------------|--------|
| **HTTP** | ❌ No Encryption | ❌ None | 🚀 Fast but **Not Secure** |
| **HTTPS (TLS 1.2)** | ✅ Yes | RSA, DH, ECDHE | ⏳ Slower (2 RTs) |
| **HTTPS (TLS 1.3)** | ✅ Yes | Only ECDHE | 🚀 Faster (1 RT) |

🔹 **TLS 1.3 is the fastest and most secure HTTPS protocol!** 🔒🚀  



---

#### **What is Mutual TLS (mTLS)?**  
- **Regular TLS** only checks if the website is real, but **mTLS** checks **both** sides—website and user.  
- It’s like a **double ID check** before entering a secure building.  

#### **Why is mTLS Important?**  
- It’s used when **both sides need to prove who they are** (like two businesses working together).  
- Example:  
  - In a **Kubernetes** application, different parts (microservices) talk to each other, and mTLS ensures **only trusted services communicate**.  
  - Helps follow **Zero Trust security**, meaning **no one is trusted by default**.  

---

### **How Does mTLS Work?**  
1. **User and server exchange certificates** (like ID cards).  
2. **Both verify each other’s certificates**.  
3. **Secure communication is established**.  

---

### **Why Use mTLS?**  
✅ **Stronger security** – Prevents unauthorized access.  
✅ **Prevents hacking** – Ensures only trusted devices/users can connect.  
✅ **Used in APIs & microservices** – Protects internal system communications.  

In short, **mTLS is like a VIP security check**—both parties prove their identity before talking! 🔒

---

![image](https://github.com/user-attachments/assets/47211ad3-c241-41d2-aea4-be9b240d8d19)

### **Easy Explanation of SSL/TLS Certificate Authentication**  

Whenever you visit a website like **Amazon**, your web browser (Chrome, Firefox, etc.) ensures that the website is **legitimate and secure** before exchanging data. This is done using **SSL/TLS certificates** issued by a **Certificate Authority (CA)**.  

#### **Step-by-Step Process:**  

✅ **Step 1: The Web Server Gets a Certificate**  
- Amazon applies for a certificate from a **Certificate Authority (CA)** (a trusted organization that verifies websites).  
- The CA verifies that Amazon **owns the domain** and then issues a **certificate**.  
- Amazon installs this certificate on its **web server**.  

✅ **Step 2: The Browser Verifies the Certificate**  
- When you try to visit Amazon, your **web browser checks the certificate** to ensure it is valid.  
- It verifies the certificate with the CA. If the certificate is **genuine**, the browser proceeds.  

✅ **Step 3: Secure Communication Begins**  
- Once verified, the browser and the server **establish an encrypted connection**.  
- All data exchanged (like login details, payment info) is **protected from hackers**.  

### **Why is This Important?**  
🔒 **Prevents fake websites** – Stops hackers from pretending to be Amazon.  
🔒 **Ensures encryption** – Protects sensitive data from being stolen.  
🔒 **Boosts trust** – A **padlock icon (🔒) in the browser** assures users they are on a secure site.  

**In short, SSL/TLS certificates help websites prove their identity and encrypt data, making the internet safer!** 🚀

![image](https://github.com/user-attachments/assets/3e8a3438-fa79-4e4f-93a1-cbde103f5a3e)

### **What happens while running below Command**

```
curl -vk https://www.jeeviacademy.com

```

1️⃣ **Client Initiates Request:**  
   - A browser (Chrome, Firefox) or an application (Python, JavaScript) **sends an HTTP request**.  
   - Example:  
     ```
     GET /index.html HTTP/1.1
     Host: jeeviacademy.com
     ```

2️⃣ **Server Processes Request:**  
   - The web server (Apache, Nginx, Node.js, etc.) **receives the request** and processes it.  
   - It may retrieve **static content (HTML, CSS, JS)** or interact with a **backend (database, API, etc.)**.

3️⃣ **Server Sends Response:**  
   - The server **returns an HTTP response** containing the requested data.  
   - Example Response:  
     ```
     HTTP/1.1 200 OK
     Content-Type: text/html
     Content-Length: 1234

     <html>
     
     ```

4️⃣ **Client Renders Response:**  
   - The client processes the response (renders an HTML page or processes JSON data).  
   - If needed, it **sends further requests** (e.g., for CSS, images, API calls).  

---
### **🔹 Web Server Examples**
| **Web Server** | **Type** | **Use Case** |
|---------------|---------|-------------|
| **Apache HTTP Server (IIS, Nginx, etc.)** | Static | Hosting websites, HTML, CSS, JS |
| **Tomcat** | Dynamic | Java-based web apps (JSP, Servlets) |
| **Node.js (Express.js)** | Dynamic | JavaScript-based APIs and web apps |
| **Django, Flask, Tornado (Python)** | Dynamic | Python-based web APIs |

---

### **🔹 Types of HTTP Communication**
| **Communication Type** | **Description** | **Example** |
|------------------------|---------------|------------|
| **Synchronous (Request-Response)** | Client waits for a response | Browser requesting a webpage |
| **Asynchronous (AJAX, WebSockets)** | Client continues execution while waiting | Real-time chat app |

---
