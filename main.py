with open("books/Frankenstein.txt") as f:
    file_contents = f.read()
    
def Tell():
    print(file_contents)
   

def WordCount():
    words = file_contents.split()
    wcount = 0
    for word in words:
        wcount += 1
    return wcount

def LetterCount():
    lcount = {}
    counting = file_contents.lower()
    for i in counting:
        if i in lcount:
            lcount[i] += 1 
        else:
            lcount[i] = 1
    return lcount

def main():
    print("-----Begin report-----")
    
    words = WordCount()
    print(f"{words} words found in the document.")

    letters = LetterCount()
    lt = list(letters.items())
    lt.sort()
    for i in lt:
        let = i[0]
        num = i[1]
        if let.isalpha():
            print(f"{num} of {let} found in doc")
        
       
  

    print("-----End report-----")

main()
    

