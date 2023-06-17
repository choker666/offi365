import time

def clock_focused_timer(duration):
    remaining_time = duration * 60  # Convert duration to seconds

    while remaining_time > 0:
        minutes = remaining_time // 60
        seconds = remaining_time % 60
        time_str = f"{minutes:02d}:{seconds:02d}"
        print(f"Time remaining: {time_str}", end="\r")
        time.sleep(1)
        remaining_time -= 1

    print("Time's up!")

# Set the duration in minutes
duration = 25  # 25 minutes

# Run the clock-focused timer
clock_focused_timer(duration)
