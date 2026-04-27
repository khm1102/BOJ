croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
String = input()

for i in croatia : String = String.replace(i, '*')  
    
print(len(String))