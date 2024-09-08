state_capitals = {
    "Bihar": "Patna",
    "Rajasthan": "Jaipur",
    "Uttar Pradesh": "Luchnow",
    "Punjab": "Chandigadh"
}

print(state_capitals)

# Add Items to a Dictionary
state_capitals['Maharastra'] = 'Mumbay'
print(state_capitals)


# Remove Dictionary Items 
# using del
del state_capitals['Maharastra']
print(state_capitals)



# clear() - clear the dictionary
country_capitals = {
  "Germany": "Berlin", 
  "Canada": "Ottawa", 
}
# clear the dictionary
country_capitals.clear()
print(country_capitals)  



# Iterate Through a Dictionary

for state in state_capitals:
    print('state: ', state)


# print dictionary values one by one
for state in state_capitals:
    print(f' {state} capital is {state_capitals[state]}')


# values()
print(state_capitals.values())
for capital in state_capitals.values():
    print("capital:", capital)

# keys()
print(state_capitals.keys())
for state in state_capitals.keys():
    print("state:", state)


# dict.items()
print(state_capitals.items())

for state, capital in state_capitals.items():
    print(state, ': ', capital)


# dict.update()
state_capitals.update({"Jharkhand": "Ranchi"})
print(state_capitals)







