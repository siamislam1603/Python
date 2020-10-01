t=int(input())
for i in range(0,t,1):
    x=(input())
    a=x[0]
    b=x[2]
    try:
        print(int(a)//int(b))
    except ZeroDivisionError as e:
        print("Error Code: integer division or modulo by zero")
    except ValueError as e:
        print("Error Code:",e)