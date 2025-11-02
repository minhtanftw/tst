import time
import subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class TestRunner(FileSystemEventHandler):
    def on_modified(self, event):
        if  event.src_path.endswith(".py"):
            print("\n FIle changed:", event.src_path)
            print("Running test")
            subprocess.run(["pytest","-v"])

if __name__ == "__main__":
    path = '.'
    event_handler = TestRunner()
    observer = Observer()
    observer.schedule(event_handler, path = path , recursive= True)
    observer.start()

    print(" Watching for changes... (Press Ctrl+C to stop)\n")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()