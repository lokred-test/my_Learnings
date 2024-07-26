def reverse(str_r):
    str_r=str_r[::-1]
    return str_r



def reverse_words(str_r):
    n=len(str_r)
    if(n==1):
        return str_r
    list=str_r.split()
    rev_all=""
    for i in range(-len(list),0):
        rev=reverse(list[i])
        rev_all=rev_all+rev+" "
    print(rev_all)
    d=reverse(rev_all)
    print(d)
    return d.strip()


A="india is my country"
print(reverse_words(A))