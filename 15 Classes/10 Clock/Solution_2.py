class Clock:
    def __init__(self, hour, minute):
        self.hour, self.minute = None, None
        self.normalize(hour, minute)

    def __repr__(self):
        return f'Clock({self.hour}, {self.minute})'

    def __str__(self):
        return f'{self.hour:02d}:{self.minute:02d}'

    def __eq__(self, other):
        if isinstance(other, Clock):
            if self.__repr__() == other.__repr__():
                return True

    def __add__(self, minutes):
        self.normalize(self.hour, self.minute, minutes)
        return Clock(self.hour, self.minute)

    def __sub__(self, minutes):
        self.normalize(self.hour, self.minute, -minutes)
        return Clock(self.hour, self.minute)

    def normalize(self, hour, minute, extra_minutes=0):
        minute = minute + extra_minutes
        if minute < 0 or minute > 59:
            self.minute = minute % 60
            hour += minute // 60
        else:
            self.minute = minute

        if hour < 0 or hour > 23:
            self.hour = hour % 24
        else:
            self.hour = hour
