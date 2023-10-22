import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from watchdog.events import PatternMatchingEventHandler
from parser import cargardatos,creararchivo,parser,scheduler

def on_created(event):
    myhandler(event.src_path)
    print("created")
def on_modified(event):
    myhandler(event.src_path)
    print("modified")
def myhandler(path):
    print("modified")
    time.sleep(1)
    parser(path)
    scheduler(path)
    print(path)
def on_moved(event):
    myhandler(event.src_path)
    print("moved")

if __name__=="__main__":
    #ruta a observar para ver si algo es modificado
    path = "C:/Users/gonza/Downloads/TFG/Parser"
    #event_handler = FileSystemEventHandler()
    event_handler = PatternMatchingEventHandler(["*.json"],path)

    event_handler.on_created=on_created
    event_handler.on_modified=on_modified
    event_handler.on_moved=on_moved

    observer = Observer()
    observer.schedule(event_handler,path)
    observer.start()
    try:
        print("monitoring")
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        print("done")
    observer.join()