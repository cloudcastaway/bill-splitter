# The following line creates a dictionary from the input. Do not modify it, please
test_dict = json.loads(input())

# Work with the 'test_dict'
min_key = None
max_key = None

for key, value in test_dict.items():
    if min_key is None and max_key is None:
        min_key = key
        max_key = key
    elif value < test_dict[min_key]:
        min_key = key
    elif value > test_dict[max_key]:
        max_key = key

print("min:", min_key)
print("max:", max_key)