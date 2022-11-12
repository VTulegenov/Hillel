from home21 import auto
import time

class track(auto):
    max_load = True
    def move(self):
        print('attention')
        super().move()

    def load(self, max_load):
        self.max_load = max_load
        time.sleep(1)
        print(max_load)
        time.sleep(1)


class car(auto):
    max_speed = True
    def move(self, max_speed):
        self.max_speed = max_speed
        super().move()
        print('max speed is ' + max_speed)


track_1 = track('brand', 1, 'mark')
track_1.move()
track_1.load('load')
car_1 = car('brand', 1, 'mark')
car_1.move("max_speed")

