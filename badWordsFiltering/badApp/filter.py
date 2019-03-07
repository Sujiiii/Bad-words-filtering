import os

def process_string(string,):
    result = ""
    str_list = string.split()
    strn_list = [i.lower() for i in str_list]

    with open(os.path.dirname(__file__)+'/badwords.txt','r') as file:
        for word in file:
           word = word.split(', ')

    for i in strn_list:
        if i in word:
            result += '*'*len(i)+" "
        else:
             result+=i+" "
    return result

# def getInput(string):
#     return process_string(string)
