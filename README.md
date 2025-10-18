# FTP Alert Discord Bot
This Discord bot monitors a local directory for new files (alerts) and sends notifications to a specified Discord user. This is particularly useful for receiving alerts from a local NVR (Network Video Recorder) system that uploads images via FTP.

Currently, the bot is meant to work with a single user (configured via the `USER_ID` environment variable) and sends alerts as direct messages.

## Bot Features
- **Automatic Alerts**: The bot checks the specified directory every minute for new files and sends them as alerts to the designated Discord user. The camera name is found using `get_camera_name()` from `camera_mapping.py`.
- **/togglealerts**: Toggles the sending of FTP alerts on or off. If alerts are disabled, new files will not trigger notifications, but they will still be deleted every minute.

> The data directory is not meant for long-term storage of files. Alerts are deleted after being sent or checked.

## Getting Started
1. Set up a Discord bot and invite it to your server / DM.
1. Create a `.env` file in the `src` directory with the required environment variables (see Environment Variables section below).
1. Run the bot using Python: `python src/ftp_alerts.py` or use the provided `start.sh` script to start both the bot and a local FTP server.

## Environment Variables
The following environment variables need to be set in a `.env` file located in the `src` directory:
| Variable Name     | Description                                      |
|-------------------|--------------------------------------------------|
| DISCORD_BOT_TOKEN | The token for the Discord bot                    |
| USER_ID           | The Discord user ID to send alerts to            |
| DATA_DIR          | The directory to monitor for new files (alerts)  |
| BABY_FTP_PATH     | The path to the BabyFTP executable (only if using `start.sh`) |

## FTP Server Setup (Optional)
If you want to use the provided `start.sh` script to run a local FTP server alongside the Discord bot, you will need to download and set up BabyFTP. You will need to set the `BABY_FTP_PATH` environment variable to point to the BabyFTP executable. 

## Future Work
- [ ] More robust error handling and logging mechanisms
- [ ] Support for multiple users or channels for alerts