import matplotlib.pyplot as plt
x = [1,2,3,4]
y = [1500,800,400,1200]
plt.plot(x,y)
plt.show()

legend = ["January", "February", "March", "April"]
plt.xticks(x,legend)

plt.plot(x,y)
plt.show()
plt.bar(x,y)

plt.ylabel("Sales in US$")
plt.xlabel("Quantity Sold")
plt.title("Monthly Sales")

plt.show()




