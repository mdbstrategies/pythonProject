#This program allows users to enter their details and gain instant access to the new list
people = ["Reuven", "David", "Yishai"]
user = input("Type your name: ")

people.append(user)
print("Here is the new list, including your name! ", people)