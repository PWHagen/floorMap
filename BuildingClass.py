__author__ = 'Patrick'

class Building:
    def __init__(self, id, num_floors):
        self.isActive = False
        self.curr_floor = 1
        self.building_id = str(id)
        self.num_floors = num_floors

    def is_active(self):
       return self.isActive

    def activate(self):
        self.isActive = True

    def deactivate(self):
        self.isActive = False

    def update_floor(self, floor):
        self.curr_floor = int(floor)

    def current_floor(self):
        return self.curr_floor

    def building_id(self):
        return self.building_id

    def num_floors(self):
        return self.num_floors