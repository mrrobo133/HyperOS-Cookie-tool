#!/usr/bin/env bash

echo "[*] Updating package lists..."
pkg update -y && pkg upgrade -y

echo "[*] Installing Python and Git..."
pkg install python git -y

echo "[+] Installation completed successfully!"
