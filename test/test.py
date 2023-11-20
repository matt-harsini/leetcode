def main():
    def middlewareOne(function):
        print("Begin middlewareOne")
        def handleOne():
            print("Executing middlewareOne")
            function()
            print("Executing middlewareOne again")
        return handleOne

    def middlewareTwo(function):
        print("Begin middlewareTwo")
        def handleTwo():
            print("Executing middlewareTwo")
            function()
            print("Executing middlewareTwo again")
        return handleTwo

    def final():
        print("Executing final")

    x = middlewareOne(middlewareTwo(final))
    x()

main()


def handlerOne(x):
    print("HandlerOne", x)
    return x * 2

def handlerTwo(y):
    print("HandlerTwo", y)
    return y + 3

# based on this information we can conclude expressions are invoked inner to outer, at least in python
print(handlerOne(handlerTwo(1)))  