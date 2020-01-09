num = input("Enter Number : ").upper()
from_base = int(input("Enter 'From' Base : "))
to_base = int(input("Enter 'To' Base : "))

CONVERT = {
    'A': 10,
    'B': 11,
    'C': 12,
    'D': 13,
    'E': 14,
    'F': 15,
    10: 'A',
    11: 'B',
    12: 'C',
    13: 'D',
    14: 'E',
    15: 'F'
}


def remove_zeroes(num):   # remove leading or trailing zeroes
    is_decimal = "." in num

    for i in num:
        if i == "0":
            num = num[1:]
        else:
            break

    if is_decimal:
        num = num[::-1]

        for i in num:
            if i == "0":
                num = num[1:]
            else:
                break

        num = num[::-1]

        if num[0] == ".":  # if number is of form 0.___
            num = "0" + num

    return num


# from_base to decimal
def from_base_to_decimal(num):
    is_decimal = "." in num

    if from_base != 10:
        if is_decimal:
            n = num.split(".")
            power = len(n[0]) - 1
            num = num.replace(".", "")
        else:
            power = len(num) - 1

        ans = 0
        for c in num:
            if c in CONVERT:
                ans += CONVERT[c] * (from_base**power)
            else:
                ans += int(c) * (from_base**power)
            power -= 1

        return str(ans)
    else:
        return num


# decimal to to_base
def decimal_to_to_base(num):
    is_decimal = "." in num

    if to_base != 10:
        if is_decimal:   # decimal val
            num = num.split(".")
            integer_part = int(num[0])
            decimal_part = float("0." + num[1])
        else:   # integer val
            integer_part = int(num)
            decimal_part = None

        ans = ''

        # SOLVING INTEGER PART
        rem = -1
        while integer_part != 0:
            rem = integer_part % to_base
            if rem > 9:
                ans += CONVERT[rem]
            else:
                ans += str(rem)
            integer_part //= to_base

        ans = ans[::-1]

        if is_decimal:   # if decimal val .. solving decimal part
            decimal_ans = ''
            precision = 15  # 15 decimal points precision
            for p in range(precision):
                product = decimal_part * to_base
                decimal_ans += str(int(product))

                if product == 1.0:
                    break

                decimal_part = product - int(product)

            ans = f"{ans}.{decimal_ans}"
        return ans
    else:
        return num


try:
    ans = from_base_to_decimal(num)
    ans = decimal_to_to_base(ans)
    ans = remove_zeroes(ans)

    ans = f"'{num}' in BASE {from_base} is '{ans}' in BASE {to_base}"

    print(ans)
except ValueError:
    print("Invalid Input !")
