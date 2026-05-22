\# 📄 Automation Lead - Week 2 Documentation



| \*\*Field\*\* | \*\*Details\*\* |

|-----------|-------------|

| \*\*Role\*\* | Automation Lead |

| \*\*Name\*\* | Nihaas Bhatti |

| \*\*Week\*\* | Week 2 |

| \*\*Date\*\* | May 22, 2026 |

| \*\*Status\*\* | ✅ Complete |

| \*\*Documentation By\*\* | Salik Saeed (Documentation Lead) |



\---



\## 📌 Overview



This document summarizes the work completed by \*\*Nihaas Bhatti\*\* (Automation Lead) during \*\*Week 2\*\* of the CCP-HybridCloud project.



\*\*Documented by:\*\* Salik Saeed



\---



\## ✅ Accomplishments



\### 1. Python Script: `test\_connectivity.py`



| Attribute | Description |

|-----------|-------------|

| \*\*Purpose\*\* | Test connectivity to all 5 devices in the hybrid cloud topology |

| \*\*Location\*\* | `scripts/test\_connectivity.py` |

| \*\*Language\*\* | Python 3.10.7 |



\### 2. Devices Tested



| # | Device Name | IP Address |

|---|-------------|------------|

| 1 | Windows Host (WSL) | `10.0.0.2` |

| 2 | Cisco Router WAN | `10.0.0.1` |

| 3 | Cisco Router LAN | `172.16.1.1` |

| 4 | Ubuntu VM | `172.16.1.10` |

| 5 | Docker Container | `10.0.0.10` |



\### 3. Python Libraries Installed



| Library | Version | Purpose |

|---------|---------|---------|

| `paramiko` | 4.0.0 | SSH connections to network devices |

| `netmiko` | 4.7.0 | Cisco device automation |

| `schedule` | 1.2.2 | Automated backup scheduling |

| `python-dotenv` | 1.2.2 | Secure password management |

| `requests` | 2.34.2 | API calls for cloud integration |

| `cryptography` | 48.0.0 | Encryption for secure communication |



\---



\## 🐍 Python Environment



| Component | Version |

|-----------|---------|

| Python | 3.10.7 |

| pip | 26.1.1 |



\---



\## 📦 Script Functionality



When `test\_connectivity.py` is executed, it performs the following:



1\. ✅ Sends \*\*2 ping requests\*\* to each device

2\. ✅ Checks if device \*\*responds\*\* (Reply from / bytes=)

3\. ✅ Displays \*\*status\*\* (☑ REACHABLE / ✗ NOT REACHABLE)

4\. ✅ Generates \*\*summary report\*\* (X/5 devices working)



\### Sample Output Format



