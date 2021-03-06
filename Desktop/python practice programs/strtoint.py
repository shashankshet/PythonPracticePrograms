#-------------------program to convert str to int using atoi-----------------
def myAtoi(string):
    res = 0
 
    # Iterate through all characters of
    #  input string and update result
    for i in range(len(string)):
        res = res * 10 + (ord(string[i]) - ord('0'))
 
    return res