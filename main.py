from app import App
from workout import Workout
from health_metric import HealthMetric

def main():
    app = App()

    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    weight = float(input("Enter your current weight (kg): "))
    height = float(input("Enter your height (cm): "))

    print(app.register_user(name, age, weight, height))

    set_goal = input("Do you want to set a goal? (yes/no): ").strip().lower()
    if set_goal == 'yes':
        target_weight = float(input("Enter your goal weight: ")) # pending task---> need to add feature
        print(app.set_weight_goal(name, target_weight))
    elif set_goal == 'no':
        print("No weight goal set.")
    else:
        print("Invalid input. Proceeding without setting a weight goal.")

    while True:
        print("\nMenu:")
        print("1. Log a workout")
        print("2. Log health metrics")
        print("3. View fitness summary")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            workout_type = input("Enter workout type (e.g., running, cycling): ")
            duration = float(input("Enter duration of workout in minutes: "))
            workout = Workout(workout_type, duration)
            print(app.log_workout(name, workout))

        elif choice == "2":
            steps = int(input("Enter number of steps taken: "))
            heart_rate = float(input("Enter average heart rate: ")) 
            sleep_hours = float(input("Enter number of hours slept: "))
            hydration = float(input("Enter amount of water consumed (in liters): "))
            health_metric = HealthMetric(steps, heart_rate, sleep_hours, hydration)
            print(app.log_health_metrics(name, health_metric))

        elif choice == "3":
            print(app.generate_user_report(name))

        elif choice == "4":
            print("Exiting the app. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":   
    main()