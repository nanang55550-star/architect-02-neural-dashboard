"""
Network Scanner Module - ARP Scan
"""

from scapy.all import ARP, Ether, srp
import sqlite3

def scan_network(target_ip):
    """
    Scan jaringan pake ARP request
    
    Args:
        target_ip: IP range (e.g., 192.168.1.0/24)
    
    Returns:
        List of devices ditemukan
    """
    try:
        # Buat ARP request
        arp = ARP(pdst=target_ip)
        ether = Ether(dst="ff:ff:ff:ff:ff:ff")
        packet = ether/arp
        
        # Kirim packet
        result = srp(packet, timeout=2, verbose=0)[0]
        
        devices = []
        for sent, received in result:
            devices.append({
                'ip': received.psrc,
                'mac': received.hwsrc,
                'vendor': "Unknown",
                'is_new': False
            })
        
        return devices
        
    except Exception as e:
        print(f"Scan error: {e}")
        return []
