\# Video Demonstration Script - Problem 8: Hybrid Cloud with IPsec



\*\*Team:\*\* CCP HybridCloud Team  

\*\*Script Writer:\*\* Salik Saeed (Documentation Lead)  

\*\*Total Duration:\*\* 8-10 minutes  

\*\*Narrated by:\*\* \[Team Member Name]



\---



\## Scene 1: Introduction (1 minute)



\*\*Visual:\*\* Team intro slide + Project title



\*\*Narration:\*\*

> "Hello, we are the CCP HybridCloud Team. Our project is Problem 8: Hybrid Cloud with IPsec. 

> We have 5 team members: Anas (Project Lead), Talha (Security Engineer), Nihaas (Automation Lead), 

> Saim (Testing Engineer), and myself Salik (Documentation Lead)."



\*\*Visual:\*\* Problem statement slide



\*\*Narration:\*\*

> "The goal is to connect an on-premise network simulated in GNS3 to a cloud network simulated in Docker, 

> using a secure IPsec tunnel."



\---



\## Scene 2: Topology Overview (1.5 minutes)



\*\*Visual:\*\* Logical topology diagram



\*\*Narration:\*\*

> "Our topology consists of two main networks. On the on-premise side, we have a Cisco router and an Ubuntu server 

> in the 172.16.1.0/24 subnet. On the cloud side, we have a StrongSwan gateway and a Docker container 

> in the 10.0.0.0/24 subnet. Both are connected via an IPsec tunnel."



\*\*Visual:\*\* Point to each device in diagram



\*\*Narration:\*\*

> "The Cisco router acts as the on-premise gateway. The StrongSwan container acts as the cloud gateway. 

> The IPsec tunnel provides encryption for all traffic between these two networks."



\---



\## Scene 3: Implementation Highlights (2 minutes)



\*\*Visual:\*\* GNS3 topology screenshot



\*\*Narration:\*\*

> "Here is our GNS3 topology. We used Cisco 7200 routers and Ubuntu server appliances."



\*\*Visual:\*\* Cisco router config scrolling



\*\*Narration:\*\*

> "The Cisco router is configured with IP addresses on both interfaces: G0/0 for the LAN and G0/1 for the IPsec tunnel."



\*\*Visual:\*\* StrongSwan configuration file



\*\*Narration:\*\*

> "On the cloud side, StrongSwan is configured as the IPsec gateway. We used IKEv2 with AES-256 encryption and 

> pre-shared key authentication."



\---



\## Scene 4: Testing \& Validation (2 minutes)



\*\*Visual:\*\* Ping from Ubuntu to Docker container



\*\*Narration:\*\*

> "To test connectivity, we ping from the on-premise Ubuntu server at 172.16.1.10 to the cloud Docker container at 10.0.0.10. 

> As you can see, the ping is successful."



\*\*Visual:\*\* `show crypto ipsec sa` command output



\*\*Narration:\*\*

> "On the Cisco router, we run 'show crypto ipsec sa' to verify the IPsec tunnel is established. 

> The output shows encryption and decryption packets are increasing, confirming the tunnel is working."



\*\*Visual:\*\* Wireshark capture showing ESP packets



\*\*Narration:\*\*

> "In Wireshark, we capture traffic between the router and StrongSwan. The packets are encrypted ESP packets, 

> proving our IPsec tunnel is securing the data."



\*\*Visual:\*\* iPerf performance test



\*\*Narration:\*\*

> "We also ran iPerf performance tests. The throughput between networks is approximately X Mbps with minimal latency."



\---



\## Scene 5: Challenges \& Solutions (1.5 minutes)



\*\*Visual:\*\* Troubleshooting screenshots



\*\*Narration:\*\*

> "We faced a few challenges. First, connecting Docker networks to GNS3 required configuring the vEthernet adapter 

> and using bridged networking."



\*\*Visual:\*\* IPsec debug logs



\*\*Narration:\*\*

> "Second, the IPsec tunnel initially failed to establish. We debugged using 'show crypto isakmp sa' on the router 

> and checked StrongSwan logs. The issue was mismatched PSK, which we corrected."



\*\*Visual:\*\* Working tunnel screenshot



\*\*Narration:\*\*

> "After troubleshooting, the tunnel came up successfully."



\---



\## Scene 6: Conclusion (1 minute)



\*\*Visual:\*\* Summary slide



\*\*Narration:\*\*

> "In conclusion, we successfully built a hybrid cloud environment connecting GNS3 to Docker, 

> established a secure IPsec tunnel, and verified end-to-end connectivity."



\*\*Visual:\*\* Future improvements slide



\*\*Narration:\*\*

> "Future improvements could include adding redundant tunnels and automating the entire deployment with Terraform."



\*\*Visual:\*\* Thank you slide with team names



\*\*Narration:\*\*

> "Thank you for watching. This was our Hybrid Cloud with IPsec project."



\---



\## Script Checklist



| Scene | Duration | Visual Ready | Narration Ready |

|-------|----------|--------------|-----------------|

| Scene 1: Introduction | 1 min | ⏳ | ⏳ |

| Scene 2: Topology | 1.5 min | ⏳ | ⏳ |

| Scene 3: Implementation | 2 min | ⏳ | ⏳ |

| Scene 4: Testing | 2 min | ⏳ | ⏳ |

| Scene 5: Challenges | 1.5 min | ⏳ | ⏳ |

| Scene 6: Conclusion | 1 min | ⏳ | ⏳ |



\---



\## Notes for Video Creation



\- \*\*Tool:\*\* OBS Studio for screen recording

\- \*\*Editing:\*\* CapCut or Shotcut

\- \*\*Background music:\*\* Optional, keep low volume

\- \*\*Narration:\*\* Clear and slow speaking pace

\- \*\*File name:\*\* `CCP\_HybridCloud\_Demo.mp4`



\---



\## Sign-off



\*\*Salik Saeed\*\*  

Documentation Lead

