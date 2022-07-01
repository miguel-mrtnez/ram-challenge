import sys
from os.path import dirname as up
import unittest
from time import sleep

dir = up(up(__file__))
sys.path.append(dir)
from utils.timer import Timer


class TestTimer(unittest.TestCase):
    
    def test_minimum(self):
        """
        The timer should not be less than the excecution time.
        """
        time = 2
        timer = Timer()
        timer.start()
        sleep(time)
        timer.stop()
        assert timer.get_time() >= time

    def test_maximum(self):
        """
        Timer should not exceed the maximum time by more than 0.5 seconds.
        """
        time = 2
        timer = Timer()
        timer.start()
        sleep(time)
        timer.stop()
        assert timer.get_time() <= time + 0.5


if __name__ == '__main__':
    unittest.main()