# 02. Time
class Time:
    max_hours = 23
    max_minutes = 59
    max_seconds = 59

    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    # instance methods:
    def set_time(self, new_hours, new_minutes, new_seconds):
        self.hours = new_hours
        self.minutes = new_minutes
        self.seconds = new_seconds

    def get_time(self):
        self.hours = f"{self.hours}" if self.hours >= 10 else f"0{self.hours}"
        self.minutes = f"{self.minutes}" if self.minutes >= 10 else f"0{self.minutes}"
        self.seconds = f"{self.seconds}" if self.seconds >= 10 else f"0{self.seconds}"
        return f"{self.hours}:{self.minutes}:{self.seconds}"

    def next_second(self):
        self.seconds += 1
        if self.seconds > Time.max_seconds:
            self.seconds = 0
            self.minutes += 1
            if self.minutes > Time.max_minutes:
                self.minutes = 0
                self.hours += 1
                if self.hours > Time.max_hours:
                    self.hours = 0

        return Time.get_time(self)


time = Time(9, 30, 59)
print(time.next_second())
time = Time(10, 59, 59)
print(time.next_second())
time = Time(23, 59, 59)
print(time.next_second())
