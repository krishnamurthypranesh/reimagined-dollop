import time

def scheduler(wait):
    def outer(func):
        def inner(*args, **kwargs):
            time.sleep(wait / 1000)
            return func(*args, **kwargs)
        return inner
    return outer


def f():
    print('Stuff')

f = scheduler(1000)(f)

f()
