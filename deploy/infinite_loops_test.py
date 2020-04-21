import time
import signal


class PeopleSalary:
    def __init__(self, name, age, salary):
        self.name = name;
        self.age = age;
        self.salary = salary

    def Junior_assistant(self, salary):
        bonus = salary * 0.3
        print(f'your bonus is {bonus}.Your Grand Total is{salary + bonus}')


def signal_handler(signal, frame):
    global interrupted
    interrupted = True


signal.signal(signal.SIGINT, signal_handler)

interrupted = False

while True:

    s = input('Enter your Name:')
    age = int(input('your age:'))
    salary = int(input('your salary: '))

    if age < 25:
        worker1 = PeopleSalary(s, age, salary)
        worker1.Junior_assistant(salary)
    time.sleep(3)

    if interrupted:
        print("Gotta go")
        break

