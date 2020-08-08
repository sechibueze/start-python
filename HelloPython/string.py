text = 'Beware, this is a very long string';

print('string length : ', len(text));
print(text[-6:]);
# C:\Users\chibuezesamuel\Documents\Apps\LearnPython\Learn
# strip white spaces
print(text.strip())
print(text.isalnum())
print(text.isalpha())
print(text.find('very'))

print(text.replace('very', 'too'))

print('If you get a %c, then you need to put in more %s to boost your CGPA by %.4f' %('D','effort', 1.23));

print(text.split(' '))
print(text)