def is_prime(test):
    stop_p = test ** 0.5

    for i in range(2, int(stop_p)+1):
        if(test % i == 0):
            return False
    return True

while True:
    try:
        data = int(input())

        # print(prime_list)
        if (is_prime(data)):
            backward = int(str(data)[::-1])

            if (is_prime(backward) and not(backward == data)):
                print("{} is emirp.".format(data))
            else:
                print("{} is prime.".format(data))
        else:
            print("{} is not prime.".format(data))

        # print(prime_list)

    except:
        break
