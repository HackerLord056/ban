import pyttsx3
from datetime import date
from datetime import datetime

while True:
    robot_mouth = pyttsx3.init()
    robot_brain = ""
    robot_waiting = ""
    robot_mouth_waiting = pyttsx3.init()
    robot_brain_waiting = "I'm waiting your next text."
    today1 = date.today()
    today2 = date.today()
    time = datetime.now()
    a = 0
    user_text = input('User: ')


    if "Hello" in user_text:
        print("Robot: Hello! Tran Gia Huy.")
        robot_brain = "Hello! Tran Gia Huy."
        a = 1

    elif "hi" in user_text:
        print("Robot: Hello! Tran Gia Huy.")
        robot_brain = "Hello! Tran Gia Huy."
        a = 1

    elif "Hi" in user_text:
        print("Robot: Hello! Tran Gia Huy.")
        robot_brain = "Hello! Tran Gia Huy."
        a = 1

    elif "hello" in user_text:
        print("Robot: Hello! Tran Gia Huy.")
        robot_brain = "Hello! Tran Gia Huy."
        a = 1

    elif "today" in user_text:
        today1 = today1.strftime("%d/%m/%Y.")
        print("Today is :", today1)
        robot_brain = today2.strftime("%B %d, %Y.")
        a = 1

    elif "Today" in user_text:
        today1 = today1.strftime("%d/%m/%Y.")
        print("Today is :", today1)
        robot_brain = today2.strftime("%B %d, %Y.")
        a = 1

    elif "time" in user_text:
        print("Now is: ", time)
        robot_brain = time.strftime("%H hours %M minutes %S seconds.")
        a = 1

    elif "Time" in user_text:
        print("Now is: ", time)
        robot_brain = time.strftime("%H hours %M minutes %S seconds.")
        a = 1

    elif "thank" in user_text:
        print("Robot: No problem.")
        robot_brain = "No problem."
        a = 1

    elif "Thank" in user_text:
        print("Robot: No problem.")
        robot_brain = "No problem."
        a = 1
    
    elif "How are you" in user_text:
        print("I'm fine thank you. And you?")
        robot_brain = "I'm fine thank you. And you?"
        a = 1

    elif "how are you" in user_text:
        print("I'm fine thank you. And you?")
        robot_brain = "I'm fine thank you. And you?"
        a = 1

    elif "Nice" and "meet you" in user_text:
        print("Robot: Nice to meet you, too.")
        robot_brain = "Nice to meet you, too."
        a = 1
    elif "nice" and "meet you" in user_text:
        print("Robot: Nice to meet you, too.")
        robot_brain = "Nice to meet you, too."
        a = 1
    elif "nice" and "Meet you" in user_text:
        print("Robot: Nice to meet you, too.")
        robot_brain = "Nice to meet you, too."
        a = 1
    elif "Nice" and "Meet you" in user_text:
        print("Robot: Nice to meet you, too.")
        robot_brain = "Nice to meet you, too."
        a = 1

    elif "What is your name" in user_text:
        print("I'm GiTr_H.")
        robot_brain = "I'm GiTr_H."
        a = 1

    elif "what is your name" in user_text:
        print("I'm GiTr_H.")
        robot_brain = "I'm GiTr_H."
        a = 1

    elif "Bye" in user_text:
        print("Goodbye, Tran Gia Huy!")
        robot_brain = "Goodbye, Tran Gia Huy!"
        a = 2

    elif "bye" in user_text:
        print("Goodbye, Tran Gia Huy!")
        robot_brain = "Goodbye, Tran Gia Huy!"
        a = 2

    elif "American" and "president" in user_text:
        print("Joe Bidden.")
        robot_brain = "Joe Bidden."
        a = 1

    elif "american" and "president" in user_text:
        print("Joe Bidden.")
        robot_brain = "Joe Bidden."
        a = 1

    elif "american" and "President" in user_text:
        print("Joe Bidden.")
        robot_brain = "Joe Bidden."
        a = 1

    elif "American" and "President" in user_text:
        print("Joe Bidden.")
        robot_brain = "Joe Bidden."
        a = 1

    else:
        print("I can't understand you. Please try again!")
        robot_brain = "I can't understand you. Please try again!"
        a = 1


    robot_mouth.say(robot_brain)
    robot_mouth_waiting.say(robot_brain_waiting)
    robot_mouth.runAndWait()
    robot_mouth_waiting.runAndWait()


    if a == 1:
        print(robot_brain_waiting)
        robot_brain = robot_brain_waiting
        robot_waiting = robot_brain_waiting
    elif a == 2:
        break