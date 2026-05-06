import time

def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

def main():
    print("Addition:", add(2, 3))
    print("Multiplication:", multiply(2, 3))

    while True:
        time.sleep(10)

if __name__ == "__main__":
    main()
