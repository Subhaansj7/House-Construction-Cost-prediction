

from subprocess import call
import tkinter as tk
import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from PIL import Image, ImageTk
from tkinter import ttk
from sklearn.decomposition import PCA
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score

root = tk.Tk()
root.title("construction cost predication")

w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
# ++++++++++++++++++++++++++++++++++++++++++++

image2 = Image.open('c.webp')

image2 = image2.resize((w, h), Image.ANTIALIAS)

background_image = ImageTk.PhotoImage(image2)


background_label = tk.Label(root, image=background_image)
background_label.image = background_image
background_label.place(x=0, y=0)  # , relwidth=1, relheight=1)



def shift():
    x1,y1,x2,y2 = canvas.bbox("marquee")
    if(x2<0 or y1<0): #reset the coordinates
        x1 = canvas.winfo_width()
        y1 = canvas.winfo_height()//2
        canvas.coords("marquee",x1,y1)
    else:
        canvas.move("marquee", -2, 0)
    canvas.after(1000//fps,shift)

canvas=tk.Canvas(root,bg="sky blue")
canvas.pack()
canvas.place(x=0, y=0)
text_var="Construction Cost Prediction"
text=canvas.create_text(0,-2000,text=text_var,font=('Raleway',25,'bold'),fill='white',tags=("marquee",),anchor='w')
x1,y1,x2,y2 = canvas.bbox("marquee")
width = 1600
height = 80
canvas['width']=width
canvas['height']=height
fps=40    #Change the fps to make the animation faster/slower
shift() 


  #Function Calling
  
  
# """Feature Selection => Manual"""
# x = data.drop(['AHD', 'Series'], axis=1)

data = pd.read_csv(r"Book1.csv")



data = data.dropna()

le = LabelEncoder()
# data['AHD'] = le.fit_transform(data['AHD'])

# data['Thal'] = le.fit_transform(data['Thal'])
# data['ChestPain'] = le.fit_transform(data['ChestPain'])

# data.head()
def Data_Preprocessing():
    data = pd.read_csv(r"Book1.csv")
    data.head()

    data = data.dropna()

    """One Hot Encoding"""

    le = LabelEncoder()
    
    data['bedrooms'] = le.fit_transform(data['bedrooms'])
    
    data['sqft_living'] = le.fit_transform(data['sqft_living'])
    
    data['floors'] = le.fit_transform(data['floors'])

    data['condition'] = le.fit_transform(data['condition'])
    
    data['zipcode'] = le.fit_transform(data['zipcode'])
    #data['Bill_Date'] = le.fit_transform(data['Bill_Date'])
    
    # data['Quantity'] = le.fit_transform(data['Quantity'])
   
  

    """Feature Selection => Manual"""
    x = data.drop(['id','price','yr_built','yr_renovated'], axis=1)
    data = data.dropna()

    print(type(x))
    y = data['price']
    print(type(y))
    x.shape

    from sklearn.model_selection import train_test_split
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=1234)


    

    load = tk.Label(root, font=("Tempus Sans ITC", 15, "bold"), width=50, height=2, background="green",
                    foreground="white", text="Data Loaded=>Splitted into 80% for Training & 20% for Testing")
    load.place(x=280, y=100)

# _+++++++++++++++++++++++++++++++++++++++++++++++++++++++
def Model_Training():
    data = pd.read_csv("Book1.csv")
    data.head()
    data.describe()

    
    from sklearn.linear_model import LinearRegression as svc
    SVM=svc()
    labels=data['price']
    
    #conv_dates = [1 if values == 2014 else 0 for values in data.date]
    #data['date'] = conv_dates
    train1 = data.drop(['id','price','yr_built','yr_renovated'],axis=1)
    
    
    from sklearn.model_selection import train_test_split
    x_train, x_test, y_train, y_test = train_test_split(train1, labels, test_size=0.20,random_state=1)
    
    from sklearn.svm import SVC
    svcclassifier = SVC(kernel='linear')
    svcclassifier.fit(x_train, y_train)

    y_pred = svcclassifier.predict(x_test)
    print(y_pred)
    
    # from sklearn.tree import DecisionTreeClassifier
    # svcclassifier = DecisionTreeClassifier()
    # svcclassifier.fit(x_train, y_train)

    # y_pred = svcclassifier.predict(x_test)
    # print(y_pred)

    print("=" * 40)
    print("==========")
    print("Classification Report : ",(classification_report(y_test, y_pred)))
    print("Accuracy : ",accuracy_score(y_test,y_pred)*100)
    accuracy = accuracy_score(y_test, y_pred)
    print("Accuracy: %.2f%%" % (accuracy * 100.0))
    ACC = (accuracy_score(y_test, y_pred) * 100)
    repo = (classification_report(y_test, y_pred))
    
    #label4 = tk.Label(root,text =str(repo),width=40,height=10,bg='khaki',fg='black',font=("Tempus Sanc ITC",14))
    #label4.place(x=205,y=100)
    
    label5 = tk.Label(root,text ="Model Traning is Completed \nModel model.joblib",width=40,height=3,bg='khaki',fg='black',font=("Tempus Sanc ITC",14))
    label5.place(x=300,y=200)
    from joblib import dump
    dump (svcclassifier,"model.joblib")
    print("Model Traning is Completed \n Model saved as model.joblib")
