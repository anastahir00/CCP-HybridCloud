# Risk Assessment Matrix - Problem 8: Hybrid Cloud

| Risk ID | Risk Description | Probability | Impact | Mitigation Strategy | Owner |
|---------|-----------------|-------------|--------|---------------------|-------|
| R1 | Cisco router won't start (HAXM/KVM error) | High | High | Use Dynamips IOS router instead | Anas |
| R2 | Docker/LocalStack license required | Medium | Medium | Use Ubuntu container as cloud alternative | Talha |
| R3 | GNS3 Cloud can't see vEthernet | Medium | Low | Run GNS3 as Administrator | Anas |
| R4 | IPsec configuration fails | Medium | High | Test with simple ping first, then add encryption | Talha |
| R5 | Time constraint (5 weeks) | Medium | High | Prioritize core requirements | Anas |
| R6 | Team member unavailable | Low | Medium | Shared documentation on GitHub | All |
| R7 | Windows Firewall blocks traffic | Low | Medium | Temporarily disable for testing | Saim |