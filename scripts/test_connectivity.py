# Week 2: Connectivity Verification Script
# Automation Lead - Nihaas
# Date: May 20, 2026

import subprocess
import datetime

# IP addresses from your IP plan
devices = {
    "Windows Host (WSL)": "10.0.0.2",
    "Cisco Router WAN": "10.0.0.1",
    "Cisco Router LAN": "172.16.1.1",
    "Ubuntu VM": "172.16.1.10",
    "Docker Container": "10.0.0.10"
}

print("=" * 60)
print(f"Week 2 Connectivity Test - {datetime.datetime.now()}")
print("=" * 60)

results = {}

for name, ip in devices.items():
    result = subprocess.run(f"ping -n 2 {ip}", 
                           capture_output=True, text=True, shell=True)
    
    if "Reply from" in result.stdout or "bytes=" in result.stdout:
        status = "✅ REACHABLE"
        print(f"{status} | {name} ({ip})")
        results[name] = True
    else:
        status = "❌ NOT REACHABLE"
        print(f"{status} | {name} ({ip})")
        results[name] = False

print("\n" + "=" * 60)
print("SUMMARY:")
print("=" * 60)

working = sum(1 for v in results.values() if v)
total = len(results)
print(f"Working: {working}/{total} devices")

if working == total:
    print("✅ Week 2 connectivity goal ACHIEVED!")
else:
    print("❌ Week 2 connectivity goal NOT achieved yet")
    print("Check GNS3 and router configurations")