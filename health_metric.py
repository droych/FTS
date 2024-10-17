class HealthMetric:
    def __init__(self, steps=0, heart_rate=0, sleep_hours=0, hydration=0):
        self._steps = steps
        self._heart_rate = heart_rate
        self._sleep_hours = sleep_hours
        self._hydration = hydration
    
    def calories_burned_from_steps(self):
        return self._steps * 0.05 

    def track_steps(self, step_count):
        self._steps = step_count

    def track_sleep(self, hours):
        self._sleep_hours = hours

    def track_hydration(self, amount):
        self._hydration = amount

    def get_steps(self):
        return self._steps

    def get_heart_rate(self):
        return self._heart_rate

    def get_sleep_hours(self):
        return self._sleep_hours

    def get_hydration(self):
        return self._hydration

    def get_health_summary(self):
        return (f"Steps: {self._steps}, Heart Rate: {self._heart_rate}, "
                f"Sleep: {self._sleep_hours} hours, Hydration: {self._hydration} liters")
