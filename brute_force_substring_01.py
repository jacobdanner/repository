# find substring containing all letters of string within larger - OPTIMIZE
def find_substring(tiny,large):
    final = []  # convert list to string to return
    mark = []   #   Put a marker where we find characters from tiny in large string
    final_word = ''  # RETURN string
    for x in range(len(large)):     # x 0
        for a in range(len(tiny)):  # a 0
            if (tiny[a] == large[x]):  # true
                print(tiny[a]," matches ",large[x], ' = ',tiny[a]==large[x], "at location:",x)   # Debug within loop
                mark.append(int(x))         # mark[x] = location

    for i in range(int(min(mark)),int(max(mark))+1):
        #print("Value: ",large[i])
        final.append(large[i])
        final_word += large[i]

    return final_word

################ main program ##################################
tiny_string = "aagz"
large_string = "abcdefghijklmnoprstuvwxyz"
print("Len of Large: ",len(large_string))
print("Final: ",find_substring(list(tiny_string),list(large_string)))
