

def permutations(string):
    if len(string)==0:
        output = [""]
        return output
    smallOutput = permutations(string[1:]) 
    output = []
    for curr_string in smallOutput:
        for i in range(len(curr_string)+1):
            new_string = curr_string[:i]+string[0]+curr_string[i:]
            output.append(new_string)
    return output        
    #Implement Your Code Here
    


string = input()
ans = permutations(string)
for s in ans:
    print(s)






