\# 🔒 Security Engineer - Week 2 Documentation



| \*\*Field\*\* | \*\*Details\*\* |

|-----------|-------------|

| \*\*Role\*\* | Security Engineer |

| \*\*Name\*\* | Muhammad Talha Bhatti |

| \*\*Week\*\* | Week 2 |

| \*\*Date\*\* | May 24, 2026 |

| \*\*Status\*\* | ✅ Complete |

| \*\*Documentation By\*\* | Salik Saeed (Documentation Lead) |



\---



\## 📌 Overview



This document summarizes the work completed by \*\*Muhammad Talha Bhatti\*\* (Security Engineer) during \*\*Week 2\*\* of the CCP-HybridCloud project.



\*\*Documented by:\*\* Salik Saeed



\---



\## ✅ Accomplishments



\### 1. StrongSwan Installation



| Attribute | Details |

|-----------|---------|

| \*\*Software\*\* | StrongSwan 5.9.5 |

| \*\*Platform\*\* | Ubuntu/Docker Container (WSL2) |

| \*\*Kernel\*\* | Linux 6.6.114.1-microsoft-standard-WSL2 |



\### 2. IPsec Configuration: `ipsec.conf`



| Parameter | Value |

|-----------|-------|

| Connection Name | `hybrid-cloud` |

| Authentication | `secret` (PSK) |

| Left (Cloud) | `10.0.0.10` |

| Left Subnet | `10.0.0.0/24` |

| Right (On-Premise) | `172.16.1.1` |

| Right Subnet | `172.16.1.0/24` |

| IKE | `aes256-sha256-modp2048` |

| ESP | `aes256-sha256` |

| Auto Start | `start` |



\*\*Full Configuration:\*\*

```bash

config setup

&#x20;   charondebug="ike 2, knl 2, cfg 2"



conn hybrid-cloud

&#x20;   authby=secret

&#x20;   left=10.0.0.10

&#x20;   leftsubnet=10.0.0.0/24

&#x20;   right=172.16.1.1

&#x20;   rightsubnet=172.16.1.0/24

&#x20;   ike=aes256-sha256-modp2048!

&#x20;   esp=aes256-sha256!

&#x20;   keyingtriess=%forever

&#x20;   auto=start



\### 3. ipsec.secrets (PSK)

10.0.0.10 172.16.1.1 : PSK "HybridCloud@2026"





\### 4. StrongSwan Version



\### 5. GitHub Documentation Files Created



| File | Description |

|------|-------------|

| security/docs/ipsec-commands.md | IPsec commands reference |

| security/docs/strongswan-research.md | StrongSwan research documentation |

| security/docs/strongswan-setup.md | Complete setup guide |



\*\*GitHub Commit:\*\*

\- Commit ID: `8bfedbe`

\- Message: "Add Security Engineer Week 2: Documentation files"

\- Changes: 3 files, 78 insertions(+)



\---



\## 📸 Screenshots



| # | Screenshot Name | Description |

|---|----------------|-------------|

| 1 | `strongswan-install.png` | StrongSwan installation process |

| 2 | `ipsec-config.png` | ipsec.conf file content |

| 3 | `ipsec-secrets.png` | ipsec.secrets PSK configuration |

| 4 | `github-push.png` | GitHub push confirmation |



\*\*Location:\*\* `docs/week2/screenshots/security/`



\---



\## 📊 Week 2 Summary



| Task | Status |

|------|--------|

| StrongSwan installed | ✅ Done |

| ipsec.conf configured | ✅ Done |

| ipsec.secrets (PSK) configured | ✅ Done |

| StrongSwan version verified | ✅ Done |

| GitHub documentation pushed | ✅ Done |

| Screenshots captured | ✅ Done |



\---



\## 🔗 Next Steps (Week 3)



| Task | Owner |

|------|-------|

| Establish IPsec tunnel between Cisco router and StrongSwan | Talha |

| Verify tunnel with ipsec status | Talha |

| Test end-to-end connectivity | Saim |

| Capture encrypted traffic in Wireshark | Saim |



\---



\## ✍️ Sign-off



| Documented By | Salik Saeed (Documentation Lead) |

| Date | May 24, 2026 |

| Team | CCP-HybridCloud |



\---



> \*This document is part of Week 2 deliverables for the CCP-HybridCloud project.\*



\*\*Documentation completed by Salik Saeed\*\*

