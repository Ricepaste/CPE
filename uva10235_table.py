def is_prime(test):
    stop_p = test ** 0.5

    # 數字比prime list小
    if (test <= prime_list[-1]):
        if (test in prime_list):
            return True
        else:
            return False

    # 數字比prime list大，但數字開根號比prime list小
    for divisor in prime_list:
        if (divisor > stop_p):
            # 除數大於被除數開根號，還沒找到因數
            prime_list.append(test)
            return True
        elif (test % divisor == 0):
            # 找到因數了
            return False

    # # 連開根號都比prime list大
    # for divisor in range(prime_list[-1] + 1, data ** 2):


prime_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131]
while True:
    try:
        data = int(input())

        st = prime_list[-1]
        for i in range(st + 1, data):
            is_prime(i)

        # print(prime_list)
        if (is_prime(data)):
            st = prime_list[-1]
            backward = int(str(data)[::-1])
            for i in range(st + 1, backward):
                is_prime(i)

            if (is_prime(backward)):
                print("{} is emirp.".format(data))
            else:
                print("{} is prime.".format(data))
        else:
            print("{} is not prime.".format(data))

        # print(prime_list)

    except:
        break
