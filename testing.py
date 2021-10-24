from generator import Generator

characters =  ['0', '1'] #characters that used in the each combinations
DIGITS = 16 # length of each combinations

missed, combinations = Generator(characters, digits=DIGITS)
gc = len(combinations)
print(f'|{gc} COMBINATIONS GENERATED|')
for count, combination in enumerate(combinations):
  if (count % 5) == 0:print()
  if count+1 > 100:
    print('Preview ended')
    break
  print(combination, end=' ')
if missed != 0:
  if missed > 1:print(f'\n[{missed} COMBINATIONS MISSED]')
  elif missed == 1:print('\n[1 COMBINATION MISSED]')
else:print('\n[NO COMBINATIONS MISSED]')
print(f'\n{(gc/(missed+gc))*100}% of {DIGITS} digit combinations generated')
