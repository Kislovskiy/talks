class Option:
    def get_or_else(self, default):
        return self.value if isinstance(self, Some) else default

class Some(Option):
    def __init__(self, value):
        self.value = value

class Nothing(Option):
    pass
