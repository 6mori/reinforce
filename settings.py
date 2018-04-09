

class Settings():

    def __init__(self):
        # screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = ( 182, 179, 226 )

        # character settings
        self.character_width = 15
        self.character_height = 20
        #self.character_drop_speed = 1
        self.character_run_speed = 1
        self.character_gravity_acceleration = 0.02
        self.character_jumping_speed = -2

        # brick settings
        self.brick_width = 15
        self.brick_height = 20