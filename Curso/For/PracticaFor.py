for i in range(5):
    print(i,end=" ")


print("\n//////////////////////////////")


fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

print("//////////////////////////////")

fruits = ["apple", "banana", "cherry"]
for i, fruit in enumerate(fruits):
    print(f"Element {i} is {fruit}")


print("//////////////////////////////")

names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
for name, age in zip(names, ages):
    print(f"{name} is {age} years old")


print("//////////////////////////////")

for i in reversed(range(5)):
    print(i,end = " ")

print("\n//////////////////////////////")

fruits = ["cherry", "banana", "apple"]
for fruit in sorted(fruits):
    print(fruit)


print("//////////////////////////////")

person = {"name": "Alice", "age": 25}
for key, value in person.items():
    print(f"{key}: {value}")