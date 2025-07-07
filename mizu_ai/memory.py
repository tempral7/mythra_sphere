class Memory:
    def __init__(self):
        # start with an empty dict
        self.store = {}

    def set(self, key, value):
        """Store a value by key."""
        self.store[key] = value

    def get(self, key, default=None):
        """Retrieve a value, or return default."""
        return self.store.get(key, default)

    def clear(self):
        """Wipe all stored data."""
        self.store = {}