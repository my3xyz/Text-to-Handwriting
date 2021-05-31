from PIL import Image
from fpdf import FPDF

img=Image.open("C:/Users/Maithri/Desktop/Text to handwriting/file/bg.png") #opening background image
sizeOfSheet=img.width #setting the size of sheet as bg image's width
gapHorizontal,gapVertical=40,0 #width and height of page
allowedchar='qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM(),.?;1234567890$_' #allowed characters

def Write(char): #a function to write characters
    if char=='\n': #end of line
        global gapHorizontal,gapVertical #declare it as global so it can be accessed anywhere
        gapHorizontal=40 #setting initial starting point
        gapVertical+=200 #next sentence so, increase height by 200 px
    else:
        char.lower() #lowercase characters
        cases=Image.open("C:/Users/Maithri/Desktop/Text to handwriting/file/%s.png"%char) #find the image
        img.paste(cases,(gapHorizontal,gapVertical)) #paste the image
        size=cases.width #the size is set to image's width
        gapHorizontal+=size #size is increased by the size of the alphabet
        del cases #alphabet is deleted

def Letters(word):
    global gapHorizontal,gapVertical
    if gapHorizontal > sizeOfSheet-95*(len(word)):
        gapHorizontal=40 #width becomes 0
        gapVertical+=200 #starts at a new line
    for letter in word:
          if  letter in allowedchar:
            if letter.islower():
                pass
            elif letter.isupper():
                letter.lower()
                letter+="upper"
            elif letter=='.':
                letter="fullstop"
            elif letter==',':
                letter="comma"
            elif letter=='-':
                letter="hiphen"
            elif letter=='!':
                letter="exclamation"
            elif letter=='?':
                letter="question"
            elif letter=='(':
                letter="bracketopen"
            elif letter==')':
                letter="bracketclose"
            elif letter =='$':
                letter='\n'
            elif letter=='_':
                letter='point'
            Write(letter)


def Word(i): #function to split sentence into words
    sentenceList = i.split(' ')
    for j in sentenceList:
        Letters(j) #passing a word to the letters function
        Write('space') #A space printed after each word


def Sentence(Input): #function to split the file into sentences
    sentenceList = Input.split('$') #split by "$" which indicates the start of next line
    for i in sentenceList:
        Word(i) #each sentence is passed to word function
        Write('\n') #next line is passed to write function

if __name__=='__main__':

    try:
        with open("text.txt",'r') as file:
            data=file.read().replace('\n','')
            l=len(data)
            nn=len(data)//450 #this number cuts to the number of characters in a page, reducing the number reduces the number of characters in a page
            #print(nn)
            #print(l)
            chunks,chunk_size=len(data),len(data)//nn #(this number represents the number of characters)
            #print(chunks)
            #print(chunk_size)
            p=[data[i:i+chunk_size] for i in range(0,chunks,chunk_size)]

            for i in range(0,len(p)):
               Sentence(p[i])
               img.save("C:/Users/Maithri/Desktop/Text to handwriting/file/%doutt.png"%i)
               img1=Image.open("C:/Users/Maithri/Desktop/Text to handwriting/file/bg.png")
               img=img1
               gapHorizontal,gapVertical=40,0
    except ValueError as E:
        print("{}\nTry again",format(E))

    imageList=[]
    for i in range(0,len(p)):
        imageList.append("C:/Users/Maithri/Desktop/Text to handwriting/file/%doutt.png"%i)

#for creating pdf
    cover=Image.open(imageList[0])
    width,height=cover.size
    pdf=FPDF(unit="pt",format=[width,height])
    for i in range(0,len(imageList)):
        pdf.add_page()
        pdf.image(imageList[i],0,0)
    pdf.output("C:/Users/Maithri/Desktop/Text to handwriting/file/new.pdf")