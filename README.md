# 🌅 WINSNIP Dawn Farmer

Auto-farming bot untuk Dawn Internet dengan support multi-account dan proxy.

## ✨ Features

- ✅ Multi-account farming
- ✅ Multi-proxy support  
- ✅ Auto statistics display
- ✅ Color terminal output
- ✅ Modular & clean code
- ✅ Cross-platform (Windows, Linux, macOS)

## 📋 Requirements

- Python 3.8+
- curl-cffi
- colorama (optional, untuk warna)

## 🚀 Installation

### Windows
```bash
pip install -r requirements.txt
```

### Linux/Mac
```bash
pip3 install -r requirements.txt
```

### Android (Termux)

1. **Install Termux**
   - Download dari F-Droid: https://f-droid.org/en/packages/com.termux/
   - Atau Google Play Store (versi lama)

2. **Update Package & Install Dependencies**
   ```bash
   pkg update && pkg upgrade
   pkg install python git
   ```

3. **Clone/Download Bot**
   ```bash
   # Clone dari GitHub
   git clone https://github.com/winsnip/Dawn-Farmer.git
   cd Dawn-Farmer
   
   # Atau download ZIP dari GitHub dan extract
   ```

4. **Install Requirements**
   ```bash
   pip install -r requirements.txt
   ```

5. **Setup Token & Run**
   ```bash
   # Edit tokens.txt pake nano
   nano tokens.txt
   # Paste token, tekan Ctrl+X, Y, Enter untuk save
   
   # Run bot
   python farm.py
   ```

**Tips Android:**
- Gunakan Termux:Widget untuk auto-start
- Install Termux:Boot untuk run saat HP restart
- Gunakan screen/tmux untuk background farming:
  ```bash
  pkg install tmux
  tmux new -s farm
  python farm.py
  # Tekan Ctrl+B lalu D untuk detach
  # tmux attach -t farm untuk kembali
  ```

## ⚙️ Setup

### 1. Cara Mendapatkan x-privy-token

**Langkah-langkah:**

1. **Buka Dawn Dashboard**
   - Kunjungi: https://dashboard.dawninternet.com
   - Login dengan akun Anda

2. **Buka Developer Tools**
   - Windows/Linux: Tekan `F12` atau `Ctrl+Shift+I`
   - Mac: Tekan `Cmd+Option+I`

3. **Buka Tab Network**
   - Klik tab **"Network"** di Developer Tools
   - Refresh halaman (F5)

4. **Cari Request**
   - Scroll list request
   - Cari request yang menuju `api.dawninternet.com`
   - Klik salah satu request (contoh: `my-code`, `stats`, `claims`, dll)

5. **Copy Token**
   - Klik tab **"Headers"** 
   - Scroll ke bawah ke bagian **"Request Headers"**
   - Cari header **"X-Privy-Token"**
   - Copy value tokennya (panjang sekali, contoh: `eyJhbGciOiJ...`)

6. **Paste ke tokens.txt**
   ```
   eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCIsImtpZ...
   ```

**Struktur Token:**
- Token dimulai dengan `eyJ`
- Sangat panjang (ratusan karakter)
- Format: `xxxxx.yyyyy.zzzzz` (3 bagian dipisah titik)

**Catatan Penting:**
- ⚠️ Jangan share token ke orang lain!
- Token akan expired, jika bot error, ambil token baru
- Satu token = satu akun

---

### 2. Add Tokens ke File

**Edit `tokens.txt`:**
```
your-x-privy-token-here
another-token-if-you-have
```

Bisa tambah banyak token (satu per baris) untuk multi-account farming.

---

### 3. Add Proxies (Optional)

**Edit `proxies.txt`:**
```
http://user:pass@ip:port
http://ip:port
socks5://user:pass@ip:port
```

Lihat `proxies.example.txt` untuk contoh format.

## 🎮 Usage

### Windows
```bash
python farm.py
```

### Linux/Mac
```bash
python3 farm.py
```

### Stop Farming
Tekan `Ctrl+C` untuk stop dengan aman.

## 📊 Statistics Display

Bot akan menampilkan:
- 💰 Total Points (Current + Referral)
- 🔥 Farming Streak
- 👥 Referral Stats & Code
- 📈 24h Activity

Statistics update setiap 5 ping (sekitar 50 menit).

## 📁 File Structure

```
farm.py              # Main entry point
tokens.txt           # Your x-privy-tokens
proxies.txt          # Your proxies (optional)
proxies.example.txt  # Proxy format examples
requirements.txt     # Dependencies
src/
  ├── config.py      # Configuration
  ├── core/
  │   ├── client.py  # API client
  │   └── farmer.py  # Farming logic
  └── utils/
      └── helpers.py # Helper functions
```

## ⚙️ Configuration

Edit `src/config.py` untuk mengubah:
- `interval`: Ping interval (default: 600 detik / 10 menit)
- `tokens_file`: File token location
- `proxies_file`: File proxy location

## 🔧 Troubleshooting

**Error: No tokens found**
- Pastikan `tokens.txt` ada dan berisi token
- Format: satu token per baris

**Error: Module not found**
- Install dependencies: `pip install -r requirements.txt`

**Ping failed**
- Check token masih valid
- Check proxy jika dipakai
- Check koneksi internet

## 📝 Notes

- Interval 10 menit (600s) adalah yang paling aman untuk earning points
- Jangan set terlalu cepat atau points tidak akan dihitung
- Streak akan bertambah jika farming konsisten setiap hari
- Gunakan proxy berbeda untuk setiap account

## 👨‍💻 Developer

**WINSNIP**  
Version: 1.0.0

## ⚠️ Disclaimer

Bot ini untuk educational purposes. Gunakan dengan bijak dan sesuai Terms of Service Dawn Internet.
