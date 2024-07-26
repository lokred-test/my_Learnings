def common_letters(str1,str2):
    # str1_cpy=""
    # for i in str1:
    #     if i in str1_cpy:
    #         continue
    #     else:
    #         str1_cpy +=i

    # str2_cpy=""
    # for i in str2:
    #     if i in str2_cpy:
    #         continue
    #     else:
    #         str2_cpy +=i

    #or
    str1_cpy=set(str1)
    str2_cpy=set(str2)
    common_letts=""
    for i in str1_cpy:
        for j in str2_cpy:
            if i==j:
                common_letts +=i+","
    print(common_letts)

str1="abcdabcd"
str2="bdxybdxy"
common_letters(str1,str2)


        
