class Timer:
    def __init__(self, seconds=0):
        self._seconds = seconds
        self._running = False

    @property
    def seconds(self):
        return self._seconds

    @seconds.setter
    def seconds(self, value):
        if not isinstance(value, (int, float)) or value < 0:
            raise ValueError
        self._seconds = value

    @property
    def formated(self):
        hours = self._seconds // 3600
        minutes = (self._seconds - hours * 3600) // 60
        sec = (self._seconds - hours * 3600 - minutes * 60)
        return f"{hours:02d}:{minutes:02d}:{sec:02d}"

    @property
    def is_running(self):
        return self._running

    def start(self):
        self._running = True

    def stop(self):
        self._running = False

    def reset(self):
        self._running = False
        self._seconds = 0

    def tick(self):
        if self._running:
            self._seconds += 1

    def recursive_countdown(self, n):
        if n < 0:
            return
        print(n, end=" ")
        self.recursive_countdown(n-1)

    def __str__(self):
        return f"{self._running} {self.formated}"


class Alarm:
    def __init__(self):
        self._hours = 0
        self._minutes = 0
        self._alarm_set = False
        self._rining = False

    def set_alarm(self, hours, minutes):
        if not (0 <= hours <= 24 and 0 <= minutes <= 60):
            return ValueError
        self._hours = hours
        self._minutes = minutes
        self._alarm_set = True
        self._rining = False

    def check_alarm(self, current_seconds):
        if not self._alarm_set:
            return False

        current_hours = (current_seconds) // 3600
        current_minutes = (current_seconds - current_hours * 3600) // 60
        if current_hours == self._hours and current_minutes == self._minutes:
            self._rining = True
            return True
        return False

    def stop_alarm(self):
        self._rining = False

    @property
    def alarm_time(self):
        if self._alarm_set:
            return f"{self._hours}:{self._minutes}"
        return "No alarm"

    @property
    def is_rining(self):
        return self._rining

    def __str__(self):
        return f"{self.alarm_time}"


class SmartTimer(Timer, Alarm):
    def __init__(self, seconds=0):
        Timer.__init__(self, seconds)
        Alarm.__init__(self)

    def tick(self):
        if self._running:
            self._seconds += 1
            if self.check_alarm(self._seconds):
                print(f"{self.formated}")

    def snooze(self):
        self._rining = False
        self._alarm_set = True
        if 55 <= self._minutes <= 60:
            self._minutes = 60 - self._minutes
            self._hours += 1
        else:
            self._minutes += 5
        print(f"{self._hours}:{self._minutes}")

    @staticmethod
    def parse_time(self, s):
        time = s.strip().split(":")
        if len(time) != 2:
            raise ValueError
        if len(time[0].strip()) != 2 or len(time[1].strip()) != 2:
            raise ValueError
        if time[0][0] == "0":
            self._hours = int(time[0][1])
        else:
            self._hours = int(time[0])
        if time[1][0] == "0":
            self._minutes = int(time[1][1])
        else:
            self._minutes = int(time[1])

    @classmethod
    def from_string(cls, s):
        time = s.strip().split(":")
        if len(time) != 3:
            raise ValueError
        seconds = int(time[0]) * 3600 + int(time[1]) * 60 + int(time[2])
        return cls(seconds)

    @staticmethod
    def filter_active_timers(timers):
        return list(filter(lambda x: x.is_running, timers))

    @staticmethod
    def map_timers(timers):
        return list(map(lambda x: x.formated, timers))

    def __str__(self):
        return f"SmartTimer {Timer.__str__(self)} | Alarm {self.alarm_time}"


smart = SmartTimer(0)
smart.set_alarm(0, 0)

print(smart)
print("\nЗапускаем таймер на 7 секунд...")
smart.start()

for i in range(7):
    smart.tick()
    if smart.is_rining:
        print("🔔 ЗВОНИТ БУДИЛЬНИК!")
        smart.snooze()

print(f"\nПосле откладывания: {smart}")
print("\nОбратный отсчёт от 3:")
smart.recursive_countdown(3)
