class Workout:
    def __init__(self, workout_type, duration):

        self._workout_type = workout_type
        self._duration = duration
        self._calories_burned = self.calculate_calories()

    def get_workout_type(self):
        return self._workout_type

    def set_workout_type(self, workout_type):
        if workout_type in ['running', 'cycling', 'weightlifting', 'other']:   #modidication needed
            self._workout_type = workout_type
            self._calories_burned = self.calculate_calories() 
        else:
            raise ValueError("Invalid workout type. Choose from 'running', 'cycling', 'weightlifting', or 'other'.")

    def get_duration(self):
        return self._duration

    def set_duration(self, duration):
        if duration > 0:
            self._duration = duration
            self._calories_burned = self.calculate_calories()  
        else:
            raise ValueError("Duration must be a positive number.")

    def calculate_calories(self):
        if self._workout_type == 'running':
            return self._duration * 10  
        elif self._workout_type == 'cycling':
            return self._duration * 18   
        elif self._workout_type == 'weightlifting':
            return self._duration * 16  
        else:
            return self._duration * 5   


    def get_calories_burned(self):
        return self._calories_burned


    def get_workout_summary(self):
        return (f"Workout: {self._workout_type}, Duration: {self._duration} minutes, "
                f"Calories Burned: {self._calories_burned:.2f}")
