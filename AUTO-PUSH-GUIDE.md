# 🚀 AUTO PUSH - Dokumentasi

Dokumentasi lengkap untuk menggunakan sistem otomatis upload file ke GitHub.

## 📋 Daftar Isi
1. [Quick Start](#quick-start)
2. [Opsi 1: Python Script](#opsi-1-python-script) ⭐ REKOMENDASI
3. [Opsi 2: Bash Script](#opsi-2-bash-script)
4. [Opsi 3: Manual Commands](#opsi-3-manual-commands)
5. [Troubleshooting](#troubleshooting)

---

## Quick Start

### Cara Tercepat (Python - REKOMENDASI):
```bash
python3 auto-push.py "masukan file index.html"
```

### Atau (Bash):
```bash
bash auto-push.sh "masukan file index.html"
```

---

## Opsi 1: Python Script ⭐

**File:** `auto-push.py`

### Setup (One-time):
```bash
# Pastikan Python 3 terinstall
python3 --version

# Buat executable
chmod +x auto-push.py
```

### Cara Pakai:

#### Dengan pesan custom:
```bash
python3 auto-push.py "masukan file index.html"
```

Output:
```
============================================================
🚀 GITHUB AUTO PUSH TOOL
============================================================

Pesan Commit: 'masukan file index.html'

➜ Mengecek status repository...
➜ Menambahkan semua file yang berubah...
✓ Semua file berhasil ditambahkan
➜ Melakukan commit...
✓ Commit berhasil dibuat
➜ Mendorong ke GitHub (main branch)...
✓ Push berhasil!

============================================================
✅ SELESAI!
Website Anda sudah diupdate di GitHub!
📍 URL: https://najibalwafa020-tech.github.io
============================================================
```

#### Tanpa pesan (otomatis timestamp):
```bash
python3 auto-push.py
```

### Contoh Command:
```bash
# Upload dengan deskripsi file
python3 auto-push.py "Update file style.css dan index.html"

# Upload dengan fitur
python3 auto-push.py "Tambah section backend dan database info"

# Upload sederhana
python3 auto-push.py "Update website"
```

---

## Opsi 2: Bash Script

**File:** `auto-push.sh`

### Setup (One-time):
```bash
chmod +x auto-push.sh
```

### Cara Pakai:
```bash
./auto-push.sh "masukan file index.html"
```

### Tanpa pesan:
```bash
./auto-push.sh
# Akan menggunakan pesan default: "Update website files"
```

---

## Opsi 3: Manual Commands

Jika tidak ingin menggunakan script, jalankan manual:

```bash
# 1. Cek status
git status

# 2. Add semua file
git add .

# 3. Commit dengan pesan
git commit -m "masukan file index.html"

# 4. Push ke GitHub
git push origin main
```

---

## Workflow Sehari-hari

### Contoh Skenario:

**Skenario 1: Membuat file baru (style.css)**
```bash
# 1. Buat file style.css di folder project
# 2. Edit file sesuai kebutuhan
# 3. Jalankan:
python3 auto-push.py "Buat file style.css dengan styling"
# ✓ File otomatis masuk ke GitHub!
```

**Skenario 2: Update index.html**
```bash
# 1. Edit index.html
# 2. Jalankan:
python3 auto-push.py "Update index.html dengan fitur baru"
# ✓ Perubahan otomatis ter-push!
```

**Skenario 3: Tambah multiple files**
```bash
# 1. Buat/edit multiple files (index.html, style.css, script.js)
# 2. Jalankan satu command:
python3 auto-push.py "Update index.html, style.css, dan script.js"
# ✓ SEMUA file langsung masuk!
```

---

## Penjelasan Yang Terjadi

Ketika Anda menjalankan command, sistem akan:

1. **Cek Status** → Lihat file apa yang berubah
2. **Git Add** → Tambahkan semua file ke staging area
3. **Git Commit** → Buat snapshot dengan pesan Anda
4. **Git Push** → Kirim ke GitHub repository
5. **Website Update** → GitHub Pages otomatis redeploy

### Timeline:
- Command dijalankan: Instant
- File di-push: 1-2 detik
- Website update di GitHub: 1-3 menit
- Website live: https://najibalwafa020-tech.github.io ✓

---

## Tips & Tricks

### 1. Alias Bash (Optional - untuk command lebih pendek)
```bash
# Tambah ke ~/.bashrc atau ~/.zshrc
alias push='python3 auto-push.py'

# Sekarang cukup ketik:
push "Update website"
```

### 2. Lihat History Commit
```bash
git log --oneline
```

### 3. Lihat File Yang Berubah
```bash
git status
```

### 4. Lihat Diff Sebelum Push
```bash
git diff
```

---

## Troubleshooting

### ❌ Error: "Permission denied"
```bash
# Solusi: Buat file executable
chmod +x auto-push.py
chmod +x auto-push.sh

# Atau gunakan:
python3 auto-push.py "pesan"
bash auto-push.sh "pesan"
```

### ❌ Error: "fatal: not a git repository"
```bash
# Solusi: Pastikan Anda di folder project
cd /workspaces/website-najibalwafa
python3 auto-push.py "pesan"
```

### ❌ Error: "nothing to commit"
```bash
# Berarti tidak ada file yang berubah
# Solusi: Edit file terlebih dahulu, baru jalankan script
```

### ❌ Error: "fatal: origin does not appear to be a 'git' repository"
```bash
# Pastikan git sudah dikonfigurasi dengan GitHub token
git remote -v
# Jika kosong, setup dengan:
git remote add origin https://github.com/najibalwafa020-tech/website-najibalwafa.git
```

### ❌ Error: "Authentication failed / 403 Forbidden"
```bash
# Solusi: Setup GitHub Token dengan benar
# 1. Generate token di: https://github.com/settings/tokens
# 2. Gunakan saat login
# 3. Atau setup SSH key untuk GitHub
```

---

## Setup Awal (Sekali saja)

Jika belum setup git di folder project:

```bash
# 1. Go to project folder
cd /workspaces/website-najibalwafa

# 2. Initialize git (jika belum)
git init

# 3. Add remote GitHub
git remote add origin https://github.com/najibalwafa020-tech/website-najibalwafa.git

# 4. Set branch name
git branch -M main

# 5. Test dengan:
python3 auto-push.py "Initial commit"
```

---

## Fitur Yang Dilakukan Script

✅ Otomatis detect file yang berubah
✅ Add semua file dalam satu command
✅ Commit dengan pesan yang jelas
✅ Push ke main branch
✅ Colored output untuk kemudahan baca
✅ Error handling yang baik
✅ Display URL website setelah sukses

---

## Kesimpulan

**Langkah cepat upload:**

```bash
# Edit file Anda
# Kemudian:
python3 auto-push.py "deskripsi file"

# SELESAI! ✓
```

Tidak perlu lagi mengetik 4 command (`git add`, `git commit`, `git push`), cukup 1 command saja!

---

**Created:** 2026-05-17
**Updated:** Active ✅
