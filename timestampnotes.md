# Some Notes on BotBot Log Timestamps

https://botbot.me/freenode/fluid-work/msg/96374801/ : 2018-02-01T11:04:09.587524+00:00

https://botbot.me/freenode/fluid-work/msg/105934113/ : 2018-11-02T09:13:27.702766+00:00

The ID of an individual log line appears to simply be the auto-incremented primary key: https://github.com/BotBotMe/botbot-web/blob/master/botbot/templates/logs/log_display.html#L7 (`line.pk`) - conclusion: unfortunately there is no time semantic to be derived from the URL. There is a rough coherence that could be established by something like recording the IDs for the start of each month, but even this would take a certain amount of time.
