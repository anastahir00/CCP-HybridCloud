# Week 2 Status Report
## Automation Lead: Nihaas

| | |
|---|---|
| **Date** | May 20, 2026 |
| **Project** | CCP HybridCloud - Problem 8 |
| **Role** | Automation Lead |

---

## 📌 Executive Summary

> Connectivity test script completed and pushed to GitHub. Ready to test once GNS3 topology is available. Backup script template pending from Week 1 will be completed in Week 3.

---

## ✅ Completed Tasks (Week 2)

| # | Task | Status |
|---|------|--------|
| 1 | Create connectivity verification script (`test_connectivity.py`) | ✓ Done |
| 2 | Include all 5 devices from IP addressing plan | ✓ Done |
| 3 | Create `docs/week2/` folder structure | ✓ Done |
| 4 | Push code and documentation to GitHub repository | ✓ Done |

---

## 🔄 In Progress / Carry Over

| Task | Original Week | Expected Completion |
|------|---------------|---------------------|
| Python backup script template | Week 1 | Week 3 |

---

## 📅 Week 3 Commitments

| Task | Priority |
|------|----------|
| Complete backup script with automated scheduling | High |
| Add automatic configuration backup for Cisco router | High |
| Integrate and test scripts with GNS3 topology | Medium |

---

## ⚠️ Blockers & Dependencies

| Blocker | Owner | Impact |
|---------|-------|--------|
| GNS3 topology incomplete | Anas | Cannot test connectivity script |
| Cisco router HAXM error | Anas | Prevents all router-related testing |

> **Note:** All testing is currently blocked until GNS3 environment is operational.

---

## 📊 Connectivity Test Coverage

| Device Name | IP Address | Script Status |
|-------------|------------|---------------|
| Windows Host (WSL) | 10.0.0.2 | ✅ Ready |
| Cisco Router (WAN) | 10.0.0.1 | ✅ Ready |
| Cisco Router (LAN) | 172.16.1.1 | ✅ Ready |
| Ubuntu VM | 172.16.1.10 | ✅ Ready |
| Docker Container | 10.0.0.10 | ✅ Ready |

**Coverage:** 5/5 devices (100%)

---

## 📝 Team Notes

| Action Item | Details |
|-------------|---------|
| **When to test** | Immediately after GNS3 is running |
| **How to test** | Run `python test_connectivity.py` |
| **Testing frequency** | After each topology change |
| **Script location** | Repository root folder |

---

## ✅ Sign Off

| Role | Name | Status |
|------|------|--------|
| Automation Lead | Nihaas | ✅ Week 2 Complete |

---

**End of Report**
