# greeter.py
import art


def greet(message: str) -> None:
    print(art.text2art(message, font="cybermedium"))