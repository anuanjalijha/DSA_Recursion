def subsequences(string):
    if len(string)==0:
        output=[]
        output.append("")
        return output
    smallerString=string[1:]
    smallerOutput=subsequences(smallerString)
    
    output=[]
    for sub in smallerOutput:
        output.append(sub)
        
    for sub in smallerOutput:
        subs_with_zeroth_char=string[0]+sub
        output.append(subs_with_zeroth_char)
        
    return output
    


string = input()
ans = subsequences(string)
for ele in ans:
    print(ele)
