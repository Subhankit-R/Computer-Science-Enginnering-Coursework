import random
 #Random float(0--1)
print(random.random())

#Random Integer
print(random.randint(1,10))

#Random Selection functions
#Random Choice from List

colors = ['red','blue','green']
print(random.choice(colors))

#Random sample(no repitition)
number = [1,2,3,4,5]
print(random.sample(number,3))

#Shuffle List
numbers = [1,2,3,4]
random.shuffle(numbers)

#Setting random Seed (for reproductibility)
random.seed(10)
print(random.random())