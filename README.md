# FTP Alert Discord Bot
Using a locally deployed FTP server this Discord bot provides notification of alerts from local NVR.
This bot was developed to handle the images from a Reolink NVR, but could likely be adapted for many 
FTP file notification applications. 

## Deployment
Before deploying locally you will need to set up a Discord bot and get the bot token as well as your user ID.
Set the following environment variables in a `.env` file in the `src` directory:

| Variable Name     | Description                                      |
|-------------------|--------------------------------------------------|
| DISCORD_BOT_TOKEN | The token for the Discord bot                    |
| USER_ID           | The Discord user ID to send alerts to            |
| BABY_FTP_PATH     | The path to the BabyFTP executable (only if using `start.sh`)               |

The Discord bot is set up to work alongside a locally deployed FTP server. 
`start.sh` handles starting both the FTP server and the Discord bot. In order to use the `start.sh` script, `babyftp.exe` is needed and `BABY_FTP_PATH` must be set. 

## Future Work
- [ ] More robust error handling and logging mechanisms
- [ ] More detailed alert messages
- [ ] Support for multiple users or channels for alerts