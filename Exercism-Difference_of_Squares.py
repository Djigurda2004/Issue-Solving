def square_of_sum(number):
    sum = 0
    for digit in range(number+1):
        sum += digit
    return sum**2


def sum_of_squares(number):
    sum = 0
    for digit in range(number+1):
        sum += (digit**2)
    return sum


def difference_of_squares(number):
    return  square_of_sum(number) - sum_of_squares(number)