def fibonacci(n):
    fib_series= [0,1]
    for i in range(2,n):
        fib_series.append(fib_series[i-1] + fib_series[i-2])
    return fib_series
n = 10
fib_series = fibonacci(n)
print(fib_series)

#output = [0,1,1,2,3,5,8,13,21,34]