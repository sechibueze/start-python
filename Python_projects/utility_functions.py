def reverse_string(text="Hello"):
    return text[::-1]


def capitalize_string(text="i love python"):
    return text.capitalize()


def swap_numbers(first_number=3, second_number = 5):
    # 3 + 5 = 8
    # 3 = 8 - 5
    # 5 = 8 - 3
    set_first_number = first_number + second_number
    set_second_number = set_first_number - second_number
    set_first_number -= set_second_number
    return first_number, second_number, " => ", set_first_number,set_second_number


def reverse_number_digits(user_input=123):
    init_number = user_input
    reverse_digits = 0
    while init_number > 0:
        digit = init_number % 10
        reverse_digits = reverse_digits * 10 + digit
        init_number //= 10
    return reverse_digits


def sum_number_digits(number=123):
    number_list = []
    temp_number = number
    while temp_number > 0:
        digit = temp_number % 10
        number_list.append(digit)
        temp_number //= 10
    return sum(number_list)


def factors_of_number(number=20):
    temp_number = number
    factors = []
    for count in range(1, temp_number + 1):
        if temp_number % count == 0:
            factors.append(count)
    return factors


def get_smallest_divisor(number=20):
    temp_number = number
    divisors = []
    for count in range(2, temp_number + 1):
        if temp_number % count == 0:
            divisors.append(count)
    return min(divisors)


# TODO
def is_prime(number=9):
    temp_number = number
    # the highest factor of an integer is at least half the number
    # 1 is excludes => it is a factor of all numbers
    # from 2 to half of the number
    possible_factors = range(2, temp_number // 2 + 1)
    kk = 0 # increase me if there is a factor => if number != prime
    for ii in possible_factors:
        if number % ii == 0: # kk is changed if there is a number that can divide
            kk += 1

    if kk > 0:  # a factor was found, kk has changed because number is not prime
        return False
    else:
        return True


def get_prime_factors(number=16):
    temp_number = number
    prime_factors = []
    for count in range(2, temp_number+1):
        if temp_number % count == 0:  #count is a factor
            kk = 0
            for ii in range(2, count//2+1):
                if count % ii == 0:
                    kk += 1

            if kk == 0:  # factor has no other factor
                prime_factors.append(count)
    return prime_factors

print("Reverse a string : ", reverse_string())
print("Capitalize a string : ", capitalize_string())
print("Swap numbers : ", swap_numbers(100,5))
print("reverse digits : ", reverse_number_digits(123456))
print("Sum of digits in number : ", sum_number_digits(999))
print("Factors of number : ", factors_of_number(111))
print("Get smallest divisor : ", get_smallest_divisor(45))
print(" is prime number : ", is_prime(4))
print("Get prime factors : ", get_prime_factors(122))

