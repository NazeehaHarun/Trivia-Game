
#Opens and reads the text file which stores questions/answers/repeat in a line-by-line breakdown
filename= "triviaGameQuestionsAndAnswersFile.txt"
filein = open(filename, "r") 

score = 0 
highscore = 0
highname = ""
checkerVar = True
name= input("Enter your name: ")

#Code reads the first line of the file which is a question
question = filein.readline().strip()

while checkerVar:
    answer = filein.readline().strip()
        
    print ("Your question is:" , question) 
    useranswer = input("Input your answer: ") 
    #If user inputs "q", the loop breaks so that the user can quit the game.
    if useranswer == 'q':
        checkerVar = False
        break
        
    #Updates the score of the user based on their answer
    #Converts the user's answers and the answer read from file to lower case
    #Removes white spaces between the words of the user's answers and the answers read from the file
    if  useranswer.lower().replace(" ","") == answer.lower().replace(" ",""):
        score = score + 2 
    else:
        score = score - 1
        
    #Stores the name of the user and their highest score
    if score > highscore:
        highscore = score
        highname = name
        
    question = filein.readline().strip()
    #Breaks the loop after reaching the last line of the file
    if (question == ""):
        checkerVar = False
        
filein.close()

#Prints the name of the user and their highest score
print (name, "your highest score is:" , highscore)