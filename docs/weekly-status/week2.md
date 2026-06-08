# Week 2 Status Report - Problem 8: Hybrid Cloud

**Date:** June 8, 2026
**Team:** CCP-HybridCloud
**Week:** 2 of 5

---

## 📊 Overall Status

| Metric | Status |
|--------|--------|
| Overall Progress | 40% |
| On Track? | ✅ Yes |
| Week 2 Completion | 100% |

---

## ✅ Accomplishments (Week 2)

### Anas (Project Lead + Network Architect)
- [x] GNS3 topology built (Router + Cloud + Ubuntu VM)
- [x] Cisco router configured (10.0.0.1, 172.16.1.1)
- [x] Ubuntu VM created and configured (172.16.1.10)
- [x] Router ↔ Ubuntu ping successful (0% loss)
- [x] Running config saved and pushed to GitHub
- [x] GNS3 project uploaded to Google Drive

### Talha (Security Engineer)
- [x] StrongSwan research completed
- [x] IPsec configuration templates prepared
- [x] Security screenshots added to GitHub

### Nihaas (Automation Lead)
- [x] GitHub repository structured
- [x] `test_connectivity.py` script created
- [x] Script pushed to `scripts/` folder

### Saim (Testing/QA Engineer)
- [x] Docker container running (10.0.0.10)
- [x] Container → Router ping successful
- [x] Wireshark PCAP captured and saved
- [x] SSH service enabled on Ubuntu

### Salik (Documentation Lead)
- [x] Week 2 status report created
- [x] Documentation compiled
- [x] All deliverables organized

---

## 📋 Week 2 Deliverables Status

| Deliverable | Status | Location |
|-------------|--------|----------|
| GNS3 topology file | ✅ | Google Drive link in README |
| Router running config | ✅ | `docs/week2/running-config.txt` |
| Router interfaces screenshot | ✅ | `docs/week2/screenshots/` |
| Ubuntu → Router ping | ✅ | `docs/week2/screenshots/` |
| Router → Ubuntu ping | ✅ | `docs/week2/screenshots/` |
| Container → Router ping | ✅ | `docs/week2/screenshots/` |
| Docker container proof | ✅ | `docs/week2/screenshots/` |
| SSH status proof | ✅ | `docs/week2/screenshots/` |
| Wireshark PCAP | ✅ | `pcaps/week2-capture.pcap` |
| Ping test results | ✅ | `docs/week2/ping-test-results.txt` |
| Week 2 status report | ✅ | `docs/weekly-status/week2.md` |

---

## ⚠️ Issues / Blockers

| Issue | Status | Resolution |
|-------|--------|------------|
| GNS3 file too large for GitHub | ✅ Resolved | Uploaded to Google Drive |
| Router → Docker ping blocked | ✅ Documented | Hyper-V isolation limitation |
| SSH login from Windows timeout | ✅ Documented | Network isolation, service active |

---

## 📅 Week 3 Goals

| Task | Owner |
|------|-------|
| Configure IPsec on Cisco router | Anas |
| Set up StrongSwan on cloud | Talha |
| Verify `show crypto ipsec sa` | Anas + Talha |
| Capture ESP packets in Wireshark | Saim |
| Update automation scripts | Nihaas |
| Prepare Week 3 status report | Salik |

---

## 📁 GitHub Repository

🔗 https://github.com/anastahir00/CCP-HybridCloud

---

## ✍️ Sign-off

| Role | Name | Status |
|------|------|--------|
| Project Lead + Network Architect | Muhammad Anas Tahir | ✅ |
| Security Engineer | Muhammad Talha Bhatti | ✅ |
| Automation Lead | Muhammad Nihaas Bhatti | ✅ |
| Testing/QA Engineer | Saim Ullah | ✅ |
| Documentation Lead | Salik Saeed | ✅ |

---

**Week 2 Complete!** 🎉