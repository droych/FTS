from user import User  

class App:
    def __init__(self):
        self._users = []

    def register_user(self, name, age, weight, height):
        user = User(name, age, weight, height)
        self._users.append(user)
        return f"User {name} registered successfully."

    def find_user(self, user_name):
        for user in self._users:
            if user.get_name() == user_name:
                return user
        return None

    def log_workout(self, user_name, workout):
        user = self.find_user(user_name)
        if user:
            user.add_workout(workout)
            return f"Workout logged for {user_name}."
        return "User not found."

    def log_health_metrics(self, user_name, health_metric):
        user = self.find_user(user_name)
        if user:
            user.add_health_metrics(health_metric)

            total_calories_from_steps = health_metric.calories_burned_from_steps()


            total_calories_from_workouts = sum([workout.get_calories_burned() for workout in user._workouts])

            total_calories = total_calories_from_steps + total_calories_from_workouts
            total_steps = sum([metric.get_steps() for metric in user._health_metrics])
            avg_heart_rate = (sum([metric.get_heart_rate() for metric in user._health_metrics]) /
                            len(user._health_metrics)) if user._health_metrics else 0

            return (f"Health metrics logged for {user_name}. "
                    f"Total Calories Burned: {total_calories:.2f}, Total Steps: {total_steps}, "
                    f"Average Heart Rate: {avg_heart_rate:.2f}\n")

        return "User not found."


    def set_weight_goal(self, user_name, target_weight):
        user = self.find_user(user_name)
        if user:
            user.set_target_weight(target_weight)
            return f"Target weight set to {target_weight:.2f} kg for {user.get_name()}."
        return "User not found."

    def generate_user_report(self, user_name):
        user = self.find_user(user_name)
        if user:
            bmi = user.calculate_bmi()
            fitness_summary = user.get_fitness_summary()
            return (f"User: {user.get_name()}, Age: {user.get_age()}, BMI: {bmi:.2f}\n"
                    f"{fitness_summary}")
        return "User not found."
