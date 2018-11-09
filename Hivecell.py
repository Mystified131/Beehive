textchunk = "Surrounded to me occasional pianoforte alteration unaffected impossible ye. For saw half than cold. Pretty merits waited six talked pulled you. Conduct replied off led whether any shortly why arrived adapted. Numerous ladyship so raillery humoured goodness received an. So narrow formal length my highly longer afford oh. Tall neat he make or at dull ye."

wordlist = []
wordlst = []
phraselist = []
lowchunk = textchunk.lower()
wordlist = lowchunk.split()

for elem in wordlist:
    elem2 = ""
    for i in elem:
        if i.isalpha():
            elem2 += i
    wordlst.append(elem2)

if len(wordlst) < 6:
    for elem in wordlst:
        phraselist.append(elem)

if len(wordlst) >= 6:
    for num1 in range(len(wordlst)):
        if num1 >= 6:
            texttemp = ""
            texttemp += (wordlst[num1 - 6] + " " + wordlst[num1 - 5] + " " + wordlst[num1 - 4] + " " + wordlst[num1 - 3] + " " + wordlst[num1 - 2] + " " + wordlst[num1 - 1])
            phraselist.append(texttemp)

print (phraselist)

## THE GHOST OF THE SHADOW ##





