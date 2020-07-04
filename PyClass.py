class MyClass:
    x = 5

    def __init__(self):
        super().__init__()
        print("INIT")

c = MyClass()
print(c.x)