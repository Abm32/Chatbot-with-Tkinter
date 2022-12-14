
from tkinter import *
from datetime import datetime
import calendar
from dotenv import load_dotenv
import wolframalpha
 
# GUI
r = Tk()
r.title("JARVIS")
 
BG_GRAY = "#ABB2B9"
BG_COLOR = "#17202A"
TEXT_COLOR = "#EAECEE"
 
FONT = "Helvetica 14"
FONT_BOLD = "Helvetica 13 bold"
 
# Send function
def send():
    send = "You -> " + e.get()
    txt.insert(END, "\n" + send)
 
    user = e.get().lower()
 
    if (user == "hello"):
        txt.insert(END, "\n" + "Bot -> Hi there, how can I help?")
 
    elif (user == "hi" or user == "hii" or user == "hiiii"):
        txt.insert(END, "\n" + "Bot -> Hi there, what can I do for you?")
 
    elif (user == "how are you"):
        txt.insert(END, "\n" + "Bot -> fine! , what about you")
 
    elif (user == "fine" or user == "i am good" or user == "i am doing good"):
        txt.insert(END, "\n" + "Bot -> Great! how can I help you.")
 
    elif (user == "thanks" or user == "thank you" or user == "now its my time"):
        txt.insert(END, "\n" + "Bot -> My pleasure !")
 
    elif (user == "what are you doing?" or user == "what do you do?" or user == "Whats your job?"):
        txt.insert(END, "\n" + "Bot -> Listening to you")
 
    elif (user == "tell me a joke" or user == "tell me something funny" or user == "crack a funny line"):
        txt.insert(
            END, "\n" + "Bot -> What's brown, hairy and wears sunglasses? A cocont on holiday.! ")
 
    elif (user == "goodbye" or user == "see you later" or user == "see yaa"):
        txt.insert(END, "\n" + "Bot -> Have a nice day!")

    elif (user == "whats the time now" or user == "time" or user == "current time"):
        txt.insert(END, "\n" + "Bot -> Time : "+str(datetime.now().strftime('%H:%M')))

    elif (user == "whats the date" or user == "date" or user == "todays date"):
        txt.insert(END, "\n" + "Bot -> Date : "+str(datetime.now().strftime('%Y-%m-%d')))

    elif (user == "what day is today" or user == "day today" or user == "today is"):
        week_days=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
        daysss = datetime.now().strftime('%Y,%m,%d')
        weekday= calendar.weekday(int(daysss[0:4]),int(daysss[5:7]),int(daysss[8:10]))
        txt.insert(END, "\n" + "Bot -> Day : "+str(week_days[weekday]))
 
    else:
        # Taking input from user
        question = user
  
        # App id obtained by the above steps
        app_id = "AHH934-68RU4X4Q5T"
  
        # Instance of wolf ram alpha 
        # client class
        client = wolframalpha.Client(app_id)
  
        # Stores the response from 
        # wolf ram alpha
        res = client.query(question)
  
        # Includes only text from the response
        answer = next(res.results).text
  
        txt.insert(END, "\n" + "Bot -> Ans : "+answer)
        #txt.insert(END, "\n" + "Bot -> Sorry! I didn't understand that")
 
    e.delete(0, END)
 
 
lable1 = Label(r, bg=BG_COLOR, fg=TEXT_COLOR, text="Welcome", font=FONT_BOLD, pady=10, width=20, height=1).grid(
    row=0)
 
txt = Text(r, bg=BG_COLOR, fg=TEXT_COLOR, font=FONT, width=60)
txt.grid(row=1, column=0, columnspan=2)
 
scrollbar = Scrollbar(txt)
scrollbar.place(relheight=1, relx=0.974)
 
e = Entry(r, bg="#2C3E50", fg=TEXT_COLOR, font=FONT, width=55)
e.grid(row=2, column=0)
 
send = Button(r, text="Send", font=FONT_BOLD, bg=BG_GRAY,
              command=send).grid(row=2, column=1)
 
r.mainloop()

#