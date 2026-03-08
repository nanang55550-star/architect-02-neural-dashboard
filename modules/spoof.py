"""
MAC Spoofing Module - Ghost Mode
"""

import random
import subprocess
import os

def random_mac():
    """
    Generate MAC address random
    
    Returns:
        String MAC address
    """
    return "02:00:00:%02x:%02x:%02x" % (
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255)
    )

def enable_ghost_mode(interface):
    """
    Enable ghost mode (MAC spoofing)
    BUTUH ROOT!
    
    Args:
        interface: Interface name (e.g., wlan0)
    """
    if os.geteuid() != 0:
        print("[!] Ghost mode butuh root. Matikan dulu.")
        return False
    
    new_mac = random_mac()
    try:
        # Matikan interface
        subprocess.run(['ifconfig', interface, 'down'], check=True)
        # Ganti MAC
        subprocess.run(['ifconfig', interface, 'hw', 'ether', new_mac], check=True)
        # Hidupkan lagi
        subprocess.run(['ifconfig', interface, 'up'], check=True)
        
        print(f"[+] Ghost mode aktif: {interface} -> {new_mac}")
        return True
        
    except Exception as e:
        print(f"[!] Gagal ghost mode: {e}")
        return False
