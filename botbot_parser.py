#!/usr/bin/env python

"""
Usage:

python botbot_parser.py [log_file_name] [channel_name] [start_date]

ex: python botbot_parser.py fluid-design.log fluid-design 2018-09-20

"""

import datetime
import sys
import os

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
f.write(log_file.readline())
f.close()

current_date = None
current_file = None

for line in log_file:
    try:
        # line is a date, update the file we're using
        current_date = datetime.datetime.strptime(line.strip(), "%Y-%m-%d")
        current_file = open(channel_name + os.sep + channel_name + "-" + line.strip() + ".log", "w")
    except ValueError:
        # not a date, write it to the file
        current_file.write(line.strip().replace("\\n", "\n"))
