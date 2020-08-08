# FileIO operation
import os;
# import sys;
new_file = open('file.txt', 'wb+');
 
print(new_file.mode);

print(new_file.name)

new_file.write(bytes('This is a new test file for Python file IO', 'UTF-8'))

new_file.close();

test_file = open('file.txt', 'r+');

file_content = test_file.read();

print('Text in file: ', file_content);

# print(open('file.txt', 'r+'))

os.remove('file.txt');



