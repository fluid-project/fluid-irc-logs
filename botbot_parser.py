#!/usr/bin/env python

"""
Usage:

python botbot_parser.py [log_file_name] [channel_name] [start_date]

ex: python botbot_parser.py fluid-design.log fluid-design 2018-09-20

"""

import datetime
import sys
import os
import re

def get_formatted_log_line(log_line, current_date):
    fixed_ts = re.sub(r'\[([0-9][0-9]:[0-9][0-9]:[0-9][0-9])\]', current_date.strftime("%Y-%m-%d") + r'T\1', log_line)
    return fixed_ts

log_file_name = sys.argv[1]

channel_name = sys.argv[2]

# Start date of the logs, the first line will be for this date
# This could be calculated from the first date in the logs,
# but not currently doing so
start_date = sys.argv[3]

# make directory for the parsed files if it doesn't exist

if not os.path.exists(channel_name):
    os.makedirs(channel_name)

log_file = open(log_file_name, "r")

# print the first line to file based on the entered start_date

f = open(channel_name + os.sep + channel_name + "-" + start_date + ".log", "w")
first_entry = log_file.readline()
for log_line in first_entry.split("\\n"):
    f.write(get_formatted_log_line(log_line, datetime.datetime.strptime(start_date.strip(), "%Y-%m-%d")) + "\n")
f.close()

current_date = None
current_file = None

# process the remaining lines
for line in log_file:
    try:
        # line is a date, update the file we're using
        current_date = datetime.datetime.strptime(line.strip(), "%Y-%m-%d")
        current_file = open(channel_name + os.sep + channel_name + "-" + line.strip() + ".log", "w")
    except ValueError:
        # not a date, write it to the file
        # split on the newline
        log_for_day = line.split("\\n")
        for log_line in log_for_day:
            fixed_ts = get_formatted_log_line(log_line, current_date)
            current_file.write(fixed_ts + "\n")
