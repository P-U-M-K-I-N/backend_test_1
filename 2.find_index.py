indexArray = [1,2,1,3,5,6,4]
max_value,max_position = 0,0

for (index,number) in enumerate(indexArray):
    
    if(number > max_value):
        max_value = number
        max_position = index
        
print('Maximum value is index = {}'.format(max_position))