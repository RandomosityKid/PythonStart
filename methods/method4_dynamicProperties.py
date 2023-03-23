import time

class Timestamp:
    @property
    def current_time(self):
        return time.time()

if __name__ == '__main__':
    timestamp = Timestamp()
    print(timestamp.current_time)
    time.sleep(3)
    print(timestamp.current_time)