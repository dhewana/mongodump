#!/usr/bin/python3

import os
import time
import datetime

DB_HOST = ''
DB_PORT = ''
DB_NAME = ''
BACKUP_PATH = ''

DATETIME = time.strftime('%Y%m%d-%H%M%S')
print ("DATETIME: " + DATETIME + "\n")

TODAYBACKUPPATH = BACKUP_PATH + DATETIME
print (time.strftime('%Y%m%d-%H%M%S') + " - Creating TODAYBACKUPPATH '" + TODAYBACKUPPATH + "' ...")
if not os.path.exists(TODAYBACKUPPATH):
    os.makedirs(TODAYBACKUPPATH)
print (time.strftime('%Y%m%d-%H%M%S') + " - TODAYBACKUPPATH '" + TODAYBACKUPPATH + "' created.\n")

print (time.strftime('%Y%m%d-%H%M%S') + " - Starting to backup database '" + DB_NAME + "' ...")
dump_cmd = "mongodump --host " + DB_HOST + " --port " + DB_PORT + " --out " + TODAYBACKUPPATH + " --db " + DB_NAME + " --gzip"
os.system(dump_cmd)
print (time.strftime('%Y%m%d-%H%M%S') + " - Backup of database '" + DB_NAME + "' completed.\n")

print (time.strftime('%Y%m%d-%H%M%S') + " - Backup script completed, your backup has been created in '" + TODAYBACKUPPATH + "' directory.\n")

print (time.strftime('%Y%m%d-%H%M%S') + " - Deleting backup files older than 7 days...")
rmgz = "find " + BACKUP_PATH + "* -type d -ctime +1 -exec rm -rf {} \;"
os.system(rmgz)
print (time.strftime('%Y%m%d-%H%M%S') + " - Backup files older than 7 days deleted.\n")
