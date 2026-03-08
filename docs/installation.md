# INSTALLATION GUIDE

## Di Termux

```bash
# 1. Update Termux
pkg update && pkg upgrade -y

# 2. Install dependencies
pkg install python libpcap git -y

# 3. Install Python packages
pip install rich scapy requests

# 4. Clone repository
git clone https://github.com/nanang55550-star/architect-02-neural-dashboard.git
cd architect-02-neural-dashboard

# 5. Jalankan
python architect_v3.py

##Di Linux (Ubuntu/Debian)Di
