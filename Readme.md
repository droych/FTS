# Fitness Tracker System

## Objective:
The Fitness Tracker System is a Python-based program designed to help users monitor their daily activities, workouts, and health metrics using object-oriented programming (OOP) principles.

---

## Features Overview:

### 1. **Workout Class**
   - **Attributes**:
     - `workout_type` (string): Represents the type of workout (e.g., running, cycling, weightlifting).
     - `duration` (float): Duration of the workout in minutes.
     - `calories_burned` (float): The number of calories burned during the workout.
   - **Methods**:
     - `calculate_calories()`: Calculates calories burned based on workout type and duration.
     - `get_workout_summary()`: Provides a summary of the workout including workout type, duration, and calories burned.

### 2. **HealthMetric Class**
   - **Attributes**:
     - `steps` (integer): The number of steps taken in a day.
     - `heart_rate` (float): The average heart rate during the day.
     - `sleep_hours` (float): The number of hours slept.
     - `hydration` (float): The amount of water consumed in liters.
   - **Methods**:
     - `track_steps(step_count)`: Updates the step count.
     - `track_sleep(hours)`: Updates the number of hours slept.
     - `track_hydration(amount)`: Updates the hydration level.
     - `get_health_summary()`: Provides a summary of the health metrics for the day.

### 3. **User Class**
   - **Attributes**:
     - `name` (string): The name of the user.
     - `age` (integer): The age of the user.
     - `weight` (float): The weight of the user.
     - `height` (float): The height of the user.
     - `workouts` (list of Workout objects): A list of the user’s completed workouts.
     - `health_metrics` (list of HealthMetric objects): A list of the user’s daily health metrics.
   - **Methods**:
     - `add_workout(workout)`: Adds a new workout to the user's workout log.
     - `add_health_metrics(health_metric)`: Logs daily health metrics for the user.
     - `calculate_bmi()`: Calculates and returns the user’s Body Mass Index (BMI) using their weight and height.
     - `get_fitness_summary()`: Provides an overview of all workouts and health metrics, including total calories burned, average heart rate, and step count for the week.

### 4. **App Class**
   - **Attributes**:
     - `users` (list of User objects): A list of all users registered in the system.
   - **Methods**:
     - `register_user(name, age, weight, height)`: Registers a new user by creating a User object.
     - `log_workout(user_name, workout)`: Logs a workout for a specific user.
     - `log_health_metrics(user_name, health_metric)`: Logs health metrics for a specific user.
     - `generate_user_report(user_name)`: Generates a detailed report for a user, showing their workouts, health metrics, and BMI.

---

## Additional Features:

### 1. **Calories Burned Calculation**
   - The `Workout` class uses customized formulas to calculate calories burned based on the workout type and intensity. For instance:
     - **Running**: Calories burned = `duration * 10`.
     - **Cycling**: Calories burned = `duration * 18`.
     - **Weightlifting**: Calories burned = `duration * 16`.
     - **Other workouts**: Calories burned = `duration * 5`.

### 2. **Progress Tracking** #pending
   - The system tracks the user’s progress towards fitness goals such as:
     - **Daily Step Count**: Logs the number of steps taken each day.
     - **Calorie Burn Goal**: Tracks the number of calories burned based on workouts.
   - The fitness summary also shows the user’s progress towards weight goals (if set).

### 3. **Weekly Summary** #still pending 
   - A feature that provides users with a weekly summary of:
     - Total calories burned.
     - Average heart rate.
     - Total steps taken.
     - Sleep and hydration statistics.
     - Progress towards any fitness goals.

### 4. **Exercise Suggestions**
   - Based on a user’s BMI and fitness data, the system provides exercise suggestions to help users improve their fitness levels. For example:
     - **Underweight**: Suggests weight-gain exercises like weightlifting or strength training.
     - **Overweight**: Suggests calorie-burning exercises like running or cycling.

### 5. **Goal Setting** (Optional Advanced Feature)
   - Users can set personal fitness goals, such as:
     - A specific target weight to reach.
     - A step goal for the day or week.
     - A calorie burn target.
   - The system tracks the user’s progress and updates their fitness summary with how close they are to achieving these goals.

### 6. **Notifications** (Optional Advanced Feature) #in future
   - Users receive notifications when they meet or fail to meet their fitness goals (e.g., reaching a daily step count or calorie burn goal).

### 7. **Workout Plans** (Optional Advanced Feature) #in future
   - Users can create predefined workout plans that they can follow over a period of time, and the system tracks their progress.

---

## Sample User Flow:
1. **User Registration**: The user registers by providing their name, age, weight, and height. The system calculates and stores their BMI.
2. **Logging Workouts**: Users log their workouts, and the system automatically calculates the calories burned based on workout type and duration.
3. **Logging Health Metrics**: Users can input their daily health data such as steps, heart rate, sleep, and hydration.
4. **Viewing Reports**: Users can view detailed fitness summaries that include total steps, calories burned, BMI, heart rate, and progress towards goals.
5. **Setting Goals**: Users can optionally set weight goals or calorie burn goals, which the system will track.
6. **Weekly Overview**: At the end of each week, users receive a summary of their workouts and health metrics for the week.

---

## Technologies Used:
- **Programming Language**: Python
- **Concepts**: Object-Oriented Programming (OOP)

---
