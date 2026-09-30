def fib(n):
    if n<=2:
        return 1
    else:
        return fib(n-1)+fib(n-2)
def print_fib(n):
    for i in range(1,n+1):
        f= fib(i)
        print(f"{f}->",end=" ")
print(print_fib(int(input("nhập N để tính fib: "))))