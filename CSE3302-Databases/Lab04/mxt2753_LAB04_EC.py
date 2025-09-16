#mxt2753_LAB04_EC.py
#Name:Mary-Rose Tracy
#ID#:1001852753
#Date:11/21/2023
#OS: VS Code Microsoft used, python 3
def LineOPro(Sent,LvlODent): #first lets put the function we need in order to 
    #dent the function that we can call in the original python function
    SentNDent='    '*LvlODent+Sent.strip()
    return SentNDent
with open("input_EC.txt","r")as TheFile:
    #LET'S CALL THE VARIABLES:
    # WE NEED TO: intiialize and set to zero the Level of dent to zero so we can count on it.
    LvlODent=0
    #THREE FALSE intiializers to clarify to the computer if it's true
    StatementIn=False
    StrIn=False
    StatementInTheLine=False
    for Sent in TheFile: #for the sentence in the file
        #NOW WE NEED to initialize variables with in the function.
        i=0
        StatemNew=""
        while i<len(Sent): #while the length of the statement
            LetNumSym=Sent[i] # clarify what the letternumber of symbol is
            if LetNumSym=='"' and(i==0 or Sent[i-1]!='\\'): #we need to handle it- the sentence I mean
                StrIn=not StrIn
            if not StrIn and not StatementIn and LetNumSym=='/'and i+1<len(Sent)and Sent[i+1]=='*': #need to do the block statments
                #like last time
                StatementIn=True
                #If we see the next letter number or symbol we don't care jump
                i+=1
            elif StatementIn and LetNumSym=='*'and i+1<len(Sent) and Sent[i+1]=='/':
                StatementIn=False
                #If we see the next letter number or symbol we don't care jump
                i+=1
            if not StrIn and not StatementIn and LetNumSym=='/'and i+1<len(Sent)and Sent[i+1]=='/':
                StatementInTheLine=True
            #Now ^^^ we have to handle the stentence & their comments

            #THIS IS WHERE I HAD THE MOST TROUBLE WITH THE INDENTIONS SO YEAH. the new is how  I figured it out for the format.
            #INDENTATION PROBLEMS:
            if not StrIn and not StatementIn and not StatementInTheLine:
                if LetNumSym=='{':
                    StatemNew+='\n' #new
                    StatemNew+=LineOPro('{',LvlODent)
                    LvlODent+=1
                    StatemNew+='\n'
                elif LetNumSym=='}':
                    StatemNew+='\n' #new
                    LvlODent-=1
                    StatemNew+=LineOPro('}',LvlODent)
                    StatemNew+='\n'
                elif LetNumSym!='\n':
                    StatemNew+=LetNumSym
            if LetNumSym=='\n': #if there's a statement put it in the next line instead of increastif the indent.
                StatementInTheLine=False
            i+=1
        if StatemNew.strip()!='': #if the sentence is not filled then here's the function for it.
            print(LineOPro(StatemNew,LvlODent))
#We couls do checking, but in the extra credit there's no where does it say it's required.