import time

print("Press Ctrl+C to stop the clock.\n")

try:
    while True:
        print(time.strftime("%H:%M:%S"), end="\r")
        time.sleep(1)
except KeyboardInterrupt:
    print("\nClock stopped.")
