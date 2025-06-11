import random
import time
import pyttsx3



engine=pyttsx3.init()

voices=engine.getProperty('voices')

engine.setProperty('voice',voices[0].id)# voices[0] = male, [1] = female (usually)

engine.setProperty('rate',150)# Speed (default ~200)
engine.setProperty('volume', 1.0)  # Volume (0.0 to 1.0)


def speak(text):
    print(text)
    engine.say(text)
    engine.runAndWait()



user_score=0
computer_score=0
rounds=3


speak(" Welcome to Rock-Paper-Scissors!")
speak("Hello Harshithasc! I am your assistant for this game.")
speak(f" First to win {rounds} rounds take the trophy!\n")
time.sleep(1)

choices=["rock","paper","scissors"]

baised_choices = {
    "rock": ["scissors", "scissors", "rock", "paper"],      # 50% win
    "paper": ["rock", "rock", "paper", "scissors"],
    "scissors": ["paper", "paper", "scissors", "rock"]
}

for i in range(1,rounds+1):
    print(f"-------Round{i}-------")
    speak("Your turn! Choose: Rock, Paper, or Scissors")

    user_choice=input("👉 You: ").strip().lower()
    while user_choice not in choices:
        user_choice=input("❌ Invalid choice. Try again: ").strip().lower()

    comp_choice=random.choice(baised_choices[user_choice])
    speak(f"Computer choose:{comp_choice}")
    time.sleep(0.5)

    if user_choice==comp_choice:
        speak("Its a tie!")

    elif(user_choice=="rock" and comp_choice=="scissors")or \
        (user_choice=="scissors" and comp_choice=="paper")or \
        (user_choice=="paper" and comp_choice=="rock"):
        speak(" You win this round!")
        user_score += 1

    else:
        speak(" Computer wins this round!")
        computer_score += 1

    speak(f"Score: You-{user_score} and Computer-{computer_score}\n")
    time.sleep(1)


speak(" Game Over! ")
speak(f" You: {user_score} \n  Computer: {computer_score}")
if user_score>computer_score:
    speak(" Congratulations! You beat the computer!")
elif computer_score>user_score:
    speak(" The computer wins! Better luck next time.")
else:
    speak(" It's a draw! You both played well.")

speak("Thanks for playing!")