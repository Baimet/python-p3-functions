#!/usr/bin/env python3

def greet_programmer():
    greet_programmer="Hello, programmer!"
    print(greet_programmer)

greet_programmer()

def greet(name="Naureen"):
    print(f"Hello, {name}!")

greet()

def greet_with_default(name="programmer"):
    print(f"Hello, {name}!")

greet_with_default("Sunny")

def add(num1=1, num2=2):
    return num1 + num2
add()

def halve(number=4):
    return number/2
halve()
