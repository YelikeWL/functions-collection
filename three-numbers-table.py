'''Print a table with N rows and 3 columns 
with three numbers outputs: m, m+1, and m^(m+1) 
m is the row number, 1 <= m <= N'''

# Prompt N
N = int(input("Enter a number: "))

# main
i=1
if N>=0:
    print('%-8s%-8s%-8s'%('m','m+1','m**(m+1)'))
    while N>0:
        print('%-8d%-8d%-8d'%(i, i+1, i**(i+1)))
        i+=1
        N-=1
else:
    print("Error input of improper number (e.g. negative number)")
