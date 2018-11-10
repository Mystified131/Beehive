def blobintophrases(textchunk):

    wordlist = []
    wordlst = []
    phraselist = []
    textchunk = textchunk.lower()
    wordlist = textchunk.split()
    texttemp = ""

    for elem in wordlist:
        elem2 = ""
        for i in elem:
            if i.isalpha():
                elem2 += i
        wordlst.append(elem2)

    if len(wordlst) < 6:
        for elem in range(len(wordlst)):
            texttemp += wordlst[elem] + " "
        texttemp = texttemp.rstrip()
        phraselist.append(texttemp)

    if len(wordlst) >= 6:
        for num1 in range(len(wordlst)):
            texttemp = ""
            texttemp += (wordlst[num1 - 6] + " " + wordlst[num1 - 5] + " " + wordlst[num1 - 4] + " " + wordlst[num1 - 3] + " " + wordlst[num1 - 2] + " " + wordlst[num1 - 1])
            phraselist.append(texttemp)

    return phraselist

## THE GHOST OF THE SHADOW ##





