#!/usr/bin/env python3
"""
ARCHITECT 02 - NEURAL DASHBOARD
Real-time Network Monitoring dengan Matrix-style UI
Author: @nanang55550-star
"""

import os
import time
import random
from rich.console import Console
from rich.table import Table
from rich.live import Live
from rich.panel import Panel
from rich.layout import Layout
from rich.text import Text

from modules.scanner import scan_network
from modules.dashboard import generate_table
from modules.spoof import random_mac, enable_ghost_mode
from modules.utils import setup_database, send_alert
import config

console = Console()

def create_layout():
    """Buat layout dashboard"""
    layout = Layout()
    layout.split_column(
        Layout(name="header", size=3),
        Layout(name="body"),
        Layout(name="footer", size=3)
    )
    return layout

def update_header():
    """Update header dengan info sistem"""
    return Panel(
        Text(f"ARCHITECT 02 - NEURAL NETWORK MONITOR\n"
             f"Target: {config.TARGET_IP} | Interface: {config.INTERFACE} | "
             f"Ghost Mode: {'ON' if config.GHOST_MODE else 'OFF'}",
             style="bold cyan"),
        style="red"
    )

def update_footer():
    """Update footer dengan status"""
    return Panel(
        Text(f"Press Ctrl+C to exit | Last scan: {time.strftime('%H:%M:%S')}",
             style="dim white"),
        style="blue"
    )

def main():
    """Main function"""
    os.system('clear')
    
    # Setup database
    conn = setup_database()
    
    # Banner
    console.print(Panel.fit(
        "[bold red]ARCHITECT 02[/bold red] - [cyan]NEURAL DASHBOARD[/cyan]\n"
        "[green]System Online[/green] • [yellow]Ghost Mode: {}[/yellow]".format(
            "ACTIVE" if config.GHOST_MODE else "DISABLED"
        ),
        title="[white]BOOT SEQUENCE[/white]"
    ))
    time.sleep(2)
    
    # Enable ghost mode kalau aktif
    if config.GHOST_MODE:
        enable_ghost_mode(config.INTERFACE)
    
    layout = create_layout()
    
    with Live(layout, refresh_per_second=1, screen=True) as live:
        while True:
            # Update header & footer
            layout["header"].update(update_header())
            layout["footer"].update(update_footer())
            
            # Scan jaringan
            devices = scan_network(config.TARGET_IP)
            
            # Generate table
            table = generate_table(devices, conn)
            layout["body"].update(table)
            
            # Cek perangkat baru
            for dev in devices:
                if dev.get('is_new', False):
                    msg = f"⚠️ NEW DEVICE: {dev['ip']} ({dev['mac']})"
                    console.print(f"[red]{msg}[/red]")
                    
                    # Kirim Telegram alert kalau dikonfigurasi
                    if config.TELEGRAM_TOKEN and config.CHAT_ID:
                        send_alert(msg, config.TELEGRAM_TOKEN, config.CHAT_ID)
            
            time.sleep(config.REFRESH_TIME)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        console.print("\n[bold red][!] ARCHITECT 02 SHUTTING DOWN... BYE BOSS![/bold red]")
    except Exception as e:
        console.print(f"[bold red]ERROR: {e}[/bold red]")
