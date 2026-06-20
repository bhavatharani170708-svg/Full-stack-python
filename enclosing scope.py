def outer():
    message="hello"
    def inner():
        print(message)
    inner()
outer()