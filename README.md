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
There are two ways to use it.
### Method-1

`characters =  ['a', 'b', 'c']`   
` _, combinations = Generator(characters, digits=2)`  
`print(combinations)`  
output = '['aa', 'ab', 'ac', 'ba', 'bb', 'bc', 'ca', 'cb', 'cc']'

### Method-2

`characters =  ['a', 'b', 'c']`  
`minIndexNum, maxIndexNum = [1, 0], [1, 2] # these numbers represents index of characters`  
`_, combinations = Generator(characters, minIndexNum=minIndexNum, maxIndexNum=maxIndexNum)`  
`print(combinations)`  
output = '['ba', 'bb', 'bc']'

### OTHER FEATURES
1. SAVE IN FILE
   **wordListFILE** parameter allows you to save file in your system.  
    `characters =  ['a', 'b', 'c']`   
    `_, combinations = Generator(characters, digits=2, wordListFILE=open('wordlist.txt', 'w+'))`  
    `combinations.seek(0)`  
    `combinations = combinations.read()`  
    `combinations = combinations.splitlines()`  
    `print(combinations)`  
    output = '['aa', 'ab', 'ac', 'ba', 'bb', 'bc', 'ca', 'cb', 'cc']'  
    
2. EXPLICIT
   **explicit** parameter will gets all combinations. Main use of explite is if its False then the generation will be fast if its true it can crash(depends on digits).  
   `characters =  ['a', 'b', 'c']`  
   `missed, combinations = Generator(characters, digits=3, explicit=False)`  
   `print(missed)`  
   output = 2  
   `characters =  ['a', 'b', 'c']`  
   `missed, combinations = Generator(characters, digits=3, explicit=True)`  
   `print(missed)`  
   output = 0  
   
3. SHUFFLING
   **shuffle** parameter will shuffles all combinations. Note that it won't shuffle if you choose file(wordListFILE parameter) as output. you can also give seed.  
   `characters =  ['a', 'b', 'c']`  
   `missed, combinations = Generator(characters, digits=2, shuffle=True)`  
   `print(combinations)`  
   output = '['ab', 'ba', 'ac', 'ca', 'cc', 'aa', 'bc', 'cb', 'bb']'  
   `characters =  ['a', 'b', 'c']`  
   `missed, combinations = Generator(characters, digits=2, shuffle=1)`  
   `print(combinations)`  
   output = '['bc', 'ca', 'cb', 'bb', 'ba', 'aa', 'cc', 'ab', 'ac']'  
