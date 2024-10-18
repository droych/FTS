from workout import Workout
from health_metric import HealthMetric

class User:
    def __init__(self, name, age, weight, height):
        self._name = name
        self._age = age
        self._weight = weight
        self._height = height
        self._target_weight = None  
        self._workouts = []
        self._health_metrics = []

    def get_name(self):
        return self._name
    
    def get_age(self):
        return self._age
    
    def get_weight(self):
        return self._weight
    
    def get_height(self):
        return self._height

    def set_target_weight(self, target_weight):
        if target_weight > 0:
            self._target_weight = target_weight   # database req
        else:
            raise ValueError("Target weight must be a positive number")

    def get_target_weight(self):
        return self._target_weight

    def check_weight_goal_progress(self):
        if self._target_weight:
            difference = self._target_weight - self._weight
            if difference == 0:
                return "You have reached your target weight!"
            elif difference > 0:
                return f"You need to gain {difference:.2f} kg to reach your target weight."
            else:
                return f"You need to lose {-difference:.2f} kg to reach your target weight."
        return "No weight goal set."

    def calculate_bmi(self):
        height_in_meters = self._height / 100
        return self._weight / (height_in_meters ** 2)

    def assess_fitness_level(self):
        bmi = self.calculate_bmi()
        if bmi < 18.5:
            return "Underweight - Consider weight gain exercises like strength training."
        elif 18.5 <= bmi < 24.9:
            return "Normal weight - Maintain with a balanced routine of cardio and strength training."
        elif 25 <= bmi < 29.9:
            return "Overweight - Consider weight loss exercises like cardio, running, or cycling."
        else:
            return "Obese - Consult a healthcare provider and focus on low-impact exercises like walking or swimming."

    def get_exercise_suggestions(self):
        fitness_level = self.assess_fitness_level()
        if "Underweight" in fitness_level:
            return "Suggested Exercises: Weightlifting, Strength Training, Protein-rich diet."
        elif "Normal weight" in fitness_level:
            return "Suggested Exercises: Running, Cycling, Balanced diet."
        elif "Overweight" in fitness_level:
            return "Suggested Exercises: Cardio (Running, Cycling), HIIT."
        else:
            return "Suggested Exercises: Walking, Low-impact cardio, Swimming."

    def add_workout(self, workout):
        self._workouts.append(workout)

    def add_health_metrics(self, health_metric):
        self._health_metrics.append(health_metric)

    def get_fitness_summary(self):       
        total_calories = sum([workout._calories_burned for workout in self._workouts])  #not being used here rn
        total_steps = sum([metric._steps for metric in self._health_metrics])
        avg_heart_rate = (sum([metric.heart_rate for metric in self._health_metrics]) /
                          len(self._health_metrics)) if self._health_metrics else 0

        weight_goal_progress = self.check_weight_goal_progress()
        fitness_level = self.assess_fitness_level()
        exercise_suggestions = self.get_exercise_suggestions()

        return (
                f"Fitness Level: {fitness_level}\n"
                f"Weight Goal Progress: {weight_goal_progress}\n"
                f"Exercise Suggestions: {exercise_suggestions}")
    def view_fitness_summary(self):   #replicated need to modify 
        total_calories = sum([workout._calories_burned for workout in self._workouts])
        total_steps = sum([metric.steps for metric in self._health_metrics])
        avg_heart_rate = (sum([metric.heart_rate for metric in self._health_metrics]) /
                          len(self._health_metrics)) if self._health_metrics else 0

       

        return (f"Total Calories Burned: {total_calories:.2f}, Total Steps: {total_steps}, "
                f"Average Heart Rate: {avg_heart_rate:.2f}\n"
              )
