# --------------------------------------------------------------------
# name          : prime_factorization.py
# version       : 1.00
# description   : 素因数分解を行うサンプルコード。
# author        : rogasawara
# date          : 2020-10-30
# update        :
# --------------------------------------------------------------------
import math as m

# --------------------------------------------------------------------
# name          : prime_factorization_v1
# description   : 素因数分解を行うサンプルコード。
# param         : num
# return        : True/False
# author        : rogasawara
# date          : 2020-10-30
# update        :
# --------------------------------------------------------------------
def prime_factorization_v1(num: int):
    arr = {}
    n = 2
    # 平方根の取得
    sq_root = m.sqrt(num)
    while n < sq_root:
        cnt = 0
        while num % n == 0:
            cnt += 1
            # 整数除算
            num //= n
        if cnt != 0:
            arr[n] = cnt
        n += 1
    if num > 1:
        arr[num] = 1
    return arr

# --------------------------------------------------------------------
# name          : prime_factorization_v2
# description   : 素因数分解を行うサンプルコード。
# param         : num
# return        : True/False
# author        : rogasawara
# date          : 2020-10-30
# update        :
# --------------------------------------------------------------------
def prime_factorization_v2(num: int):
    arr = {}
    n = 2
    # 平方根の取得
    sq_root = m.sqrt(num)
    while n < sq_root:
        cnt = 0
        while num % n == 0:
            cnt += 1
            num //= n
        
        if cnt != 0:
            arr[n] = cnt
        
        if n == 2:
            n += 1
        else:
            n += 2
        
        if num == 1:
            break
    if num > 1:
        arr[num] = 1
    return arr

# --------------------------------------------------------------------
# name          : prime_factorization_v3
# description   : 素因数分解を行うサンプルコード。
# param         : num
# return        : True/False
# author        : rogasawara
# date          : 2020-10-30
# update        :
# --------------------------------------------------------------------
'''
def prime_factorization_v3(num: int):
    arr = {}
    n = 2
    # 平方根の取得
    sq_root = m.sqrt(num)
    while n < sq_root:
        cnt = 0
        while num % n == 0:
            cnt += 1
            num //= n
        
        if cnt != 0:
            arr[n] = cnt

        if n > 3:
            while num % (n + 2) == 0:
                cnt += 1
                num //= (n + 2)
            
            if cnt != 0:
                arr[n + 2] = cnt
        
        # nのインクリメント
        if n == 2:
            n += 1
        if n == 3:
            n += 2
        else:
            n += 6
        
        # numが1になった場合、break
        if num == 1:
            break

    if num > 1:
        arr[num] = 1
    return arr
'''


if __name__ == '__main__':
    import time 
    import random

    tgt_num = 4338489384

    start = time.time()
    print(prime_factorization_v1(tgt_num))
    print('v1::',time.time() - start)

    start = time.time()
    print(prime_factorization_v2(tgt_num))
    print('v2::', time.time() - start)
'''
    start = time.time()
    print(prime_factorization_v3(tgt_num))
    print('v3::', time.time() - start)
'''