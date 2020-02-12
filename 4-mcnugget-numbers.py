    
def is_mcnugget(n):
    if n <= 0:
        return False
    elif n == 6: 
        return True
    elif n == 9:
        return True
    elif n == 20: 
        return True
    else: 
        return (is_mcnugget(n-20) or is_mcnugget(n-9) or is_mcnugget(n-6))

for i in range(45):
    if not is_mcnugget(i):
        print(i)


# for i in range(150):
#     if not is_mcnugget(i):
#         print(i)

