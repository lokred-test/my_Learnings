def substring(string):
    for i in range(len(string)+1):
        for j in range(i,len(string)+1):
            print(string[i:j])
string="dhoni"
substring(string)