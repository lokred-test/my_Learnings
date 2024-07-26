
def anagram(A):
    if(A==None):
        return
    else:
        dict={}
        for i in range(len(A)):
            word="".join(sorted(A[i])) #"".join is mandatory for sorting a word(to sort each char with no space)
            if(word in dict):
                dict[word].append(i)
            else:
                dict[word]=[i]
        return dict
b=["cat","dog","god","tca","act"]
print(anagram(b))

x="madam"
rev=x[::-1]
if x==rev:
    print("Anagram")
else:
    print("not")