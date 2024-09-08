# Function to search for a key in a nested dictionary
def search_key(d, key):
    if key in d:
        return d[key]
    for k, v in d.items():
        if isinstance(v, dict):
            result = search_key(v, key)
            if result is not None:
                return result
    return None
  

# Example usage
nested_dict = {
    'person1': {
        'name': 'Alice',
        'details': {
            'age': 30,
            'city': 'New York'
        }
    },
    'person2': {
        'name': 'Bob',
        'details': {
            'age': 25,
            'city': 'Los Angeles'
        }
    }
}

value = search_key(nested_dict, 'city')
print(value)
