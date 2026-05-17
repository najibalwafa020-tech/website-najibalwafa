#!/bin/bash

# Script Otomatis Upload File ke GitHub Repository
# Cara penggunaan:
# ./auto-push.sh "pesan commit Anda di sini"

# Warna output
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Check jika ada argumen (pesan commit)
if [ $# -eq 0 ]; then
    # Jika tidak ada argumen, gunakan default
    COMMIT_MSG="Update website files"
    echo -e "${YELLOW}⚠️  Pesan commit tidak diberikan${NC}"
    echo -e "${BLUE}Menggunakan pesan default: '$COMMIT_MSG'${NC}"
else
    # Gunakan argumen sebagai pesan commit
    COMMIT_MSG="$@"
fi

echo ""
echo -e "${BLUE}═══════════════════════════════════════════════════${NC}"
echo -e "${BLUE}🚀 AUTO PUSH TO GITHUB${NC}"
echo -e "${BLUE}═══════════════════════════════════════════════════${NC}"
echo ""

# Step 1: Lihat status git
echo -e "${YELLOW}📋 Mengecek status repository...${NC}"
git status
echo ""

# Step 2: Add semua file yang berubah
echo -e "${YELLOW}➕ Menambahkan semua file yang berubah...${NC}"
git add .
echo -e "${GREEN}✓ File berhasil ditambahkan${NC}"
echo ""

# Step 3: Commit dengan pesan yang diberikan
echo -e "${YELLOW}💾 Melakukan commit dengan pesan: '$COMMIT_MSG'${NC}"
git commit -m "$COMMIT_MSG"

if [ $? -ne 0 ]; then
    echo -e "${RED}✗ Commit gagal (mungkin tidak ada perubahan)${NC}"
    exit 1
fi

echo -e "${GREEN}✓ Commit berhasil${NC}"
echo ""

# Step 4: Push ke GitHub
echo -e "${YELLOW}🌐 Mendorong ke GitHub...${NC}"
git push origin main

if [ $? -eq 0 ]; then
    echo -e "${GREEN}✓ Push berhasil!${NC}"
    echo ""
    echo -e "${BLUE}═══════════════════════════════════════════════════${NC}"
    echo -e "${GREEN}✅ SELESAI! Website Anda sudah diupdate di GitHub${NC}"
    echo -e "${BLUE}═══════════════════════════════════════════════════${NC}"
    echo ""
    echo -e "${BLUE}📍 URL Website: https://najibalwafa020-tech.github.io${NC}"
    echo ""
else
    echo -e "${RED}✗ Push gagal! Periksa koneksi internet dan akses token${NC}"
    exit 1
fi
