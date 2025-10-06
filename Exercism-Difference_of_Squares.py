def square_of_sum(number):
    return sum([digit for digit in range(number+1)])**2


def sum_of_squares(number):
    return sum([digit**2 for digit in range(number+1)])


def difference_of_squares(number):
    return square_of_sum(number) - sum_of_squares(number)