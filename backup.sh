#!/bin/bash

dt=$(date +%Y-%m-%d-%H-%M-%S)
home_dir=/opt/data
backup_dir=/app/backup

if [ -d $backup_dir ];
then
	echo "Backup directory present"
else
	echo "backup directory creating"
	mkdir -p /app/backup
fi

backup_dir_check=/app/backup/$dt

echo $backup_dir_check

if [ -d $backup_dir_check ];
then
	echo "backup directory check passed"
else
	echo "creatig backup_dir_check"
	mkdir -p $backup_dir_check
fi


cp -r $home_dir/* $backup_dir_check

ls -lrth $backup_dir_check


