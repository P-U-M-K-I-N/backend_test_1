n = int(input("Enter n of factorial : "))
fac_val = 1
amount_zero = 0

if (n == 0):
    # 0! is 1
    fac_val = 0
else:
    for i in range(n):
        fac_val = fac_val * (i+1)

str_val = str(fac_val)
for i in range(len(str_val)):
    last_step_to_start = str_val[len(str_val)-i-1]
    # print(last_step_to_start)
    if(int(last_step_to_start) == 0):
        amount_zero+=1
        # print('===> {}'.format(amount_zero))
    else:
        break
    
print('Have amount of 0 from back is {}'.format(amount_zero))
