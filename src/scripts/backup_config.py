import paramiko
import datetime

ROUTER_IP = "10.0.0.1"
USERNAME = "cisco"
PASSWORD = "cisco"

def backup_router_config():
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"R1_backup_{timestamp}.txt"
    
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ROUTER_IP, username=USERNAME, password=PASSWORD, look_for_keys=False, allow_agent=False)
        
        stdin, stdout, stderr = ssh.exec_command("show running-config")
        config = stdout.read().decode()
        
        with open(filename, "w") as f:
            f.write(config)
        
        ssh.close()
        print(f"[{datetime.datetime.now()}] Backup saved: {filename}")
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    backup_router_config()
