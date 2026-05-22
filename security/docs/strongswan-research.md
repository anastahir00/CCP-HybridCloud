# StrongSwan IPsec Research
## What is StrongSwan?
StrongSwan is an open-source IPsec-based VPN solution for Linux.
It implements IKEv1 and IKEv2 key exchange protocols.

## What is IPsec?
IPsec (Internet Protocol Security) encrypts and authenticates 
IP packets to secure network communications.

## How it works in our project
- Cloud side (10.0.0.0/24): StrongSwan runs in Docker container
- On-premise side (172.16.1.0/24): Cisco Router acts as IPsec endpoint
- Tunnel encrypts all traffic between the two networks using AES-256

## Encryption used
- IKE: aes256-sha256-modp2048
- ESP: aes256-sha256
- Auth: Pre-Shared Key (PSK)    