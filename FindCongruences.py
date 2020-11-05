
banner = """This little script help you to find some congruences in a given interval. This can be helpful when you're working with very large integer."""

def exp_res(c):
    export = input("Export results in txt file ? y/n ")
    if export == "y" or export == "Y":
        name = input("Path to file(including name file, empty is current folder): ")
        if name == "":
            name = "CongruenceExport.txt"
        else:
            name = name
        file = open(name, "w",encoding="utf-8")
        var = ""
        for i in c:
            var += i+"\n"
        file.write(var)
        file.close()
    else:
        pass

def congru(a,b):
    pol = input("Enter two numbers to set the interval (empty is 2-100) : ")

    if pol == "":
        print("default selected : interval between 2-100")
        c = []
        for x in range(2,100):
            if a%x == b%x:
                c.append(str(a)+" ≡ "+str(b)+" modulo "+str(x))
                print(a,"≡",b,"modulo",x)
        exp_res(c)

    else:
        pal = pol.split("-")
        print(pal)
        min,max = int(pal[0]),int(pal[1])
        c = []
        for x in range(min,max):
            if a%x == b%x:
                c.append(str(a)+" ≡ "+str(b)+" modulo "+str(x))
                print(a,"≡",b,"modulo",x)
        exp_res(c)

if __name__ == "__main__":
    print(banner)
    a,b = int(input("a : ")),int(input("b : "))
    congru(a,b)
