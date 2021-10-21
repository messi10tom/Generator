import random

def Generator(characters, digits=None, minIndexNum=None, maxIndexNum=None, wordListFILE=None, explicit=False, shuffle=False):
    if digits:
      minIndexNum = [0 for _ in range(digits)]
      maxIndexNum = [len(characters)-1 for _ in range(digits)]
    if wordListFILE:wordListFILE.write(''.join(characters[i] for i in minIndexNum)+'\n')
    else:
      wordList = []
      wordList.append(''.join(characters[i] for i in minIndexNum))
    missing = 0
    while True:
        minIndexNum[-1] += 1
        if explicit:
          for _ in range(len(maxIndexNum)):
            for index, element in enumerate(minIndexNum):
                if element == len(characters):
                    minIndexNum[index] = 0
                    minIndexNum[index-1] += 1
        else:
          for index, element in enumerate(minIndexNum):
              if element == len(characters):
                  minIndexNum[index] = 0
                  minIndexNum[index-1] += 1
        if wordListFILE:
          try:wordListFILE.write(''.join(characters[i] for i in minIndexNum)+'\n')
          except:missing += 1
        else:
          try:wordList.append(''.join(characters[i] for i in minIndexNum))
          except:missing += 1
        if minIndexNum == maxIndexNum:
            if type(shuffle) == int:
              if wordListFILE:print("Warning! shuffle don't work in FILE mode")
              random.seed(shuffle)
              random.shuffle(wordList)
            elif shuffle == True:
              if wordListFILE:print("Warning! shuffle don't work in FILE mode")
              random.shuffle(wordList)
            if wordListFILE:return missing
            return (missing, wordList)


characters =  ['0', '1'] #['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
#wordListFILE = open('wordlist.txt', 'w+')
DIGITS = 16
missed, combinations = Generator(characters, digits=DIGITS, shuffle=45)
#missed = Generator(characters, minIndexNum, maxIndexNum, wordListFILE=wordListFILE, explicit=False)
#wordListFILE.seek(0)
#combinations = wordListFILE.read()
#combinations = combinations.splitlines()
gpw = len(combinations)
print(f'|{gpw} COMBINATIONS GENERATED|')
for count, combination in enumerate(combinations):
  if (count % 5) == 0:print()
  if count+1 > 100:
    print('Not The End')
    break
  print(combination, end=' ')
if missed != 0:
  if missed > 1:print(f'\n[{missed} COMBINATIONS MISSED]')
  elif missed == 1:print('\n[1 COMBINATION MISSED]')
else:print('\n[NO COMBINATIONS MISSED]')
print(f'\n{(gpw/(missed+gpw))*100}% of {DIGITS} digit combinations generated')
#wordListFILE.close()