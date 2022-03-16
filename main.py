def memoize(f):
    dict_f = {}

    def memo_f(n):
        if n not in dict_f.keys():
            dict_f[n] = f(n)
        return dict_f[n]

    return memo_f

@memoize
def fib(n):
    if n <= 0:
        return 1
    else:
        return fib(n-1) + fib(n-2)

print(fib(100))