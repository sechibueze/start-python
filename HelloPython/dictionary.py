# '''Dictionary is like an Object in javascript
# They cannot be joined with + sign like in lists and tuples
# '''

class_list = {
    'firstname': 'Samuel',
    'lastname': 'Chibueze',
    'affiliate': 'TeachFroNigeria',
    'level': 2,
    'isHappy': True
};
class_list['status'] = 'active';
del class_list['affiliate'];
class_list['size'] = len(class_list) + 1;
print(class_list);
print('keys : ', class_list.keys());
print('values : ', class_list.values());
print(class_list.get('firstname'));
