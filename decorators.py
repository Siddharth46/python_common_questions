def limit_check(func):
    def check(a,b):
        if a>10 or b>10:
            print("number too big")
            return
        return func(a,b)
    return check

@limit_check
def addition(a,b):
    return a+b

print(addition(4,6))
