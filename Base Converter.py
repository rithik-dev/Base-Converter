from tkinter import *

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
def from_base_to_decimal(num, from_base):
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
def decimal_to_to_base(num, to_base):
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
                int_part = int(product)
                if int_part in CONVERT:
                    decimal_ans += CONVERT[int_part]
                else:
                    decimal_ans += str(int_part)

                if product == 1.0:
                    break

                decimal_part = product - int(product)

            ans = f"{ans}.{decimal_ans}"
        return ans
    else:
        return num


def gui():
    num = n.get().strip().upper()

    try:
        from_base = int(f_base.get())
        to_base = int(t_base.get())

        if from_base>16 or to_base>16:
            ans = "Invalid Input !"
        else:
            ans = from_base_to_decimal(num, from_base)
            ans = decimal_to_to_base(ans, to_base)
            ans = remove_zeroes(ans)

    except ValueError:
        ans = "Invalid Input !"

    answer.set(ans)


if __name__ == "__main__":
    win = Tk()
    win.geometry('400x200')
    win.resizable(False, False)
    win.title("Base Converter")

    Label(win, text='ENTER NUMBER BELOW').pack(side=TOP)

    global n
    n = Entry(win, justify=CENTER)
    n.pack(side=TOP, fill=X)

    Label(win, text='ENTER INITIAL BASE BELOW').pack(side=TOP)

    global f_base
    f_base = Entry(win, justify=CENTER)
    f_base.pack()

    Label(win, text='ENTER NEW BASE BELOW').pack(side=TOP)

    global t_base
    t_base = Entry(win, justify=CENTER)
    t_base.pack()

    Button(win, text='CONVERT', command=gui).pack(side=TOP)

    global answer
    answer = StringVar()
    answer.set('')

    Label(win, textvariable=answer, font='Helvetica 16 bold',
          wraplength=390, justify=CENTER).pack()

    win.mainloop()


# FIXME:     23798ABD.389F 16 to 13
