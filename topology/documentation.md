\# Topology Documentation - Problem 8: Hybrid Cloud with IPsec



\*\*Team:\*\* CCP HybridCloud Team

\*\*Documentation Lead:\*\* Salik Saeed

\*\*Date:\*\* May 21, 2026



\---



\## Network Overview



| Network | Subnet | Gateway | Description |

|---------|--------|---------|-------------|

| On-Premise Network | 172.16.1.0/24 | 172.16.1.1 | GNS3 simulated environment |

| Cloud Network | 10.0.0.0/24 | 10.0.0.1 | Docker/LocalStack environment |

| IPsec Tunnel | - | - | Secure connection between both networks |



\---



\## Device Inventory



| Device | Role | Platform | Network |

|--------|------|----------|---------|

| Cisco Router | On-Premise Gateway | Cisco IOS (GNS3) | On-Premise |

| Ubuntu Server | On-Premise Server | Ubuntu 22.04 | On-Premise |

| StrongSwan | Cloud Gateway | StrongSwan (Docker) | Cloud |

| Docker Container | Cloud Server | Alpine/Ubuntu | Cloud |



\---



\## Interface Details



\### Cisco Router (On-Premise Gateway)



| Interface | IP Address | Subnet Mask | Connected To |

|-----------|------------|-------------|--------------|

| G0/0 | 172.16.1.1 | 255.255.255.0 | Ubuntu Server |

| G0/1 | 192.168.100.1 | 255.255.255.0 | StrongSwan (IPsec) |



\### Ubuntu Server (On-Premise)



| Interface | IP Address | Subnet Mask | Connected To |

|-----------|------------|-------------|--------------|

| eth0 | 172.16.1.10 | 255.255.255.0 | Cisco Router G0/0 |



\### StrongSwan Gateway (Cloud)



| Interface | IP Address | Subnet Mask | Connected To |

|-----------|------------|-------------|--------------|

| eth0 | 10.0.0.1 | 255.255.255.0 | Docker Container |

| eth1 | 192.168.100.2 | 255.255.255.0 | Cisco Router G0/1 |



\### Docker Container (Cloud Server)



| Interface | IP Address | Subnet Mask | Connected To |

|-----------|------------|-------------|--------------|

| eth0 | 10.0.0.10 | 255.255.255.0 | StrongSwan eth0 |



\---



\## IPsec Tunnel Details



| Parameter | Value |

|-----------|-------|

| Protocol | IPsec (IKEv2) |

| Authentication | Pre-shared Key (PSK) |

| Encryption | AES-256 |

| Hash | SHA-256 |

| Local Endpoint | 192.168.100.1 (Cisco Router) |

| Remote Endpoint | 192.168.100.2 (StrongSwan) |



\---



\## Connection Diagram



\---



\## Status



| Component | Status | Remarks |

|-----------|--------|---------|

| On-Premise Network | ✅ Configured | GNS3 ready |

| Cloud Network | ✅ Configured | Docker ready |

| IPsec Tunnel | 🔄 In Progress | Being configured by Talha |

| End-to-End Connectivity | ⏳ Pending | After IPsec completion |



\---



\## Sign-off



\*\*Salik Saeed\*\*  

Documentation Lead

