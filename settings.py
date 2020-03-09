class Settings():

    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_colour = (230, 230, 230)
        
        self.ship_speed_factor = 10
        
        self.bullet_speed = 15
        self.bullet_width = 5
        self.bullet_height = 15
        self.bullet_colour = (60, 60, 60)
        self.bullets_allowed = 5
        
        self.alien_speed_factor = 5
        self.ship_limit = 3
        self.alien_drop_speed = 10
        self.speedup_scale = 1.5
        self.fleet_direction = 1
        
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed_factor = 3.5
        self.bullet_speed = 5
        self.alien_speed_factor = 1
        self.fleet_direction = 1
    
    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_drop_speed *= self.speedup_scale