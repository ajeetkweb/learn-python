# Function to flatten a nested dictionary
def flatten_dict(d, sep='_'):
    items = []
    for k, v in d.items():
        new_key = f"{k}{sep}"
        if isinstance(v, dict):
            print(v.items())
            for key, value in v.items():
                new_key2 = f"{k}{key}{sep}"
                items.append((new_key2, value))
        else:
            items.append((new_key, v))
            
    return dict(items)

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

flat_dict = flatten_dict(nested_dict)
print(flat_dict)
