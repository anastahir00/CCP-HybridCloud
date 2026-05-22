# StrongSwan Cloud-Side Setup Guide

## Overview
This guide explains how to set up StrongSwan as the cloud-side
IPsec endpoint in our Hybrid Cloud project.

## Prerequisites
- Docker Desktop installed
- WSL2 with Ubuntu 22.04

## Step 1: Pull Ubuntu Docker Image
docker pull ubuntu:22.04

## Step 2: Run Container
docker run -it --name cloud-gateway ubuntu:22.04 bash

## Step 3: Install StrongSwan
apt update && apt install -y strongswan strongswan-pki

## Step 4: Configure ipsec.conf
- left = 10.0.0.10 (cloud side IP)
- leftsubnet = 10.0.0.0/24
- right = 172.16.1.1 (on-premise router IP)
- rightsubnet = 172.16.1.0/24
- Encryption: aes256-sha256-modp2048

## Step 5: Configure ipsec.secrets
10.0.0.10 172.16.1.1 : PSK "HybridCloud@2026"

## Step 6: Start StrongSwan
ipsec start
ipsec status

## Network Diagram
Cloud (Docker) 10.0.0.0/24 <--IPsec Tunnel--> On-premise 172.16.1.0/24