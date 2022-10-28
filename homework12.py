from datetime import datetime
time = datetime.now()

def time_of_function(function):
    def wrapped():
        start_time = datetime.now()
        function()
        end_time = datetime.now()
        print(end_time - start_time)
    return wrapped

@time_of_function
def func():
    for i in range(10000):
        print(i)


@time_of_function
def foo():
    print(100*4)
    print(100 + 4)
    print(100 / 4)
    print(100 - 4)
    print(100*4*100*4*4*4)

func()
foo()






