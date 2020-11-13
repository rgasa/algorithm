# --------------------------------------------------------------------
# name          : isPrime.py
# version       : 1.00
# description   : 素数判定のサンプルスクリプト。
# author        : rogasawara
# date          : 2020-09-12
# update        :
# --------------------------------------------------------------------

# --------------------------------------------------------------------
# name          : is_prime_v1
# description   : 素数判定のサンプルスクリプト。
# param         : num
# return        : True/False
# author        : rogasawara
# date          : 2020-09-12
# update        :
# --------------------------------------------------------------------
def is_prime_v1(num: int ) -> bool:
    if num <= 1:
        return False
    for i in range (2,num):
        if num % i == 0:
            return False
    return True
# --------------------------------------------------------------------
# name          : is_prime_v2
# description   : 素数判定のサンプルスクリプト。
# param         : num
# return        : True/False
# author        : rogasawara
# date          : 2020-10-28
# update        :
# --------------------------------------------------------------------
def is_prime_v2(num: int ) -> bool:
    """
    36 = 1 * 36
    36 = 2 * 18
    36 = 3 * 12
    36 = 4 * 9
    36 = 6 * 6      <= √n
    36 = 9 * 4
    36 = 12 * 3
    36 = 18 * 2
    36 = 36 * 1
    """
    if num <= 1:
        return False

    i = 2
    while i * i <= num:
        if num % i == 0:
            return False
        i += 1
    return True
# --------------------------------------------------------------------
# name          : is_prime_v3
# description   : 素数判定のサンプルスクリプト。
# param         : num
# return        : True/False
# author        : rogasawara
# date          : 2020-10-28
# update        :
# --------------------------------------------------------------------
def is_prime_v3(num: int ) -> bool:
    if num <= 1:
        return False

    if num == 2:
        return True

    if num % 2 == 0:
        return False

    i = 3
    while i * i <= num:
        if num % i == 0:
            return False
        i += 2
    return True

# --------------------------------------------------------------------
# name          : is_prime_v4
# description   : 素数判定のサンプルスクリプト。
# param         : num
# return        : True/False
# author        : rogasawara
# date          : 2020-10-28
# update        :
# --------------------------------------------------------------------
def is_prime_v4(num: int ) -> bool:
    """
    2 or 3 6k +- √n
    """
    if num <= 1:
        return False

    if num <= 3:
        return True

    if num % 2 == 0 or num % 3 == 0:
        return False

    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True



if __name__ == '__main__':
    import time 
    import random

    numbers = [random.randint(0, 1000) for _ in range(1000000)]
    start = time.time()
    for num in numbers:
        is_prime_v1(num)
    print('v1',time.time() - start)

    start = time.time()
    for num in numbers:
        is_prime_v2(num)
    print('v2',time.time() - start)

    start = time.time()
    for num in numbers:
        is_prime_v3(num)
    print('v3',time.time() - start)

    start = time.time()
    for num in numbers:
        is_prime_v4(num)
    print('v4',time.time() - start)


