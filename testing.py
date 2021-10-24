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
