# IP Addressing Plan - Problem 8: Hybrid Cloud

**Prepared by:** Muhammad Anas Tahir (Project Lead + Network Architect)
**Date:** May 19, 2026

## Network Subnets

| Network Name | Subnet | CIDR | Gateway | Purpose |
|--------------|--------|------|---------|---------|
| Cloud Network | 10.0.0.0 - 10.0.0.255 | /24 | 10.0.0.1 | Docker containers + Router WAN |
| On-Premise Network | 172.16.1.0 - 172.16.1.255 | /24 | 172.16.1.1 | Ubuntu VM (on-premise server) |

## Device IP Allocation

| Device | Interface | IP Address | Subnet | Gateway |
|--------|-----------|------------|--------|---------|
| Windows Host | vEthernet (WSL) | 10.0.0.2 | 255.255.255.0 | N/A |
| Cisco Router | e0/0 (WAN) | 10.0.0.1 | 255.255.255.0 | 10.0.0.1 |
| Cisco Router | e0/1 (LAN) | 172.16.1.1 | 255.255.255.0 | N/A |
| Ubuntu VM (On-Premise) | eth0 | 172.16.1.10 | 255.255.255.0 | 172.16.1.1 |
| Docker Cloud Container | eth0 | 10.0.0.10 | 255.255.255.0 | 10.0.0.1 |

## Routing Table (Cisco Router)

| Destination | Subnet Mask | Next Hop | Interface | Type |
|-------------|-------------|----------|-----------|------|
| 10.0.0.0 | 255.255.255.0 | N/A | e0/0 | Connected |
| 172.16.1.0 | 255.255.255.0 | N/A | e0/1 | Connected |
| 0.0.0.0 | 0.0.0.0 | 10.0.0.10 | e0/0 | Default Static |