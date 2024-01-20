name = "Ashik"
count = 1

def another():
    color = "blue"
    global count 
    count += 1
    print(count)

    def greeting(name):
        nonlocal color
        color = "Red"
        print(color)
        print(name)
    greeting("Safayat")

another()