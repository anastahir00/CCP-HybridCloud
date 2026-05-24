# Security Engineer - Week 2 Documentation

**Role:** Security Engineer

**Name:** Muhammad Talha Bhatti

**Week:** Week 2

**Date:** May 24, 2026

**Status:** Complete

**Documentation By:** Salik Saeed

---

## Accomplishments

### 1. StrongSwan Installation

- **Software:** StrongSwan 5.9.5

- **Platform:** Ubuntu/Docker Container (WSL2)

- **Kernel:** Linux 6.6.114.1

### 2. IPsec Configuration (ipsec.conf)

- **Connection Name:** hybrid-cloud

- **Authentication:** PSK

- **Left (Cloud):** 10.0.0.10

- **Left Subnet:** 10.0.0.0/24

- **Right (On-Premise):** 172.16.1.1

- **Right Subnet:** 172.16.1.0/24

- **IKE:** aes256-sha256-modp2048

- **ESP:** aes256-sha256

**Full Configuration:**

config setup
    charondebug="ike 2, knl 2, cfg 2"

conn hybrid-cloud
    authby=secret
    left=10.0.0.10
    leftsubnet=10.0.0.0/24
    right=172.16.1.1
    rightsubnet=172.16.1.0/24
    ike=aes256-sha256-modp2048!
    esp=aes256-sha256!
    auto=start

### 3. IPsec PSK

10.0.0.10 172.16.1.1 : PSK "HybridCloud@2026"

### 4. StrongSwan Version

Linux strongSwan U5.9.5/K6.6.114.1

### 5. GitHub Files Created

- security/docs/ipsec-commands.md

- security/docs/strongswan-research.md

- security/docs/strongswan-setup.md

**Commit ID:** 8bfedbe

---

## Screenshots

1. strongswan-install.png - Installation process

2. ipsec-config.png - ipsec.conf content

3. ipsec-secrets.png - PSK configuration

4. github-push.png - GitHub push confirmation

**Location:** docs/week2/screenshots/security/

---

## Week 2 Summary

- StrongSwan installed: Done

- ipsec.conf configured: Done

- ipsec.secrets configured: Done

- GitHub push done: Done

---

## Next Steps

- Establish IPsec tunnel

- Verify tunnel with ipsec status

- Test connectivity

- Capture traffic in Wireshark

---

**Documentation by Salik Saeed**