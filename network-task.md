

### 🟢 Phase 1: The Basics (Tasks 1-10)

*Focus: Understanding how computers talk and the physical/logical boundaries of networks.*

1. **The Definition:** Write a one-sentence definition of a "Network."
2. **Identify Yourself:** Run `hostname` and `hostname -I` on your machine.
3. **The Identifier:** Explain the difference between a **MAC Address** (Hardware) and an **IP Address** (Logical).
4. **Network Types:** List the use cases for PAN, LAN, MAN, and WAN.
5. **VPN Basics:** Explain how a VPN "tunnels" data through a public network.
6. **Topology Check:** Research and define a "Star Topology" vs. "Mesh Topology."
7. **The Internet:** Identify why the Internet is classified as a WAN.
8. **Network Media:** List three types of physical media (Fiber, Copper, Radio Waves).
9. **The Gateway:** Identify your router's IP address using `ip route | grep default`.
10. **The Ping:** Use `ping -c 4 8.8.8.8` to check basic internet reachability.

---

### 🧠 Phase 2: The Models (Tasks 11-25)

*Focus: Mastering the OSI 7-Layer and TCP/IP 4-Layer models.*

11. **OSI Order:** List the 7 layers of the OSI model from bottom to top.
12. **Layer 1:** Describe the function of the **Physical Layer**.
13. **Layer 2:** Identify your network interface's MAC address using `ip link show`.
14. **Layer 3:** Explain why the **Network Layer** is the "Routing" layer.
15. **Layer 4:** Contrast **TCP** (Reliable) vs. **UDP** (Fast) at the Transport Layer.
16. **Layer 7:** List 5 protocols that live at the **Application Layer**.
17. **TCP/IP Model:** List the 4 layers of the TCP/IP model.
18. **Mapping:** Create a table mapping OSI layers to TCP/IP layers.
19. **Encapsulation:** Describe how a "Segment" becomes a "Packet" and then a "Frame."
20. **PDU Identification:** What are the PDUs for Layers 2, 3, and 4? (Frame, Packet, Segment).
21. **The Handshake:** Diagram the TCP 3-Way Handshake (SYN, SYN-ACK, ACK).
22. **The Termination:** Research the 4-step process to close a TCP connection (FIN/ACK).
23. **Port Logic:** Identify which OSI layer "Ports" belong to.
24. **Checksums:** Explain how the Data Link layer detects errors in a frame.
25. **Protocol Data:** Use `ss -t` to see active TCP segments currently on your machine.

---

### 🌐 Phase 3: IP Addressing & Subnetting (Tasks 26-45)

*Focus: The "Math" of networking. Essential for VPC and Cloud setup.*

26. **IPv4 Anatomy:** Explain what the four "octets" in an IP address represent.
27. **Class System:** List the ranges for Class A, B, and C addresses.
28. **Private IPs:** List the three RFC 1918 private ranges (10.x, 172.16.x, 192.168.x).
29. **Subnet Masks:** Explain what a subnet mask does (Network vs. Host portion).
30. **CIDR Intro:** Convert `255.255.255.0` to CIDR notation (`/24`).
31. **Address Calculation:** How many total IPs are in a `/24`? (256).
32. **Usable IPs:** Why are there only 254 usable IPs in a `/24`? (Network & Broadcast).
33. **Network ID:** Identify the Network ID of `192.168.1.55/24`.
34. **Broadcast:** Identify the Broadcast address of `10.0.0.50/8`.
35. **Small Subnets:** Calculate the usable IPs in a `/30` (Common for point-to-point).
36. **VPC Planning:** Design a network with 4 subnets using `10.0.0.0/16`.
37. **Public IPs:** Check your public IP using `curl ifconfig.me`.
38. **NAT:** Explain why your laptop has a private IP but the internet sees a public one.
39. **IPv6:** Describe one major difference between IPv4 and IPv6.
40. **IPv6 Check:** Run `ip -6 addr` to see if your machine has a global IPv6.
41. **Loopback:** Ping your own machine using `ping 127.0.0.1`.
42. **APIPA:** Research what a `169.254.x.x` address means (DHCP failure).
43. **DHCP Process:** Define the DORA process (Discover, Offer, Request, Acknowledge).
44. **Static IP:** Research how to set a static IP on a Linux server.
45. **Subnetting Tool:** Install and use `ipcalc` to verify a subnet: `ipcalc 192.168.1.0/26`.

---

### 🛣️ Phase 4: Routing & DNS (Tasks 46-65)

*Focus: How data finds its way across the globe.*

