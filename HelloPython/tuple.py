# Tuple are just like lists but they cannot be changed once created
# However, one can convert a tuple to list, change the list, and convert back to tuple
# tuples are wrapped in parenthesis like a ball()
# Define a Tuple
gadgets = ('headset', 'phone', 'laptop', 'charger');
print('Tuple : ', gadgets);
# make a list from tuples
list_from_tuple = list(gadgets);

# Make a change to the list_from-tuple;
list_from_tuple.append('cables');

# Revert to Tuple
tuple_from_list = tuple(list_from_tuple);

# display results
print('Tuple from List : ', tuple_from_list);
print('List from tuple : ', list_from_tuple);
# print(max(gadgets));
# print(len(gadgets));
