def programa_1() :
    max_num = float(input("Introduce un número: "))
    sum_nums = max_num
    
    for i in range(9):
    
        
        num = float(input("Introduce otro número "))
        
        sum_nums =sum_nums+ (num)
        if num > max_num:
            
            max_num = num
    print("The largest number is:",max_num )
    print("The average is:", sum_nums/10)
    
programa_1()
