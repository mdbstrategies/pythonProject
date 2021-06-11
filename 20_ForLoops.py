#Lesson on the For Loops
blog_posts = ["", "The coolest Python course", "How to build new businesses", "", "What is wrong in the White House?", "Why BLM?"]
for post in blog_posts:
    if post == "":
        continue
    else:
        print(post)
print("_____________________")

myString = "This is my string"
for char in myString:
    print(char)
print("_____________________")
for x in range (0,10):
    print(x)
person = {"Name": "Jane Smith", "Age": "34", "Occupation": "Teacher"}
for key in person:
    print(key,":", person[key])
print("________________________________")
blog_posts = {"Python": ["The coolest Python course", "How to build new businesses", "What is wrong in the White House?", "Why BLM?"], "Javascript": ["How to nestle things", "Integrating CSS", "Node andi ts use"]}
for category in blog_posts:
    print("Posts about: ", category)
    for post in blog_posts[category]:
        print(post)

