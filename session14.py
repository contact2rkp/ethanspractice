import math
n = int(input('Enter the number:'))
try:
    print(100/n)
except ZeroDivisionError as z:
    print(z)

except TypeError as T:
    print(T)

except Exception as E:
    print('Exceptin Received', sys.exc_info())

else:
    print(f'n')

finally:
    print('I am in finally block')

print('Program completed')