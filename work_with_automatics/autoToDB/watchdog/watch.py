# -*- coding:utf-8 -*-
# 参考になったリンク
# https://pypi.org/project/watchdog/
# https://stackoverflow.com/questions/22736481/ignoring-files-with-watchdog
# https://stackoverflow.com/questions/19522567/how-to-ignore-files-starting-with-a-period-using-watchmedo/19602316
# https://stackoverflow.com/questions/16261425/monitoring-a-single-file/16261529#16261529

import os, sys
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from watchdog.events import PatternMatchingEventHandler
from watchdog.events import RegexMatchingEventHandler

# Override the methods related to PatternMatchingEventHandler 
class EventHandler(PatternMatchingEventHandler):
    def on_created(self, event):
        filepath = event.src_path
        filename = os.path.basename(filepath)
        print('\n%sができました' % filename)

    # def on_modified(self, event):
        # filepath = event.src_path
        # filename = os.path.basename(filepath)
        # print('%sを変更しました' % filename)

    def on_deleted(self, event):
        filepath = event.src_path
        filename = os.path.basename(filepath)
        print('\n%sを削除しました' % filename)

if __name__ == "__main__":
    # Define the directory path and file pattern for watchdog
    watchPath = '.'
    watchPattern = ["*.mp4"]

    # Configure event handler and Observer
    eventHandler = EventHandler(patterns=watchPattern)
    observer = Observer()
    observer.schedule(eventHandler, watchPath, recursive=True)

    # Start watching
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
