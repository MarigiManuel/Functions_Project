"""
Write a function for checking the speed of drivers. This function should have one parameter: speed.
If speed is less than 70, it should print “Ok”.
Otherwise, for every 5km above the speed limit (70), it should give the driver one demerit point and print the total number of demerit points. 
For example, if the speed is 80, it should print: “Points: 2”.
If the driver gets more than 12 points, the function should print: “License suspended"
"""

def drivers_speed(speed):
    speed_limit = 70
    demerit_points = 0

    if speed < speed_limit:
        print('Ok')
    else: 
        demerit_points = (speed - speed_limit) // 5
        print(f'Points: {demerit_points}')

    if demerit_points > 12:
        print('License Suspended!')

drivers_speed(60)
drivers_speed(100)
drivers_speed(250)


"""
Write a function called fizz_buzz that takes a number.
If the number is divisible by 3, it should return “Fizz”.
If it is divisible by 5, it should return “Buzz”.
If it is divisible by both 3 and 5, it should return “FizzBuzz”.
Otherwise, it should return the same number.
"""

def fizz_buzz(input):
    if (input % 3 == 0) and (input % 5 ==0):
        return 'FizzBuzz'
    if input % 3 == 0:
        return 'Fizz'
    if input % 5 == 0:
        return 'Buzz'
    
    else:
        return input
    
print(fizz_buzz(3))
print(fizz_buzz(5))
print(fizz_buzz(15))
print(fizz_buzz(22))