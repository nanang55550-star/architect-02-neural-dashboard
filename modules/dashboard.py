"""
Dashboard Module - Rich Table Display
"""

from rich.table import Table
from rich.panel import Panel
import sqlite3

def generate_table(devices, conn):
    """
    Generate Rich table buat dashboard
    
    Args:
        devices: List of devices dari scan
        conn: Database connection
    
    Returns:
        Rich Table object
    """
    table = Table(
        title="[bold red]LIVE NETWORK INFILTRATION[/bold red]",
        border_style="cyan",
        header_style="bold magenta"
    )
    
    table.add_column("IP ADDRESS", style="green", no_wrap=True)
    table.add_column("MAC ADDRESS", style="yellow")
    table.add_column("VENDOR", style="blue")
    table.add_column("RISK LEVEL", style="red")
    table.add_column("STATUS", style="white")
    
    c = conn.cursor()
    
    for dev in devices:
        # Cek di database
        c.execute("SELECT * FROM devices WHERE mac=?", (dev['mac'],))
        data = c.fetchone()
        
        if data is None:
            # Perangkat baru
            risk = "⚠️ HIGH"
            status = "NEW"
            dev['is_new'] = True
            
            # Simpan ke database
            c.execute("INSERT INTO devices VALUES (?, ?, ?)",
                     (dev['mac'], dev['ip'], "Unknown"))
            conn.commit()
        else:
            risk = "✓ LOW"
            status = "KNOWN"
            dev['is_new'] = False
        
        table.add_row(
            dev['ip'],
            dev['mac'],
            dev['vendor'],
            risk,
            status
        )
    
    return Panel(table, title="[bold cyan]SCAN RESULTS[/bold cyan]")
