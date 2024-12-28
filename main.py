import time
import random

def show_funny_message():
    messages = [
        "Hey buddy! Buy the software or you'll work like in stone age 🦖",
        "Only today and right now - 146% discount on the coolest software! 🔥",
        "Psst... Want awesome software for the price of a coffee? ☕",
        "Alert! User without license detected. Urgent upgrade required! 🚨", 
        "Buy software - get second one free! (just kidding, there's no second one) 🎁"
    ]
    
    print("\n=== Important Message ===")
    for _ in range(3):
        message = random.choice(messages)
        print(message)
        time.sleep(1)
    
    print("\nPress Y to buy, N to continue living with pirated version 🏴‍☠️")
    choice = input().lower()
    
    if choice == 'y':
        print("Great choice! Proceeding to payment...")
        time.sleep(1)
        print("💳 Price: $9999.99")
    else:
        print("Your loss! I'll pop up every hour until you buy 😈")

if __name__ == "__main__":
    show_funny_message()
