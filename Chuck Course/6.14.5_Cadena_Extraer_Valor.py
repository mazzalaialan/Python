str = 'X-DSPAM-Confidence:0.8475'
tultul = str.find(':')
print(tultul)
casinum = str[tultul+1:len(str)]
num = float(casinum)
print(num)
