# Fitness Tracker System

## Objective

Design and implement a **Python-based Fitness Tracker System** that helps users monitor their daily activities, workouts, and health metrics using **OOP principles**.

## Features

### 1. Workout Class

- **Attributes:**

  - `workout_type`: The type of workout (e.g., running, cycling, weightlifting).
  - `duration`: Duration of the workout in minutes.
  - `calories_burned`: The number of calories burned during the workout.

- **Methods:**
  - `calculate_calories()`: Calculates calories burned based on workout type and duration.
  - `get_workout_summary()`: Returns a summary of the workout including type, duration, and calories burned.

### 2. HealthMetric Class

- **Attributes:**

  - `steps`: Number of steps taken in a day.
  - `heart_rate`: Average heart rate during the day.
  - `sleep_hours`: Number of hours slept.
  - `hydration`: Amount of water consumed (in liters).

- **Methods:**
  - `track_steps(step_count)`: Updates the step count.
  - `track_sleep(hours)`: Updates sleep hours.
  - `track_hydration(amount)`: Updates hydration level.
  - `get_health_summary()`: Returns a summary of health metrics for the day.

### 3. User Class

- **Attributes:**
  - `name`: User's name.
  - `age`: User's age.
  - `weight`: User's weight.
  - `height`: User's height.
  - `workouts`: A list of the user's completed workouts.
  - `health_metrics
