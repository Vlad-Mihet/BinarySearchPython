import random
array = [random.randint(-100, 100) for i in range(15)]
array = sorted(array)
print(array)
print(array[7])
left = 0
right = 14
length = len(array)
wantedNumber = int(input('See if your number is in the array: '))
x = array.index(wantedNumber)
left = 0
right = length - 1
position = None
while left <= right:
    middleIndex = (left + right) // 2
    if wantedNumber >= array[middleIndex]:
        position = middleIndex
        left = middleIndex + 1
    else:
        right = middleIndex - 1
if wantedNumber == array[position]:
    print('Your chosen number has been found on position ' + str(x) + ' in the array')
else:
    print('The number you have chosen hasn\'t been found in the array!')