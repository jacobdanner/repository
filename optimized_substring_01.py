# find substring containing all letters of string within larger - OPTIMIZE
def find_substring(tiny,large):
    final = []  # convert list to string to return
    mark = []   #   Put a marker where we find characters from tiny in large string
    final_word = ''  # RETURN string
    head=0
    tail=(int(len(large)-1))#(range(len(large)-1)/2)
    for x in range(int(len(large)/2)):     # Loop through large string of characters to half
        for a in range(len(tiny)):  # Loop through small string characters
            if (tiny[a] == large[x]):  # true if small character = large character
                print("HEAD: ",tiny[a]," matches ",large[x], ' = ',tiny[a]==large[x], "at location:",x)   # Debug within loop
                mark.append(int(x))         # mark[x] = location
            if (tiny[a] == large[tail]):
                print("TAIL: ",tiny[a]," matches ",large[tail], ' = ',tiny[a]==large[tail], "at location:",tail)   # Debug within loop
                mark.append(int(tail))         # mark[x] = location
            #print(mark)
        tail-=1  # tail decreases location by 1 from end to .5 len times
    for i in range(int(min(mark)),int(max(mark))+1):
        #print("Value: ",large[i])
        final.append(large[i])
        final_word += large[i]

    return final_word

################ main program ##################################
tiny_string = "abnglw"
large_string = "abcdefghijklmnoprstuvwxyz"
print("Len of Large: ",len(large_string))
print("Final: ",find_substring(list(tiny_string),list(large_string)))
