# 🧠 ARCHITECT 02 - NEURAL DASHBOARD

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)](https://python.org)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![Termux](https://img.shields.io/badge/Termux-Compatible-brightgreen)](https://termux.com)

**Real-time Network Monitoring Dashboard with Matrix-style UI**  
Built for Termux/HP by **@nanang55550-star**

---

## 📋 **FITUR UTAMA**

| Fitur | Deskripsi |
|-------|-----------|
| 🕵️ **Live Network Scan** | Deteksi semua perangkat di jaringan WiFi lo |
| 🎨 **Rich Dashboard** | Tampilan hacker ala film Matrix (warna-warni) |
| 👻 **Ghost Mode** | Ganti MAC address biar gak ketauan router (butuh root) |
| ⚠️ **Risk Level** | Label HIGH/LOW buat perangkat asing |
| 🔄 **Auto Refresh** | Update otomatis tiap 5 detik |

---

## 🚀 **QUICK START**

```bash
# Clone repository
git clone https://github.com/nanang55550-star/architect-02-neural-dashboard.git
cd architect-02-neural-dashboard

# Install dependencies
pip install -r requirements.txt

# Jalankan
python architect_v3.py
```

---

## 📦 **INSTALASI DI TERMUX**

```bash
# Update Termux
pkg update && pkg upgrade -y

# Install Python & dependencies
pkg install python libpcap -y
pip install rich scapy

# Clone & run
git clone https://github.com/nanang55550-star/architect-02-neural-dashboard.git
cd architect-02-neural-dashboard
python architect_v3.py
```

---

## ⚙️ **KONFIGURASI**

Edit `config.py`:

```python
# config.py
TARGET_IP = "192.168.1.0/24"  # Ganti dengan IP jaringan lo
INTERFACE = "wlan0"           # Interface WiFi
GHOST_MODE = False             # True kalau HP root
REFRESH_TIME = 5               # Refresh per detik
```

---

## 🖼️ **SCREENSHOT**

```
┌─────────────────────────────────────────────┐
│   ARCHITECT 02 - LIVE NETWORK INFILTRATION   │
├──────────────┬───────────────┬──────────────┤
│ IP ADDRESS   │ MAC ADDRESS   │ RISK LEVEL   │
├──────────────┼───────────────┼──────────────┤
│ 192.168.1.1  │ 00:11:22...   │ LOW          │
│ 192.168.1.5  │ AA:BB:CC...   │ LOW          │
│ 192.168.1.12 │ 11:22:33...   │ HIGH         │
└──────────────┴───────────────┴──────────────┘
```

---

## 🛠️ **MODULES**

| Module | Fungsi |
|--------|--------|
| `scanner.py` | Scan ARP buat deteksi perangkat |
| `dashboard.py` | Tampilan Rich Table |
| `spoof.py` | MAC spoofing (butuh root) |
| `utils.py` | Fungsi bantuan |

---

## ⚠️ **DISCLAIMER**

Tools ini **HANYA** untuk:
- ✅ Memantau jaringan lo sendiri
- ✅ Belajar network security
- ✅ Testing keamanan WiFi pribadi

**DILARANG** digunakan untuk:
- ❌ Menyerang jaringan orang lain
- ❌ Mencuri data
- ❌ Aktivitas ilegal

---

## 📝 **LICENSE**

MIT License - lihat file [LICENSE](LICENSE)

---

## 📬 **CONTACT**

**Creator:** [@nanang55550-star](https://github.com/nanang55550-star)

- GitHub: [nanang55550-star](https://github.com/nanang55550-star)
- Discord: [YRYwwEc8](https://discord.gg/YRYwwEc8)

---

**⭐ Star repo ini kalau bermanfaat!** 🚀
