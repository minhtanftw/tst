def add_sprinkles(func):
    def wrapper():
        print("you add sprinkles")
        func()
    return wrapper

@add_sprinkles
def get_api():
    print("here is your ice cream")

get_api()