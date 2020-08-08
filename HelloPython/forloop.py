

fruits = ['Apple', 'Banana', 'Carrot', 'Dodo', 'Elsever'];
# for x in range(0,10,2):
#     print('x = ',x);

# for x in fruits:
#     print(x);


data = [[1,2,3], [10,20,30],[100,200,300]];
# Loop inside loop
for x in range(0, len(data)):
    for y in range(0, len(data[x])):
        for z in range(0, len(data[x])):
            print(x,y,z);