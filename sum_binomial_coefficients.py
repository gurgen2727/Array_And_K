#!/usr/bin/env python
import sys

PRIME = 1000000007
PRIME_2 = PRIME - 2


# modular exponentiation: x ^ y % mod
def mod_exp(x):
    y = PRIME_2
    r = 1
    while y > 0:
        if (y & 1) == 1:
            r = (r * x) % PRIME
        x = (x * x) % PRIME
        y >>= 1

    return r


# Using Fermat's little theorem to pre-compute factorials and inverses
# Note: only works when p is prime and k < p
def fermat_compute(n):
    facts = [0] * n
    invfacts = [0] * n

    facts[0] = 1
    invfacts[0] = 1
    for i in range(1, n):
        # calculate factorial and corresponding inverse
        facts[i] = (facts[i - 1] * i) % PRIME
        # instead of calling mode_exp is used once
        invfacts[i] = mod_exp(facts[i])

    return facts, invfacts


# Calculate array of FACTS and INFACTS
FACTS, INFACTS = fermat_compute(100001)


# Compute binomial coefficient from given pre-computed factorials and inverses
def binom_pre_computed(facts, infacts, n, k):
    # n! / (k!^(p-2) * (n-k)!^(p-2)) (mod p)
    return (facts[n] * ((infacts[k] * infacts[n - k] % PRIME))) % PRIME


# Using Fermat's little theorem to compute nCk mod p
# considering cancelation of p in numerator and denominator
# Note: p must be prime
def fermat_binom_advanced(n, k):
    if k > n - k:
        k = n - k
    if k == 0 or n == k:
        return 1
    # calculate numerator
    num = 1
    for i in range(n, n - k, -1):
        num = (num * i) % PRIME
    # calculate denominator
    denom = 1
    for i in range(1, k + 1):
        denom = (denom * i) % PRIME

    # numerator * denominator^(p-2) (mod p)
    return (num * mod_exp(denom)) % PRIME


sys.stdin = open('in.txt')

T = input()
while T > 0:
    T -= 1
    N, K = [int(elem) for elem in raw_input().split()]
    if K > N:
        # find the near K equal or below N(by -2)ff
        near2index = (K - N) / 2 + (K - N) % 2
        K = K - 2 * near2index
    # check whether there is 0 in array
    there_is_zero = False
    not_zero_count = 0
    for elem in raw_input().split():
        if elem == '0' or elem == '-0':
            there_is_zero = True
        else:
            not_zero_count += 1

    count = 0
    if there_is_zero:
        mink = min(K, not_zero_count)
        # sum of cnzc(0) + cnnzc(1) + cnnzc(2) + ... + cnnzc(mink)
        for i in xrange(0, mink + 1):
            count = (count + binom_pre_computed(FACTS, INFACTS, not_zero_count, i)) % PRIME
    else:
        # sum of cn(0) + cn(2) + cn(4) + ... + cn(K)
        # sum of cn(1) + cn(3) + cn(5) + ... + cn(K)
        for i in xrange(K % 2, K + 1, 2):
            count = (count + binom_pre_computed(FACTS, INFACTS, N, i)) % PRIME
    sys.stdout.write('%s\n' % count)
