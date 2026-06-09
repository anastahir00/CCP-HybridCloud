# Week 3 Status Report - Problem 8: Hybrid Cloud

**Date:** June 10, 2026
**Week:** 3 of 5

## Accomplishments

### Security Engineer (Talha's tasks - done by Anas)
- ✅ StrongSwan 5.9.5 installed on Docker container (10.0.0.10)
- ✅ `ipsec.conf` configured for IKEv1 with AES256/SHA256
- ✅ `ipsec.secrets` configured with pre-shared key
- ✅ StrongSwan service running and listening

### Network Architect (Anas's tasks)
- ✅ ISAKMP policy configured (AES256, SHA256, DH14)
- ✅ Pre-shared key configured
- ✅ Transform set ESP-AES-SHA configured
- ✅ Crypto map applied to FastEthernet2/0
- ✅ Access list 100 defines traffic to encrypt (172.16.1.0/24 → 10.0.0.0/24)

### Testing/QA (Saim's tasks - done by Anas)
- ✅ Wireshark capture attempted on vEthernet (WSL)
- ✅ Filter `isakmp || esp` applied
- ✅ PCAP file saved (`week3-esp-capture.pcap`)
- ✅ Screenshot taken (`wireshark-no-isakmp-or-esp.png`)

## Issues / Limitations

### Platform Limitation - Hyper-V Internal Switch
The IPsec tunnel cannot fully establish due to Windows/Hyper-V networking limitations:

**Problem:** Docker container (10.0.0.10) and GNS3 router (10.0.0.1) cannot exchange IKE packets (UDP 500/4500) because the Hyper-V internal switch blocks traffic between Docker and GNS3 Cloud node.

**Evidence:**
- Router `show crypto isakmp sa` shows `MM_NO_STATE` (no Phase 1 completion)
- StrongSwan `ipsec statusall` shows `CONNECTING` indefinitely
- Wireshark shows no ISAKMP or ESP packets

**Conclusion:** Both sides are correctly configured. The tunnel is blocked by Windows platform, not configuration error.

## Screenshots Saved
- `router-isakmp-sa.png` - Shows MM_NO_STATE
- `router-ipsec-sa.png` - Shows 0 encapsulated packets
- `router-crypto-map.png` - Crypto map configuration
- `router-access-list.png` - Access list 100
- `strongswan-status.png` - StrongSwan CONNECTING state
- `wireshark-no-isakmp-or-esp.png` - No ESP packets captured

## Config Files Saved
- `ipsec.conf` - StrongSwan configuration
- `ipsec.secrets` - Pre-shared key
- `router-crypto-config.txt` - Router crypto section

## Week 3 Deliverables Status
| Deliverable | Status |
|-------------|--------|
| StrongSwan installed | ✅ |
| Router crypto map | ✅ |
| ISAKMP/IPSEC screenshots | ✅ |
| Wireshark capture | ✅ (no ESP due to limitation) |
| PCAP file | ✅ |
| Documentation | ✅ |

## Next Week Goals (Week 4)
- NAT configuration
- QoS / rate limiting
- Performance testing (iPerf)
- Backup automation script