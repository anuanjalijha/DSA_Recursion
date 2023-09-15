def pairStar(string):
    if len(string)<=1:
        return string
    if string[0] != string[1]:
        return string[0] + pairStar(string[1:]) 
    else:
        return string[0]+'*'+pairStar(string[1:]) 
string = str(input())
print(pairStar(string))           
## Read input as specified in the question.
