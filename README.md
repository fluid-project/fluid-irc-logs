# Fluid IRC Logs from BotBot.me

The [BotBot.me](https://botbot.me/) logging service officially shuts down on 2018-11-05.

This repository contains the following:

- the raw logs scraped from BotBot with the assistance of the BotBot operators (the `*.log` files in the root directory) - these are large dumps of the channel log over the years in a single file
    - there is one set of files from a scrape on 2018-09-20 and one for a scrape on 2018-11-05 - the later one supersedes the earlier, but both are being retained for now
- `botbot_parser.py`, a Python script that parses the raw BotBot logs and extracts logs from on a per-day basis. It also does some reformatting to make the extracted logs more readable.
- individual directories for daily logs extracted from the raw logs for each channel: `fluid-design`, `fluid-tech` and `fluid-work`
- `parse_logs.sh`, a convenience script for running `botbot_parser.py` over multiple log files
- `README.md` - this file
- `timestampnotes.md` - a note on how URLs to individual messages in BotBot's logging interface are (or, unfortunately as it turns out, are not) related to timestamps
