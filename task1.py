def sortingAcronyms(lst):
    # sorts normally by alphabetical order
    lst.sort(reverse=True)
    # sorts by descending length
    lst.sort(key=len, reverse=True)
    return lst

if __name__  == '__main__':
    lst_len = int(input())
    inpLst = []
    for i in range(lst_len):
        inp = str(input())
        words = inp.split()
        acronym = ""
        for word in words:
            if word[0].isupper():
                alpha = word[0]
                acronym = acronym + alpha
        inpLst.append(acronym)
    sortingAcronyms(inpLst)            
    for word in inpLst:
        print(word)

