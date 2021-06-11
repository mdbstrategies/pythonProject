#Exercise on dictionaries in Python which include predefined dictionary standards that can be used for people filling otu their data
person = {"name": "Shmuel", "gender": "male", "address": "Rua Sao Luiz 62", "phone": "51983077885"}
key = input("What information do you want to know about the person? ").lower()
result = person.get(key, "That information is not available")
print(result)
