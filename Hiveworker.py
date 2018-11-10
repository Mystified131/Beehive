def blobintowords(textchunk):

    wordlist = []
    wordlst = []
    lowchunk = textchunk.lower()
    wordlist = lowchunk.split()

    for elem in wordlist:
        elem2 = ""
        for i in elem:
            if i.isalpha():
                elem2 += i
        wordlst.append(elem2)

    return wordlst

## THE GHOST OF THE SHADOW ##





