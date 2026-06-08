# ☁️ CCP HybridCloud - Problem 8

**Computer Networks Project** — Hybrid Cloud connecting on-premise network to cloud via IPsec VPN tunnel.

---

## 👥 Team Members

| Role | Name | ID |
|------|------|-----|
| Project Lead + Network Architect | Muhammad Anas Tahir | F2024266985 |
| Security Engineer | Muhammad Talha Bhatti | F2024266503 |
| Automation Lead | Muhammad Nihaas Bhatti | F2024266196 |
| Testing/QA Engineer | Saim Ullah | F2024266594 |
| Documentation Lead | Salik Saeed | F2024266596 |

---

## 🎯 Project Overview

Hybrid Cloud connecting **on-premise network (GNS3)** to **cloud (Docker)** via **IPsec tunnel**.

---

## 🌐 Network Topology

| Network | Type | Subnet | Platform |
|---------|------|--------|----------|
| On-Premise | Local | 172.16.1.0/24 | Ubuntu Server (GNS3) |
| Cloud | Remote | 10.0.0.0/24 | Docker container |
| Tunnel | IPsec | Between Cisco router and StrongSwan gateway | — |

---

## 📁 Repository Structure
```
CCP-HybridCloud/
├── docs/ # Architecture, IP plans, weekly reports
├── src/ # Scripts and automation code
│ └── scripts/ # Python automation scripts
├── pcaps/ # Wireshark packet captures
├── security/ # Security documentation and configs
├── assets/ # Diagrams and screenshots
├── README.md # This file
└── .gitignore # Git ignore rules
```
---

## 🚀 Technologies Used

| Technology | Purpose |
|------------|---------|
| GNS3 | Network simulation (on-premise) |
| Docker | Cloud environment |
| StrongSwan / IPsec | VPN tunnel |
| Wireshark | Packet analysis |
| Python | Connectivity testing |

---

## 📅 Weekly Progress

| Week | Focus | Status |
|------|-------|--------|
| 1 | Requirements & Topology Design | ✅ Complete |
| 2 | GNS3 Implementation & Connectivity | ✅ Complete |
| 3 | Security & IPsec | 🔄 In Progress |
| 4 | Advanced Features & Integration | ⏳ Pending |
| 5 | Final Report & Video | ⏳ Pending |

---

## 🔧 How to Run / Test

### Prerequisites
- GNS3 installed
- Docker installed
- Wireshark for packet capture

### Steps
1. Clone the repository
2. Review IP plan in `docs/ip-plan/`
3. Launch GNS3 topology
4. Run connectivity tests:
   ```bash
   python src/scripts/test_connectivity.py

📄 License
MIT — free to use, modify, and distribute

---

## What I Added

| Section | Why |
|---------|-----|
| **Table for Network Topology** | Clear visualization |
| **Repository Structure** | Shows organization |
| **Technologies Table** | Lists tools used |
| **Weekly Progress Table** | Shows project status |
| **How to Run** | Instructions for others |
| **Badges (optional)** | Professional look |

---
