Configurare i bot come servizi per Linux
===========================

`/etc/systemd/system/infunibot-telegram.service`

```
#infunibot-telegram

[Service]
ExecStart=python3 app.py
WorkingDirectory=/home/user/InfUniBot/InfUniBot-Telegram
Restart=always
StandardOutput=syslog
StandardError=syslog
SyslogIdentifier=infunibot-telegram
User=user
Group=user

[Install]
WantedBy=multi-user.target
```

`/etc/systemd/system/infunibot-discord.service`

```
#infunibot-discord

[Service]
ExecStart=python3 app.py
WorkingDirectory=/home/user/InfUniBot/InfUniBot-Discord
Restart=always
StandardOutput=syslog
StandardError=syslog
SyslogIdentifier=infunibot-discord
User=user
Group=user

[Install]
WantedBy=multi-user.target
```