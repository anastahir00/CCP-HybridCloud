# Topology Documentation - Problem 8: Hybrid Cloud

**Team:** CCP HybridCloud Team
**Documentation Lead:** Salik Saeed
**Date:** May 21, 2026

## 📋 Table of Contents

1. [Network Overview](#1-network-overview)
2. [IP Addressing Plan](#2-ip-addressing-plan)
3. [Routing Table](#3-routing-table)
4. [Physical Topology Diagram](#4-physical-topology-diagram)
5. [Change Log](#5-change-log)
## 1. Network Overview

| Network | Subnet | Gateway | Description |
|---------|--------|---------|-------------|
| Cloud Network | 10.0.0.0/24 | 10.0.0.1 | Docker containers + Router WAN |
| On-Premise Network | 172.16.1.0/24 | 172.16.1.1 | Ubuntu VM + Management |

## 2. IP Addressing Plan

| Device | Interface | IP Address | Network |
|--------|-----------|------------|---------|
| Cisco Router | e0/0 | 10.0.0.1 | Cloud |
| Cisco Router | e0/1 | 172.16.1.1 | On-Premise |
| Ubuntu VM | eth0 | 172.16.1.10 | On-Premise |
| Docker Container | eth0 | 10.0.0.10 | Cloud |
| StrongSwan | eth0 | 10.0.0.10 | Cloud |
| Windows Host | vEthernet | 10.0.0.2 | Cloud |

## 3. Routing Table

| Destination | Next Hop | Interface | Type |
|-------------|----------|-----------|------|
| 10.0.0.0/24 | N/A | e0/0 | Connected |
| 172.16.1.0/24 | N/A | e0/1 | Connected |
| 0.0.0.0/0 | 10.0.0.10 | e0/0 | Default Static |

## 4. Physical Topology Diagram

Refer to: docs/week1/topology-diagram.pdf
---

## 5. Routing Table (Cisco Router)

| Destination | Subnet Mask | Next Hop | Interface | Type | Status |
|-------------|-------------|----------|-----------|------|--------|
| 10.0.0.0 | 255.255.255.0 | N/A | e0/0 | Connected | ACTIVE |
| 172.16.1.0 | 255.255.255.0 | N/A | e0/1 | Connected | ACTIVE |
| 0.0.0.0 | 0.0.0.0 | 10.0.0.10 | e0/0 | Static Default | ACTIVE |

---

## 6. Physical Topology Diagram

*Refer to `docs/week1/topology-diagram.pdf` for visual diagram.*

| File | Location |
|------|----------|
| Draw.io Source | `docs/week1/topology-diagram.drawio` |
| PDF Export | `docs/week1/topology-diagram.pdf` |

---

## 📌 Change Log

| Date | Author | Change |
|------|--------|--------|
| May 21, 2026 | Salik Saeed | Initial documentation created |
| | | |

---

*Documentation maintained by Documentation Lead - Salik Saeed*