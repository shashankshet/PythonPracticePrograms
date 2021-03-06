##To find the max cosecutive ones

def maxConsequtiveOnes(String):
    if String == "" :
        return 0
    max_till_now = 0
    ones = []
    for i in String:
        if i == "1":
            max_till_now += 1
        if i == "0":
            max_till_now = 0
        ones.append(max_till_now)
    return max(ones)
print(maxConsequtiveOnes('101101111'))