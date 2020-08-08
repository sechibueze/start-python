# Use if statements

age = 18;
weight = 55;
sex = 'male';
score = 55;

if(age > 16):
    print('Now you can drive on...');


if (weight > 30 and weight <60) :
    print('You\'re normal weight');
else: print('You are just Ok');


if score > 70 :
    grade = 'Á';
elif score <70 and score >=60 :
    grade = 'B';
elif score <60 and score >= 50:
    grade = 'C';
elif score < 50 and score >= 40:
    grade = 'D';
else: grade = 'F';

print( 'Grade : ', grade);