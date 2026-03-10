# 19-coundown-timer-program
# Countdown Timer - Simple Version (No Functions/Classes)

import time

print("=== COUNTDOWN TIMER ===")
print()

# Get the starting number from user
start_number = int(input("Enter the number to countdown from: "))

print(f"\nStarting countdown from {start_number}...")
print("Press Ctrl+C to stop the countdown anytime.\n")

# Add a brief pause before starting
time.sleep(1)

# Countdown loop - goes from start_number down to 0
current_number = start_number

while current_number >= 0:
    if current_number == 0:
        print("🎉 TIME'S UP! 🎉") #windows + ; to get emoji window.
        # Play a "beep" sound effect with text
        for i in range(3):
            print("BEEP!")
            time.sleep(0.3)
    else:
        print(f"{current_number}")
        time.sleep(1)  # Wait 1 second
    
    current_number -= 1  # Decrease by 1

print("\n" + "="*30)
print("Countdown completed!")
print("="*30)
