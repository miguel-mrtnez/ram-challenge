from time import perf_counter, sleep


class Timer:

    def start(self):
        self.star_time = perf_counter()

    def stop(self):
        self.stop_time = perf_counter()
        self.time = self.stop_time - self.star_time
    
    def get_time(self):
        return self.time


if __name__ == '__main__':
    timer = Timer()
    start = timer.start()
    sleep(5)
    end = timer.stop()
    print("Time:", str(timer.get_time()))