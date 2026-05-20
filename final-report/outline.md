\# Final Report Outline - Problem 8: Hybrid Cloud with IPsec



\*\*Team:\*\* CCP HybridCloud Team  

\*\*Documentation Lead:\*\* Salik Saeed  

\*\*Total Pages:\*\* 15-20  



\---



\## 1. Introduction (2 pages)



\### 1.1 Project Background

\- Hybrid cloud concept

\- Need for secure connectivity

\- IPsec as VPN solution



\### 1.2 Problem Statement

\- Connect on-premise (GNS3) to cloud (Docker)

\- Establish secure IPsec tunnel



\### 1.3 Objectives

\- Design hybrid cloud topology

\- Implement IPsec tunnel

\- Verify end-to-end connectivity



\### 1.4 Team Roles \& Responsibilities



| Role | Name | Responsibilities |

|------|------|------------------|

| Project Lead + Network Architect | Anas Tahir | Topology, IP addressing, GNS3 |

| Security Engineer | Talha Bhatti | IPsec, StrongSwan, security |

| Automation Lead | Nihaas Bhatti | Scripts, GitHub management |

| Testing/QA Engineer | Saim Ullah | Testing, validation, PCAP |

| Documentation Lead | Salik Saeed | Reports, diagrams, video |



\---



\## 2. Requirements Analysis (1.5 pages)



\### 2.1 Network Requirements

\- On-premise network: 172.16.1.0/24

\- Cloud network: 10.0.0.0/24

\- IPsec tunnel between both



\### 2.2 Tools \& Technologies Used



| Tool | Purpose |

|------|---------|

| GNS3 | Network simulation |

| Docker | Cloud simulation |

| StrongSwan | IPsec gateway |

| Ubuntu Server | On-premise server |

| Wireshark | Packet capture |

| iPerf3 | Performance testing |



\---



\## 3. Topology Design (2 pages)



\### 3.1 Logical Topology Diagram

\- Diagram with all devices and connections



\### 3.2 IP Addressing Plan



| Device | Interface | IP Address |

|--------|-----------|------------|

| Cisco Router | G0/0 | 172.16.1.1/24 |

| Ubuntu Server | eth0 | 172.16.1.10/24 |

| StrongSwan | eth0 | 10.0.0.1/24 |

| Docker Container | eth0 | 10.0.0.10/24 |



\### 3.3 Device Inventory

\- Hardware/software specifications



\---



\## 4. Implementation (4 pages)



\### 4.1 GNS3 Setup

\- Installation steps

\- Topology creation

\- Device configuration



\### 4.2 On-Premise Configuration

\- Cisco router basic config

\- Ubuntu server setup



\### 4.3 Cloud Configuration

\- Docker network setup

\- StrongSwan installation



\### 4.4 IPsec Tunnel Configuration

\- StrongSwan ipsec.conf

\- Cisco router crypto map

\- PSK configuration



\### 4.5 Automation Script (if any)

\- Python backup script

\- GitHub integration



\---



\## 5. Testing \& Validation (2 pages)



\### 5.1 Test Plan



| Test Case | Expected Result | Status |

|-----------|-----------------|--------|

| Ping on-premise to cloud | Success | ⏳ |

| IPsec SA verification | Established | ⏳ |

| Wireshark packet capture | Encrypted packets | ⏳ |

| Performance test | Throughput measured | ⏳ |



\### 5.2 Test Results

\- Ping test matrix

\- IPsec status output

\- Screenshots



\---



\## 6. Challenges \& Solutions (1.5 pages)



\### 6.1 Issues Faced



| Challenge | Solution |

|-----------|----------|

| Docker-GNS3 bridge connectivity | Configured vEthernet adapter |

| IPsec tunnel not establishing | Checked PSK and peer IPs |



\### 6.2 Troubleshooting Steps

\- Debug commands used

\- Logs analysis



\---



\## 7. Conclusion (1 page)



\### 7.1 Summary of Achievements

\- Hybrid cloud connected

\- IPsec tunnel established

\- End-to-end working



\### 7.2 Future Improvements

\- Add redundancy

\- Automate deployment



\---



\## 8. References \& Appendices (2-3 pages)



\### 8.1 Running-Configs

\- Cisco router full config

\- StrongSwan ipsec.conf



\### 8.2 Screenshots

\- GNS3 topology

\- Ping test results

\- IPsec SA output

\- Wireshark capture



\### 8.3 PCAP Files (if available)

\- Pre-IPsec traffic

\- Post-IPsec encrypted traffic



\---



\## References



\- GNS3 Documentation: https://docs.gns3.com/

\- StrongSwan Wiki: https://wiki.strongswan.org/

\- Cisco IPsec Configuration Guide

\- Docker Network Documentation



\---



\## Document Version Control



| Version | Date | Author | Changes |

|---------|------|--------|---------|

| 1.0 | May 21, 2026 | Salik Saeed | Initial outline |



\---



\## Sign-off



\*\*Salik Saeed\*\*  

Documentation Lead



