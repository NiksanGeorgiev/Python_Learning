def FromXtoDenary(num ,nSystem): #num in string
    answer = 0
    for i in range(len(num)):
        number = 0
        if num[i] in ['A', 'B', 'C', 'D', 'E', 'F']:
            number = 10 + ['A', 'B', 'C', 'D', 'E', 'F'].index(num[i])
        else:
            number = int(num[i])
        answer += number * (nSystem ** (len(num) - 1 - i))
    return answer

def DenaryToX(num ,nSystem): # num in int
    answer = ''
    while num != 0:
        rem = num % nSystem
        num //= nSystem
        if rem > 9:
            for i in (['A', 'B', 'C', 'D', 'E', 'F']):
                if rem == 10 + ['A', 'B', 'C', 'D', 'E', 'F'].index(i):
                    answer += i
        else:
            answer += str(rem)
    return answer[::-1]

print('Hello and welcome to the numeric system convertor!')
print('The numeric systems that you can use are with base 2-10 and 16')
num = input('Please enter a number that you want to convert: ' )
base = int(input('Please enter the base of the numeric system in which the number is: ' ))
while not( base in range(2,11) or base == 16):
    base = int(input('Please enter the base of the numeric system in which the number is: ' ))
baseToConvert = int(input('Please enter the base of the numeric system that you want to convert the number in: '))
while not( baseToConvert in range(2,11) or baseToConvert == 16):
    baseToConvert = int(input('Please enter the base of the numeric system that you want to convert the number in: '))

if base == 10:
    print(DenaryToX(int(num), baseToConvert))
elif baseToConvert == 10:
    print(FromXtoDenary(num, base))
else:
    print(DenaryToX(FromXtoDenary(num, base), baseToConvert))