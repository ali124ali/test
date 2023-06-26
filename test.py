from time import sleep

for i in range(10):
    print('line number: {}'.format(i))
    sleep(2)

def say_hello(name):
    return f"HEllo {name}"
