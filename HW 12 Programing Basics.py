a = 0.0
li = [1.0, 'abc', 2.5, 'b', 3, 'c', 4.11, 'd', 5, 'e']

for i in range(len(li)):
    if isinstance(li[i], (int, float)):
        a = a + li[i]
        print(f"The sum of the list so far is {a}")
    if isinstance(li[i], str):
        print(f"The value of the element in the list is {li[i]}")