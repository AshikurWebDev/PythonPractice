persons = "Dave"
coins = 3

print("\n" + persons + "has" + str(coins) + "cons left.")

message = "\n%s has %s coin left. " %(persons, coins)
print(message)

message = "\n{} has {} coins left. ".format(persons, coins)

print(message)

message = "\n{1} has {0} coins left.".format(coins, persons)
print(message)

message = "\n{person} has {coin} coins left.".format(coin=coins, person=persons)
print(message)

player = {
    'person' : 'dave', 
    'coins' : 3
}

message = "\n{person} has {coins} coins left".format(**player)
print(message)

###############################
# f-String ! This is the way

message = f"\n{persons} has {coins} coins left."
print(message)
message = f"\n{persons} has {2 * 5} coins left."
print(message)
message = f"\n{persons.lower()} has {2 * 5} coins left."
print(message)

###############################
# Passing formating options 

num = 10
print(f"\n2.5 times {num} is {2.25 * num:.2f}")
for num in range(1,11): 
    print(f"2.5 times {num} is {2.25 * num:.2f}")
for num in range(1,11): 
    print(f"{num} divided by 4.52 is {2.25 * num/4.52:.2%}")