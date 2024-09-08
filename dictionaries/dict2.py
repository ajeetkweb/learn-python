
# Example nested dictionary
people = {
    'person1': {
        'name': 'Alice',
        'age': 30,
        'city': 'New York'
    },
    'person2': {
        'name': 'Bob',
        'age': 25,
        'city': 'Los Angeles'
    }
}

# Accessing a nested value
alice_age = people['person1']['age']
bob_city = people['person2']['city']

print(f"Alice's age: {alice_age}")
print(f"Bob's city: {bob_city}")


# Iterating over a nested dictionary
for person, details in people.items():
    print(f"{person}:")
    for key, value in details.items():
        print(f"  {key}: {value}")


