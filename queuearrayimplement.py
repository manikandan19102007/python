queue = [None] * 5
front = -1
rear = -1

def enqueue(x):
    global front, rear
    if rear == 4:
        print("Queue Overflow")
    else:
        if front == -1:
            front = 0
        rear += 1
        queue[rear] = x
        print("Inserted:", x)

def dequeue():
    global front, rear
    if front == -1 or front > rear:
        print("Queue Underflow")
    else:
        print("Deleted:", queue[front])
        front += 1

def display():
    if front == -1 or front > rear:
        print("Queue is Empty")
    else:
        print("Queue:", queue[front:rear+1])

enqueue(10)
enqueue(20)
enqueue(30)
display()

dequeue()
display()


print("1. Parking the car")
print("2. Getting the car from parking lot")

choice = int(input("Enter your choice: "))

if choice == 1:
    car = input("Enter car name/number to park: ")
    enqueue(car)
elif choice == 2:
    dequeue()
else:
    print("Invalid choice")
