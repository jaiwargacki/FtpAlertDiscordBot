#!/bin/bash

source .env

if [ ! -d "${DATA_DIR}" ]; then
  echo "Creating data directory..."
  mkdir -p "${DATA_DIR}"
else
  echo "Data directory already exists."
fi

echo "Starting FTP server..."
"${BABY_FTP_PATH}" &>/dev/null &

echo "Starting Discord bot..."
python ftp_alerts.py