from utils.excercises import char_counter, episode_locations
from utils.response import ResponseManager
from utils.timer import Timer


timer_cc = Timer()
timer_el = Timer()


# Char counter
timer_cc.start()
results_cc = char_counter()
timer_cc.stop()
response_cc = ("Char counter", timer_cc.get_time(), results_cc)

# Episode locations
timer_el.start()
results_el = episode_locations()
timer_el.stop()
response_el = ("Episode locations", timer_el.get_time(), results_el)

# Response generation
response = ResponseManager([response_cc, response_el])
response.dump()