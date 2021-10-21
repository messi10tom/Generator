# Generator
Generate combinations according to the specs

## Parameters

**characters** - It is a list which contains characters that are included in combinations.  
**digits** - Number of digits of output.  
**minIndexNum** - Minimum of output.  
**maxIndexNum** - Maximum of output.  
**wordListFILE** - Output will be stored in this file.  
**explicit** - If its true the Generator will generate complete amount of combination.  
**shuffle** - It will shuffle the entire combination list randomly if its true. Integers is also accepted as seeds.  

## HOW TO USE
There are two ways to use it
### Method-1

`characters =  ['a', 'b', 'c']   
  _, combinations = Generator(characters, digits=2)`  
output = '['aa', 'ab', 'ac', 'ba', 'bb', 'bc', 'ca', 'cb', 'cc']'

### Method-2

`characters =  ['a', 'b', 'c']  
minIndexNum, maxIndexNum = [1, 0], [1, 2] # these numbers represents index of characters  
_, combinations = Generator(characters, minIndexNum=minIndexNum, maxIndexNum=maxIndexNum)`  
output = '['ba', 'bb', 'bc']'

### OTHER FEATURES
