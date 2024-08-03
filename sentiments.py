import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from tkinter import *
import tkinter as tk
import tkinter.messagebox
from textblob import TextBlob
import json

root=tk.Tk()
with open('comment_data.json') as data_file:
    data = json.load(data_file)

sentiment_list = []
Total_comment=0
positive_comment=0
negative_comment=0
neutral_comment=0

for x1,y1  in data['comment'].items():
    try:
        Total_comment+=1
        sentence=TextBlob(y1)
        
        if sentence.sentiment.polarity>0:
            positive_comment+=1
        elif sentence.sentiment.polarity<0:
            negative_comment+=1
        else:
            neutral_comment+=1
        sentiment_list.append({"id": x1, "comment": y1, "sentiment_score": sentence.sentiment.polarity })
        
        
    except:
        print ("Fail")
pos=float(positive_comment/Total_comment)*100
neg=float(negative_comment/Total_comment)*100
neu=float(neutral_comment/Total_comment)*100
root.title("Sentiment Analysis")
root.geometry("855x666")
root.configure(bg='white')

class analysis_text():
    def setResult(self, type, res):
                if (type == "neg"):
                   self.negativeLabel.configure(text = "Negative : " + str(res) + " % \n")
                if (type == "neu"):
                    self.neutralLabel.configure( text = "Neutral : " + str(res) + " % \n")
                if (type == "pos"):
                    self.positiveLabel.configure(text = "positive : " + str(res) + " % \n")
    def __init__(self):
        self.negativeLabel = Label(text="Positive:%s " % (pos)+"%",fg="orange",bg="white",font=("Helvetica",20))
        self.negativeLabel.pack()
        self.neutralLabel  = Label(text="Negative:%s " % (neg)+"%",fg="brown",bg="white",font=("Helvetica",20))
        self.neutralLabel.pack()
        self.positiveLabel = Label(text="Neutral:%s " % (neu)+"%",fg="blue",bg="white",font=("Helvetica",20))
        self.positiveLabel.pack()

    def __init__(self):
        self.negativeLabel = Label(text="Positive:%s " % (pos)+"%",fg="green",bg="white",font=("Helvetica",20))
        self.negativeLabel.pack()
        self.neutralLabel  = Label(text="Negative:%s " % (neg)+"%",fg="red",bg="white",font=("Helvetica",20))
        self.neutralLabel.pack()
        self.positiveLabel = Label(text="Neutral:%s " % (neu)+"%",fg="purple",bg="white",font=("Helvetica",20))
        self.positiveLabel.pack()

with open('sentiment_comments.json', 'w') as outfile:
    json.dump(sentiment_list, outfile)

    frameChartsLT=tk.Frame(root)
frameChartsLT.pack()
SentimentListExp=[pos,neg,neu]
myColors=["orange","brown","purple"]
fig=Figure()
ax=fig.add_subplot(111)
ax.pie(SentimentListExp,radius=1,labels=SentimentListExp,colors=myColors)
chart1=FigureCanvasTkAgg(fig,frameChartsLT)
chart1.get_tk_widget().pack()
myanalysis = analysis_text()
root.mainloop()
root.mainloop()
