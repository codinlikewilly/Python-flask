import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from utilities.LogHandler import get_logger

logger = get_logger(__name__)


class DirectoryWatcher:
    DIRECTORY_TO_WATCH = "./reports"
    logger.info(f"Monitoring {DIRECTORY_TO_WATCH}")

    def __init__(self):
        self.observer = Observer()

    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, self.DIRECTORY_TO_WATCH, recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(5)
        except:
            self.observer.stop()
            logger.exception("An Error occurred while processing.")
            print("Error")

        self.observer.join()


class Handler(FileSystemEventHandler):

    @staticmethod
    def on_any_event(event):
        print(event)
        if event.is_directory:
            return None

        elif event.event_type == 'created':
            # Take any action here when a file is first created.
            print("Received created event - %s." % event.src_path)
            logger.info(f"new file detected: {event.src_path}")
            return event.src_path

        elif event.event_type == 'modified':
            # Taken any action here when a file is modified.
            logger.info(f"file was modified: {event.src_path}")
            print("Received modified event - %s." % event.src_path)

        elif event.event_type == 'deleted':
            logger.info(f"file was deleted: {event.src_path}")
            print("file deleted")
        else:
            print("Weird event")
