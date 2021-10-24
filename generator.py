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
            if wordListFILE:return (missing, wordListFILE)
            return (missing, wordList)
