import schedule
import time

def task():
    print("Task executed")

def task2():
    print("working on Task2....")
    time.sleep(1)
    print('Task2 completed.')

# Schedule the task for a specific date and time
scheduled_date_time = "2024-04-27 16:22:00"  # Example: "YYYY-MM-DD HH:MM:SS"
# schedule.every().day.at(scheduled_date_time).do(task)
schedule.every(1).minutes.do(task)
schedule.every().day.at("16:45:00").do(task2)

# Run the scheduler
while True:
    schedule.run_pending()
    time.sleep(1)
