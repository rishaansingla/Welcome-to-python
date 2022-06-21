# Input Year:
year = int(input('Enter Year: '))

if year % 100 == 0:
    if year % 400 ==0:
        print('It Is A Leap Year')
    else:
        print('It Is Not A Leap')
else:
    if year % 4 == 0:
        print('It Is A Leap Year')
    else:
        print('It Is Not A Leap')
