# mongodump
Dump a MongoDB database.

## Config example
```
DB_HOST = '127.0.0.1'
DB_PORT = '27017'
DB_NAME = 'dbname'
BACKUP_PATH = '/home/user/dbname/'
```
Note : The `/` at the end of `BACKUP_PATH` is **important**.

## Allow executable
```
chmod +x mongodump.py
```

## Cron job daily example
```
20 0 * * * /usr/bin/python3 /home/user/mongodump.py > /home/user/mongodump.log
```

## Cron job to clean up the mongodump log
```
0 1 * * sun echo "empty" > /home/user/mongodump.log
```
