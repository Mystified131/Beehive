textchunk = "Surrounded to me occasional pianoforte alteration unaffected impossible ye. For saw half than cold. Pretty merits waited six talked pulled you. Conduct replied off led whether any shortly why arrived adapted. Numerous ladyship so raillery humoured goodness received an. So narrow formal length my highly longer afford oh. Tall neat he make or at dull ye."

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

print (wordlst)

## THE GHOST OF THE SHADOW ##





