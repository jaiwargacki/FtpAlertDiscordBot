# Ftp Alert Discord Bot
Using a locally deployed FTP server this Discord bot provides notification of alerts from local NVR.
This bot was developed to handle the images from a Reolink NVR, but could likely be adapted for many 
FTP file notification applications. 

## Deployment
_TODO: Bot deployment info_

Set up to work alongside a locally deployed FTP server. 
`start.sh` handles starting both the FTP server (need `babyftp.exe` locally, setting `BABY_FTP_PATH` in your `.env`) and the Discord bot. 