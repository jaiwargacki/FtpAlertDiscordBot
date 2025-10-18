#!/bin/bash

FTP_DIR="./data"

if [ ! -d "$FTP_DIR" ]; then
  echo "Creating data directory..."
  mkdir -p "$FTP_DIR"
else
  echo "Data directory already exists."
fi

source .env

echo "Starting FTP server..."
"${BABY_FTP_PATH}" &>/dev/null &

echo "Starting Discord bot..."
python ftp_alerts.py