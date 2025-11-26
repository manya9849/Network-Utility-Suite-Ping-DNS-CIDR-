# 🌐 Network Access & Utility Suite (Ping, DNS, CIDR)

A modern, full-stack network analysis toolkit built with **Flask (Python)** and a **premium Tailwind CSS frontend**.  
This project provides three essential networking utilities in a single dashboard:

- **Ping Tester** – Check host reachability & latency  
- **DNS Resolver** – Convert domain names into IP addresses  
- **CIDR Subnet Calculator** – Breakdown network ranges & subnet details  

Designed for computer networks mini-projects, diagnostics, demos, and educational use.

---

## 🚀 Features

###  Ping Tester
- Tests reachability using ICMP
- Displays latency, packet loss, RTT statistics
- Supports both domain names and IP addresses
- Works on Windows & Linux (auto-detects OS)

###  DNS Resolver
- Converts domains to IPv4 addresses
- Uses system DNS resolver
- Handles invalid domains gracefully

###  CIDR Subnet Calculator
- Parses IPv4 CIDR (e.g., `192.168.1.0/24`)
- Displays:
  - Network address
  - Broadcast address
  - Total number of addresses
  - First & Last usable hosts
- Validates input and returns detailed JSON

###  Frontend (Tailwind CSS)
- Premium glass-UI design
- Fully responsive layout
- Smooth hover effects
- Monospace technical output sections

---

## 🖥️ Tech Stack

| Component | Technology |
|----------|------------|
| **Backend** | Python, Flask |
| **Frontend** | HTML, Tailwind CSS, JavaScript |
| **Network Utilities** | `socket`, `subprocess`, `ipaddress` |
| **Platform Support** | Windows, Linux, macOS |

---

## 📂 Project Structure

│── app.py # Flask backend
│── static/
│ └── index.html # Main dashboard UI
│── templates/ (optional)
│── requirements.txt
│── README.md
└── .gitignore

## 🧪 Example Inputs for Testing
Ping

8.8.8.8
google.com
10.255.255.1 (should fail)

DNS

openai.com
youtube.com
invalid.domain.xyz (fail)

CIDR

192.168.1.0/24
10.0.0.0/8
192.168.1.0/30

## 📸 Screenshots

<img width="1920" height="1020" alt="Screenshot 2025-11-26 185245" src="https://github.com/user-attachments/assets/6bd8c945-7bc2-4c20-ada9-b56eb9854f02" />

<img width="1920" height="1020" alt="Screenshot 2025-11-26 185341" src="https://github.com/user-attachments/assets/b2415218-b385-4210-a8be-7ba316a43ec8" />

## 🙌 Author

 KM Manya Muthamma
 
Computer Networks Mini Project

Network Access & Utility Suite (2025)
