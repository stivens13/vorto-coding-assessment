class Load:
    def __init__(self, load_id, pickup, dropoff):
        self.load_id = load_id
        self.pickup = pickup
        self.dropoff = dropoff

    def __repr__(self):
        return f"Load({self.load_id}, {self.pickup}, {self.dropoff})"

