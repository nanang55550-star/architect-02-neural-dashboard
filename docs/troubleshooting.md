
# TROUBLESHOOTING

## Error: "No module named scapy"

```bash
pip install scapy

Error: "Permission denied"
bash
```
# Jalankan dengan root
```bash
sudo python architect_v3.py
```
# python: "Ghost mode butuh root"
Matikan ghost mode di config:
```bash
GHOST_MODE =False
```
# Scan kosong / gak ada device
Cek IP jaringan lo:

```bash
ip route show
# Update TARGET_IP di config
