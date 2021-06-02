# how can I use:  for i,j in enumerate(array):

def find_substring(tiny,large):
    final = []  # convert list to string to return
    mark = []   #   Put a marker where we find characters from tiny in large string
    final_word = ''  # RETURN string
    head=0
    middleup = (int(len(large)/2))
    middledown = middleup+1
    tail=(int(len(large)-1))#(range(len(large)-1)/2)
    print("tail: ",tail)
    print("mup : ",middleup)
    print("mdon: ",middledown)
    print("------------------------------------------")
    for x in range(int(len(large)/4)+1):
        #print("Current location of loop: ",x)     # Loop through large string of characters to half
        for a in range(int(len(tiny))):  # Loop through small string characters
            if (tiny[a] == large[x]):  # true if small character = large character
                print("P1: ",tiny[a]," matches ",large[x], ' = ',tiny[a]==large[x], "at location:",x)   # Debug within loop
                mark.append(int(x))         # mark[x] = location
            if (tiny[a] == large[middleup]):
                print("P2 : ",tiny[a]," matches ",large[middleup], ' = ',tiny[a]==large[middleup], "at location:",middleup)   # Debug within loop
                mark.append(int(middleup))         # mark[x] = location
            if (tiny[a] == large[middledown]):
                print("P3: ",tiny[a]," matches ",large[middledown], ' = ',tiny[a]==large[middledown], "at location:",middledown)   # Debug within loop
                mark.append(int(middledown))         # mark[x] = location
            if (tiny[a] == large[tail]):
                print("P4: ",tiny[a]," matches ",large[tail], ' = ',tiny[a]==large[tail], "at location:",tail)   # Debug within loop
                mark.append(int(tail))         # mark[x] = location
            #print(mark)
        print("P1: ",large[x]," | P2: ",large[middleup]," | P3: ",large[middledown]," | P4: ", large[tail])
        tail-=1
        middleup -=1
        middledown +=1
    print("All Hits of Character Locations: ",mark)

     # pointers decreases and increase location by 1 from end to .5 len times
    for i in range(int(min(mark)),int(max(mark))+1):
        #print("Value: ",large[i])
        final.append(large[i])
        final_word += large[i]
    return final_word

################ main program ##################################
tiny_string = "fs"
large_string = "abcdefghijklmnopqrstuvwxyz"
print("Len of Large (",large_string,"):",len(large_string))
print("Len of Tiny  (",tiny_string,"):",len(tiny_string))
print("------------------------------------------")
print("Final: ",find_substring(list(tiny_string),list(large_string)))
