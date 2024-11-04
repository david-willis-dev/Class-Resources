print("Welcome to Joe's Burger Shop")
print("----Menu----")
print("Burger: $10")
print("Cheeseburger: $12")

patties = 10
buns = 20
chzSlices = 15
revenue = 0
while (patties > 0 and buns > 1 and chzSlices > 0):
	numBurgers = (int)(input("How many burgers would you like? "))
	numCheeseburgers = (int)(input("How many of those would you like with cheese? "))
	patties = patties - numBurgers
	chzSlices = chzSlices - numCheeseburgers
	buns = buns - numBurgers * 2
	revenue = revenue + numCheeseburgers * 12
	revenue = revenue + (numBurgers - numCheeseburgers) * 10

print("----End of Day Stock----")
print("patties left: ", patties)
print("buns left: ", buns)
print("chzSlices left: ", chzSlices)
print("Total revenue for the day: ", revenue)
