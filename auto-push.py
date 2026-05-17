#!/usr/bin/env python3
"""
Script Otomatis Upload File ke GitHub Repository
Cara penggunaan: python3 auto-push.py "pesan commit Anda"
"""

import subprocess
import sys
from datetime import datetime

# ANSI Color Codes
class Colors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    BOLD = '\033[1m'
    END = '\033[0m'

def print_header(text):
    print(f"\n{Colors.BLUE}{'='*60}{Colors.END}")
    print(f"{Colors.BLUE}{Colors.BOLD}{text}{Colors.END}")
    print(f"{Colors.BLUE}{'='*60}{Colors.END}\n")

def print_success(text):
    print(f"{Colors.GREEN}✓ {text}{Colors.END}")

def print_error(text):
    print(f"{Colors.RED}✗ {text}{Colors.END}")

def print_info(text):
    print(f"{Colors.YELLOW}➜ {text}{Colors.END}")

def run_command(cmd, description):
    """Jalankan command dan return status"""
    print_info(description)
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            return True, result.stdout
        else:
            return False, result.stderr
    except Exception as e:
        return False, str(e)

def main():
    print_header("🚀 GITHUB AUTO PUSH TOOL")
    
    # Get commit message dari argumen
    if len(sys.argv) > 1:
        commit_msg = " ".join(sys.argv[1:])
    else:
        commit_msg = f"Update website - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    
    print(f"{Colors.CYAN}Pesan Commit: {Colors.BOLD}'{commit_msg}'{Colors.END}\n")
    
    # Step 1: Check git status
    print_info("Mengecek status repository...")
    success, output = run_command("git status --short", "")
    if output.strip():
        print(output)
    else:
        print("Tidak ada file yang berubah")
    print()
    
    # Step 2: Add files
    print_info("Menambahkan semua file yang berubah...")
    success, output = run_command("git add .", "")
    if success:
        print_success("Semua file berhasil ditambahkan")
    else:
        print_error("Gagal menambahkan file")
        return False
    print()
    
    # Step 3: Commit
    print_info("Melakukan commit...")
    success, output = run_command(f'git commit -m "{commit_msg}"', "")
    if success:
        print_success("Commit berhasil dibuat")
        print(output.strip())
    elif "nothing to commit" in output:
        print(f"{Colors.YELLOW}⚠ Tidak ada perubahan untuk di-commit{Colors.END}")
        return False
    else:
        print_error("Gagal melakukan commit")
        print(output)
        return False
    print()
    
    # Step 4: Push
    print_info("Mendorong ke GitHub (main branch)...")
    success, output = run_command("git push origin main", "")
    if success:
        print_success("Push berhasil!")
        print()
        print_header("✅ SELESAI!")
        print(f"{Colors.GREEN}Website Anda sudah diupdate di GitHub!{Colors.END}")
        print(f"{Colors.CYAN}📍 URL: https://najibalwafa020-tech.github.io{Colors.END}\n")
        return True
    else:
        print_error("Push gagal!")
        print(output)
        print(f"\n{Colors.YELLOW}Kemungkinan masalah:{Colors.END}")
        print("• Koneksi internet tidak stabil")
        print("• Token akses GitHub expired/invalid")
        print("• Permission denied")
        print("\nCoba jalankan: git push origin main")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
