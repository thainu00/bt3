def get_sum(*num):
    tmp=0
    #duyet cac tham so
    for i in num:
        tmp+=i
        return tmp
result=get_sum(12,3,4,5)
print(result)
