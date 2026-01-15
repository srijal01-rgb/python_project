wordOne = input("enter first word:")
wordTwo = input("enter second word:")

if(len(wordOne) != len(wordTwo)):
    print(f"not anagram")
else:
    count ={}
    for ch in wordOne:
        count[ch] = count.get(ch,0) + 1

    for ch in wordTwo:
        if ch not in count or count[ch] == 0:
            print (f"not anagram")
            break
        count[ch] -=1
    else:
         print("anagram")


