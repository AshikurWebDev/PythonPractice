users = ['Ashik', 'Safayat', 'Moshiur']
data = ['Ashik', 42, True]
emptylist = []
print ("Ashik" in users)
print (users[0])
print (users[-2])
print (users.index("Ashik"))
print(users[0:2])
print(users[1:])
print(len(data))
users.append('Hijbulla')
users.extend(['hello', 'Elsa'])
users += ['Rahat']

# users.extend(data)
# print(users[0:])

users.insert(0, 'Bob')
print(users)

users.remove('Bob')
print(users)
