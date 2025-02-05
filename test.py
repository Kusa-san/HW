import random
group = ['kusa','omer','ayman','sahar','malaz','walaa','fatima','minna','mona']
group1 = []
group2 = []
group3 = []

while len(group) > 0:

    group1.append(group.pop(random.randint(0,len(group)-1)))
    group2.append(group.pop(random.randint(0,len(group)-1)))
    group3.append(group.pop(random.randint(0,len(group)-1)))

print(f"group 1 is : {group1}")
print(f"group 2 is : {group2}")
print(f"group 3 is : {group3}")