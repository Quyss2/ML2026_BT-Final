def get_hoc_bong(GPA,DRL):
    if GPA >= 9 and DRL >= 90:
        return 10
    elif GPA >=8 and DRL >= 80:
        return 5
    return 0
GPA=float(input("nhập GPA:"))
DRL = float(input("nhập DRL"))
result = get_hoc_bong(GPA,DRL)
print(f"GPA= {GPA}, DRL = {DRL}, result = {result}")

def fib(n,n+1):
    if n == 0:
    elif