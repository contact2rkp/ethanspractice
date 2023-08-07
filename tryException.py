count = 1

while count <= 5:
    try:
        number = int(input('Enter a number:'))
        var = 100 / number
        break
    except ZeroDivisionError as z:
        print('Please provide the number greater than 0')
        count += 1