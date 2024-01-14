import random
import pyttsx3
from playsound import playsound


engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voices',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def application(schoolname,location,leavefor,date,name):
    return f'''
    to
    the printciple of {schoolname}
    {location}
    
    dear sir,
            I beg to say that I am suffering from feaver since {date} and doctor 
            has recommended me for {leavefor} leave 
            
    So,
        kindly grant me {leavefor} days leave
    thank you,
            
    your sincearly
        {name}'''

speak("hello user how may i help you")
while(True):
    
    inp=input(" ")

    #joke=random.randint(1,8)
    joke=1

    if(inp=="tell a joke"):
        if(joke==1):
            speak('''now i will tell you a joke ,in a train 4 peoples are travelling ,one is from america,one is from canada,one is from iran,
            one is from india, the one from iran said ,we have alot of crued oil in our country and throws a bottle of crued oil,
            the one from canada said we have alot of water in our country and thrown some bottles filled with water,
            the one from amarica said that we have alot of money in our country and thrown a suitcase filled with money
            and the one from india said we have alot of peoples in my country and thrown all of them out of the train 
            ha ha ha ha i know i am so funny, enjoy rest  ,for more jokes''')
        if(joke==2):
            speak('''one day a forigner was eating paaan in varaansi and he asked the owner of that shop where i can throw this paaan 
            then the shop owner replyed go straight  you will find a machine of red color and black button when you will press black buttonit will open and then trow your paaan inside that machine 
            and then he did the same and seen a girl having red mackup on her face and black spot on her face when
            the foraigner the''')
        if(joke==3):
            pass
        if(joke==4):
            pass
        if(joke==5):
            pass
        if(joke==6):
            pass
        if(joke==7):
            pass
        if(joke==8):
            pass
        
        
    dict={
        "hello":"hi",
        "goodmorning":"thankyou",
        "good morning":"thanks alot",
        "fine":"well thats great",
        "i am fine":"ok",
        "how are you":"i am fine ,what about you",
        " ":" what is that please enter something that makes sense",
        "q":"q, what is that please enter something that makes sense",
        "w":"w, what is that please enter something that makes sense",
        "e":"e, what is that please enter something that makes sense",
        "r":"r, what is that please enter something that makes sense",
        "t":"t, what is that please enter something that makes sense",
        "y":"y, what is that please enter something that makes sense",
        "you":"u, what, i am sorry  if i did something wrong ",
        "u":"u, what is that please enter something that makes sense",
        "i":"i, what is that please enter something that makes sense",
        "o":"o, what is that please enter something that makes sense",
        "p":"p, what is that please enter something that makes sense",
        "a":"a, what is that please enter something that makes sense",
        "s":"s, what is that please enter something that makes sense",
        "d":"d, what is that please enter something that makes sense",
        "f":"f, what is that please enter something that makes sense",
        "g":"g, what is that please enter something that makes sense",
        "h":"h, what is that please enter something that makes sense",
        "j":"j, what is that please enter something that makes sense",
        "k":"k, what is that please enter something that makes sense",
        "l":"l, what is that please enter something that makes sense",
        "z":"z, what is that please enter something that makes sense",
        "x":"x, what is that please enter something that makes sense",
        "c":"c, what is that please enter something that makes sense",
        "v":"v, what is that please enter something that makes sense",
        "b":"b, what is that please enter something that makes sense",
        "n":"n, what is that please enter something that makes sense",
        "m":"m, what is that please enter something that makes sense",
        
        "who is divyakant":"divyakant is divyanshu sirs best friend",
        "who is the prime minister of india":"modi ji is the prime minister of india ",
        "who are you":"a am assistant of divyanshu sir",
        "what can you do":"i can answer any question in the world",
        "who is divyakant":"he is divyanshu sir best friend",
        "who developed you":"divyanshu",
        "who is your developer":"gulugole",
        "who is kajal didi":"kajal didi is the best sister of divyanshu sir",
        "":"",
        "":"",
        "":"",
        "":"",
        "":"",
        "":"",
        "":"",
        "":"",
        "":"",
        "":"",
        "":"",
        "":"",
        "":"",
        "":"",
       
    }
    if(inp=="rock"):
        speak("choos one from stone paper sceisor make sure enter correct spelling")
        i=11
        p=0
        c=0
        while(i>=1):
            i-=1
            print(f"chanses remaining {i+1}")
            speak(f"chanses remaining {i+1}")
            a=random.randint(1,3)
            if(a==1):
                comp="stone"
            if(a==2):
                comp="paper"
            if(a==3):
                comp="scisor"
            player=input("stone,paper,scisor : \n")

                
            if(comp=="stone"):
                if(player=="scisor"):
                    print(f"computer choose {comp} you lose")
                    speak(f"computer choose {comp} you lose")
                    c+=1
                if(player=="paper"):
                    print(f"computer choose {comp} you win")
                    speak(f"computer choose {comp} you win")
                    p+=1
            if(comp=="paper"):
                if(player=="stone"):
                    print(f"computer choose {comp} you lose")
                    speak(f"computer choose {comp} you lose")
                    c+=1
                if(player=="scisor"):
                    print(f"computer choose {comp} you win")
                    speak(f"computer choose {comp} you win")
                    p+=1
            if(comp=="scisor"):
                if(player=="paper"):
                    print(f"computer choose {comp} you lose")
                    speak(f"computer choose {comp} you lose")
                    c+=1
                if(player=="stone"):
                    print(f"computer choose {comp} you win")
                    speak(f"computer choose {comp} you win")
                    p+=1

            if(player==comp):
                print(f"computer choose {comp} its a tie")
                speak(f"computer choose {comp} its a tie")
                p+=1
                c+=1
            print(f"                                computer point [{c}] your point [{p}]")
            speak(f"computer point [{c}] your point [{p}]")
        if(p==c):
            print("it is a tie")
            speak("it is a tie")
        if(p>c):
            print("yeh you defeted computer winner ")
            speak("yeh you defeted computer winner ")
        else:
            print("oh you are defeted by the computer ")
            speak("oh you are defeted by the computer ")
    elif(inp=="introduce"):
        playsound("inro.mp3")
    elif("letter" in inp):
        print('''
make sure to enter "Sclool's Name","School's Location","How Many days you want leave for","todays date","your name" respectively
''')
        speak('''
make sure to enter "Sclool's Name","School's Location","How Many days you want leave for","todays date","your name" respectively
''')
        schoolname=input("enter your school name")
        location=input()
        leavefor=input()
        date=input()
        name=input()
        out=application(schoolname,location,leavefor,date,name)
        print(out)
        f=open("leave.txt","w")
        f.write(out)
        print("we have made a file in this folder")

    else:
        speak(dict.get(inp))

