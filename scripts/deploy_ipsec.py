import paramiko
import time
import datetime

# Router connection details
ROUTER_IP = "10.0.0.1"
USERNAME = "cisco"
PASSWORD = "cisco"

# IPsec configuration commands
IPSEC_COMMANDS = [
    "configure terminal",
    "crypto isakmp policy 10",
    " encryption aes 256",
    " hash sha256",
    " authentication pre-share",
    " group 14",
    " lifetime 86400",
    "exit",
    "crypto isakmp key HybridCloud2026 address 10.0.0.10",
    "crypto ipsec transform-set ESP-AES-SHA esp-aes 256 esp-sha-hmac",
    " mode tunnel",
    "exit",
    "crypto map CMAP 10 ipsec-isakmp",
    " set peer 10.0.0.10",
    " set transform-set ESP-AES-SHA",
    " match address 100",
    "exit",
    "access-list 100 permit ip 172.16.1.0 0.0.0.255 10.0.0.0 0.0.0.255",
    "interface FastEthernet2/0",
    " crypto map CMAP",
    "exit",
    "write memory",
    "exit"
]

def deploy_ipsec():
    print(f"[{datetime.datetime.now()}] Deploying IPsec to router...")
    
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ROUTER_IP, username=USERNAME, password=PASSWORD, look_for_keys=False, allow_agent=False)
        
        for cmd in IPSEC_COMMANDS:
            print(f">>> {cmd}")
            stdin, stdout, stderr = ssh.exec_command(cmd)
            time.sleep(0.5)
            output = stdout.read().decode()
            if output:
                print(output)
        
        ssh.close()
        print(f"[{datetime.datetime.now()}] IPsec deployment complete!")
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    deploy_ipsec()
