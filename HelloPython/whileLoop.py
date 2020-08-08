import random;

randn = random.randrange(0, 50);

# while randn != 33:
#     print(randn);
#     randn = random.randrange(0,50);


indx = 0;

while(indx <= 20):
    if indx%2 == 0:
        print(indx);
    elif indx == 9:
        break;
    else:
        indx += 1;
        continue;
    indx += 1;