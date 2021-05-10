def p(k) :
    return f"Hi! {k}"

def add(x, y) :
    return x+y+5


''' WITHOUT THIS ON IMPORTING ALL THING WILL BE EXECUTED WHICH IS NOT NEEDED! '''

if __name__ == "__main__":
    print(p("QWERTY"))
    print(add(4, 6))


print(__name__)    # [main] here but in imported file it will be the [i46nameMain]