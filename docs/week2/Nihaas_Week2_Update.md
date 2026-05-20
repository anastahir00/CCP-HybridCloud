\# Week 2 Status - Nihaas (Automation Lead)

\*\*Date:\*\* May 20, 2026

\*\*Project:\*\* CCP HybridCloud - Problem 8



\## ✅ Completed this week:

\- \[x] Created connectivity verification script (`test\_connectivity.py`)

\- \[x] Script ready to test all 5 devices from IP plan

\- \[x] GitHub folder structure updated with `docs/week2/`

\- \[x] Successfully pushed code to repository



\## 🔄 In progress:

\- \[ ] Python backup script template (carry over from Week 1)



\## 📋 For Week 3:

\- Complete backup script with scheduling

\- Add automated config backup for Cisco router

\- Integrate with GNS3 once topology is ready



\## ⚠️ Blockers / Dependencies:

\- Waiting for Anas to complete GNS3 topology (HAXM error)

\- Cannot test connectivity until router and VMs are running



\## 📊 Connectivity Test Script Status:

| Device | IP | Script Ready |

|--------|-----|---------------|

| Windows Host (WSL) | 10.0.0.2 | ✅ |

| Cisco Router WAN | 10.0.0.1 | ✅ |

| Cisco Router LAN | 172.16.1.1 | ✅ |

| Ubuntu VM | 172.16.1.10 | ✅ |

| Docker Container | 10.0.0.10 | ✅ |



\## 💬 Notes for Team:

\- Script is ready - will test immediately when GNS3 is running

\- Run `python test\_connectivity.py` after each topology change

\- All 5 devices from IP plan are included

