

def fat(n):
        if n==0 or n==1:
                return 1
        else:
                return n*fat(n-1)

err = 100.0
n = 0
e_ant = 0

while(err>=0.0001):
        e = e_ant + 1/fat(n)
        print(e, e_ant, err)

        err = (e - e_ant)/e
        e_ant = e
        n = n+1

e = e_ant + 1/fat(n)
print(e, e_ant, err)





