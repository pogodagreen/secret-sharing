from random import randrange


def isPrime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

p = randrange(1000, 10000)
while not isPrime(p):
        p = randrange(1000, 10000)

def sigma(a, x, t):
    result = 0
    for j in range(1, t - 1):
        result += a[j] * (x ** j)
    return result


def getSecret(t, tab):
    sigma = 0
    for i in range(1, t):
        multiplication = 1
        for j in range(1, t):
            if i != j:
                multiplication *= (-1*j) / (i - j)
        sigma += tab[i] * multiplication
    return sigma%p


if __name__ == '__main__':

    s = randrange(0, p - 1)
    n = 10
    a = [s]
    t = 6
    for i in range(1, t):
        a.append(randrange(0, 1000))
    print(a)
    sTab = [s]
    for i in range(1, n):
        sTab.append((s + sigma(a, i, t)) % p)
    print(sTab)
    print(getSecret(t, sTab))