def listToString(s): 
    
    # initialize an empty string
    str1 = "" 
    
    # traverse in the string  
    for ele in s: 
        str1 = ele  
    
    # return string  
    return str1     
def call_file():

    bedrooms = tk.IntVar()
    sqft_living = tk.IntVar()
    floors = tk.IntVar()
    condition = tk.IntVar()
    yr_built = tk.IntVar()
    yr_renovated = tk.IntVar()
    zipcode = tk.IntVar()
   
    def Detect():
        e1=bedrooms.get()
        print(e1)
        e2=sqft_living.get()
        print(e2)
        e3=floors.get()
        print(e3)
        e4=condition.get()
        print(e4)
        # e5=yr_built.get()
        # print(e5)
        # e6=yr_renovated.get()
        # print(e6)
        e7=zipcode.get()
        print(e7)
       
     
        
        from joblib import dump , load
        a1=load('model.joblib')
        v= a1.predict([[e1, e2, e3, e4,e7]])
        #v=[v]
        
        predicted_price=listToString(v) 
        yes = tk.Label(root,text="construction cost predication  \n " +str(predicted_price),background="gray",foreground="white",font=('times', 20, ' bold '),width=25,height=5)
        yes.place(x=370,y=470)
        

    frame_display = tk.LabelFrame(root, text=" --Display-- ", width=500, height=550, bd=5, font=('times', 14, ' bold '),background="#FAAFBE")
    frame_display.grid(row=0, column=0, sticky='nw')
    frame_display.place(x=800, y=170)
    
    l1=tk.Label(frame_display,text="bedrooms",background="#5E5A80",font=('times', 20, ' bold '),width=10,fg='white')
    l1.place(x=90,y=50)
    bedrooms=tk.Entry(frame_display,bd=2,width=5,font=("TkDefaultFont", 20),textvar=bedrooms)
    bedrooms.place(x=300,y=50)

    l2=tk.Label(frame_display,text="sqft living",background="#5E5A80",font=('times', 20, ' bold '),width=10,fg='white')
    l2.place(x=90,y=100)
    sqft_living=tk.Entry(frame_display,bd=2,width=5,font=("TkDefaultFont", 20),textvar=sqft_living)
    sqft_living.place(x=300,y=100)

    l3=tk.Label(frame_display,text="floors",background="#5E5A80",font=('times', 20, ' bold '),width=10,fg='white')
    l3.place(x=90,y=150)
    floors=tk.Entry(frame_display,bd=2,width=5,font=("TkDefaultFont", 20),textvar=floors)
    floors.place(x=300,y=150)
    
    l4=tk.Label(frame_display,text="condition",background="#5E5A80",font=('times', 20, ' bold '),width=10,fg='white')
    l4.place(x=90,y=200)
    condition=tk.Entry(frame_display,bd=2,width=5,font=("TkDefaultFont", 20),textvar=condition)
    condition.place(x=300,y=200)

    # l5=tk.Label(frame_display,text="yr_built",background="#5E5A80",font=('times', 20, ' bold '),width=10,fg='white')
    # l5.place(x=90,y=250)
    # yr_built=tk.Entry(frame_display,bd=2,width=5,font=("TkDefaultFont", 20),textvar=yr_built)
    # yr_built.place(x=300,y=250)

   
    # l7=tk.Label(frame_display,text="yr_renovated",background="#5E5A80",font=('times', 20, ' bold '),width=10,fg='white')
    # l7.place(x=90,y=300)
    # yr_renovated=tk.Entry(frame_display,bd=2,width=5,font=("TkDefaultFont", 20),textvar=yr_renovated)
    # yr_renovated.place(x=300,y=300)

    l8=tk.Label(frame_display,text="zipcode",background="#5E5A80",font=('times', 20, ' bold '),width=10,fg='white')
    l8.place(x=90,y=250)
    zipcode=tk.Entry(frame_display,bd=2,width=5,font=("TkDefaultFont", 20),textvar=zipcode)
    zipcode.place(x=300,y=250)


    button1 = tk.Button(frame_display,text="Submit",command=Detect,font=('times', 20, ' bold '),width=10)
    button1.place(x=160,y=330)
    

def window():
    root.destroy()


button4 = tk.Button(root, foreground="white", background="black", font=("Tempus Sans ITC", 14, "bold"),
                    text="Prize Prediction", command=call_file, width=20, height=2)
button4.place(x=5, y=300)


# button4 = tk.Button(root, foreground="white", background="black", font=("Tempus Sans ITC", 14, "bold"),
#                     text="model_training", command=Model_Training, width=20, height=2)
# button4.place(x=5, y=400)
button4 = tk.Button(root, foreground="white", background="black", font=("Tempus Sans ITC", 14, "bold"),
                    text="Data Preprocessing", command=Data_Preprocessing, width=20, height=2)
button4.place(x=5, y=400)

exit = tk.Button(root, text="Exit", command=window, width=20, height=2, font=('times', 15, ' bold '),bg="red",fg="white")
exit.place(x=5, y=500)

root.mainloop()



