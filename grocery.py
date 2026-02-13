def main():
    l = items("")
    table(l)

def items(prompt):
    l = {}
    while True:
        try:
            i = input(prompt).upper()
            if i in l :
                l[i] = l[i]+1
            else:
                l[i] = 1
        except ValueError:
            pass
        except EOFError:
            return l
        
def table(d):
    l = sorted(d)
    for i in l:
        print(d[i],i)
        
main()