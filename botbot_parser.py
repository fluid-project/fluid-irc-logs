#!/usr/bin/env python

import datetime

log_file_name = "fluid-design.log"

# Start date of the logs, th first line will be for this date
start_date = "2018-09-20"

# Open the file

# Parse it by day

# Dump the botbot log format to an individual file by date

log_file = open(log_file_name, "r")

# print the first line to file based on the entered start_date

f = open("fluid-design-" + start_date + ".log", "w")
f.write(log_file.readline())
f.close()

current_date = None
current_file = None

for line in log_file:
    try:
        # line is a date, update the file we're using
        current_date = datetime.datetime.strptime(line.strip(), "%Y-%m-%d")
        current_file = open("fluid-design-" + line.strip() + ".log", "w")
    except ValueError:
        # not a date
        current_file.write(line)
