from belt import Belt

class Leftbelt(Belt):
    def __init__(self, level: int, speed:float = 1.5, start_x: int = 0,
                 end_x: int = 250):
        super().__init__(level = level, direction= "left", speed = speed,
                         start_x= start_x, end_x = end_x)