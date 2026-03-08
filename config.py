# ARCHITECT 02 - Konfigurasi
# Edit sesuai jaringan lo

# Target jaringan (ganti sesuai IP WiFi lo)
# Cek pake: ip route show
TARGET_IP = "192.168.1.0/24"

# Interface WiFi (biasanya wlan0)
INTERFACE = "wlan0"

# Ghost Mode (MAC Spoofing) - butuh ROOT!
GHOST_MODE = False

# Waktu refresh (detik)
REFRESH_TIME = 5

# Telegram Alert (opsional)
TELEGRAM_TOKEN = ""  # Isi kalau mau notif
CHAT_ID = ""         # Isi kalau mau notif
