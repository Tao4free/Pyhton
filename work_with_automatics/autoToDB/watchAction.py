# -*- coding:utf-8 -*-
import os, sys, shutil
import time
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
import mysql.connector

# Connect the SQL
config = {
  "user": "xxx",
  "password": "xxx",
  "host": "localhost",
  "database": "xxx",
  "raise_on_warnings": True
}

cnx = mysql.connector.connect(**config)
cursor = cnx.cursor()

# Define the directory path and file pattern for watchdog
watchPath = '.'
movePath = './data'
watchPattern = ["*.mp4"]


def getTimeLabel(filename):
    bodyname = filename.split('.')[0]
    time = bodyname.split('_')[0]
    label = bodyname.split('_')[1]
    return time, label


def pushToSQL(time, label):
    addRec = ("INSERT INTO standup_logID"
              "(time, label)"
              "VALUES (%s, %s) ON DUPLICATE KEY UPDATE label=%s")
    rec = (time, label, label)

    # Insert new employee
    cursor.execute(addRec, rec)

    # Make sure data is committed to the database
    cnx.commit()


# Override the methods related to PatternMatchingEventHandler 
class EventHandler(PatternMatchingEventHandler):
    def on_created(self, event):
        filepath = event.src_path
        filename = os.path.basename(filepath)
        fdpath = filepath.replace(filename, '')
        print('\n%sができました' % filename)
        # shutil.move(filepath, movePath)
        os.replace(filepath, os.path.join(movePath, filename))
        time, label = getTimeLabel(filename)
        # print('\n %s %s' % (time, label))
        pushToSQL(time, label)

    # def on_modified(self, event):
        # filepath = event.src_path
        # filename = os.path.basename(filepath)
        # print('%sを変更しました' % filename)

    # def on_deleted(self, event):
        # filepath = event.src_path
        # filename = os.path.basename(filepath)
        # print('\n%sを削除しました' % filename)

if __name__ == "__main__":
    # Configure event handler and Observer
    eventHandler = EventHandler(patterns=watchPattern)
    observer = Observer()
    observer.schedule(eventHandler, watchPath, recursive=False)

    # Start watching
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

    # Shutdown connection with MySQl
    cursor.close()
    cnx.close()