46. **The Router:** Define a router's job in 10 words or less.
47. **Routing Table:** View your kernel routing table using `ip route`.
48. **Static Route:** Research the command to manually add a route to a specific IP.
49. **Default Route:** Identify the "0.0.0.0/0" route and its importance.
50. **Hop Count:** Use `traceroute google.com` to see the "hops" to the destination.
51. **DNS Definition:** Explain why DNS is the "Phonebook of the Internet."
52. **Root Servers:** Research what the "Root DNS Servers" are.
53. **The Resolver:** Find your current DNS server: `cat /etc/resolv.conf`.
54. **A Records:** Use `dig google.com` to find an A record.
55. **CNAME:** Research what a CNAME (Canonical Name) is used for.
56. **MX Records:** Find the mail servers for a domain: `dig google.com MX`.
57. **TTL:** Explain what "Time to Live" means in a DNS record.
58. **Reverse DNS:** Use `dig -x 8.8.8.8` to find the hostname of an IP.
59. **Propogation:** Explain why DNS changes can take up to 48 hours.
60. **Local Hosts:** Edit your `/etc/hosts` file to map `test.local` to `127.0.0.1`.
61. **BGP:** Research the "Border Gateway Protocol" (The routing protocol of the Internet).
62. **AS Numbers:** Define an "Autonomous System" (AS).
63. **Anycast:** Briefly explain how one IP can exist in multiple global locations.
64. **DNSSEC:** Research how DNSSEC adds security to DNS lookups.
65. **Public Resolvers:** List the IPs for Google DNS and Cloudflare DNS.

---

### ⚡ Phase 5: Protocols & Ports (Tasks 66-85)

*Focus: The "Language" of services.*

66. **Standard Ports:** Memorize: SSH (22), HTTP (80), HTTPS (443), DNS (53).
67. **Database Ports:** Memorize: MySQL (3306), Postgres (5432), Redis (6379).
68. **Checking Ports:** Use `ss -tuln` to see all listening ports on your machine.
69. **Telnet/NC:** Use `nc -zv google.com 443` to check if a port is open.
70. **HTTP Methods:** List the purpose of GET, POST, PUT, and DELETE.
71. **Status Codes:** What do 200, 404, and 500 mean?
72. **Headers:** Use `curl -I https://google.com` to view HTTP response headers.
73. **HTTPS:** Explain the role of SSL/TLS in securing port 443.
74. **SSH:** Use `ssh-keygen` to generate a key pair.
75. **FTP:** Explain why FTP is considered insecure compared to SFTP.
76. **SMTP:** Identify the port used for sending email (25 or 587).
77. **ICMP:** Identify which tool uses ICMP (Hint: Ping).
78. **ARP:** Run `arp -a` to see the IP-to-MAC mapping on your local network.
79. **NTP:** Explain why "Network Time Protocol" is vital for log synchronization.
80. **SNMP:** Research how SNMP is used for infrastructure monitoring.
81. **WebSocket:** Contrast a standard HTTP request with a WebSocket connection.
82. **gRPC:** Research why microservices use gRPC instead of REST/HTTP.
83. **Load Balancing:** Explain the difference between L4 (Transport) and L7 (Application) load balancing.
84. **Keep-Alive:** What is an HTTP Keep-Alive header?
85. **Sticky Sessions:** Explain "Session Persistence" in load balancing.

---

### 🛡️ Phase 6: Security & Troubleshooting (Tasks 86-100)

*Focus: Fixing things when they break and keeping hackers out.*

86. **Firewalls:** List the difference between a Stateless and Stateful firewall.
87. **UFW/Iptables:** Use `sudo ufw status` to check your Linux firewall.
88. **Security Groups:** Research how AWS Security Groups differ from a standard firewall.
89. **DDoS:** Define a Distributed Denial of Service attack.
90. **Packet Capture:** Use `sudo tcpdump -i any -c 5` to sniff 5 packets.
91. **Wireshark:** Download Wireshark and open a sample `.pcap` file.
92. **Latency:** Define "Round Trip Time" (RTT).
93. **Jitter:** Research how jitter affects VoIP and Video streaming.
94. **Packet Loss:** List two common causes of packet loss.
95. **The MTU:** Research "Maximum Transmission Unit" and why fragmentation is bad.
96. **Port Scanning:** Use `nmap localhost` to scan your own machine for open ports.
97. **Intrusion Detection:** Research the difference between an IDS and an IPS.
98. **Zero Trust:** Briefly explain the "Never Trust, Always Verify" networking philosophy.
99. **Cloud Networking:** Define a VPC (Virtual Private Cloud).
100. **The DevOps Goal:** Write a paragraph on how networking knowledge helps you automate infrastructure.

---
