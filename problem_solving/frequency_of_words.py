from collections import Counter
def freq_words(sentance):
    x=sentance.split()  #the split function converts a sentence(seperated by " ") into list format with each word as an element
    print(x)
    count=Counter(x)
    # count={}
    # for i in x:
    #     if i in count:
    #         count[i] +=1
    #     else:
    #         count[i]=1
    print(count)
    return count

sentance="Lokesh loves eating apple and mango his sister also loves eating apple and mango"
output=freq_words(sentance)

#delete duplicates
x=list(set(output))
print(x)
