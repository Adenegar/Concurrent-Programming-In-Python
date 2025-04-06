import threading
import time

def count():
    print("One")
    time.sleep(1)
    print("Two")

def main():
    threads = []
    # Start threads
    for _ in range(3):
        thread = threading.Thread(target=count)
        threads.append(thread)
        thread.start()
    
    # Stop threads
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()
