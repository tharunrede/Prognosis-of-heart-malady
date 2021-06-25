import tkinter
import pandas as pd
from PIL import Image, ImageTk
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler

from sklearn.ensemble import RandomForestClassifier


def Help():
    nwin = tkinter.Toplevel()
    nwin.title("Attribute Description")
    Attributes = Image.open('Attributes.png')
    image2 = Attributes.resize((820, 340), Image.ANTIALIAS)
    Attributes2 = ImageTk.PhotoImage(image2)
    lbl2 = tkinter.Label(nwin, image=Attributes2)
    lbl2.pack()
    nwin.mainloop()


def takeInput():
    inputValues = []

    age1 = ((int(age.get()) - 29) / (77 - 29))
    #print(age1)
    trestbps1 = ((int(rbp.get()) - 94) / (200 - 94))
    chol1 = ((int(serumChol.get()) - 126) / (564 - 126))
    thalach1 = ((int(thalach.get()) - 71) / (202 - 71))
    oldpeak1 = (int(oldpeak.get()) / 6.2)

    inputValues.append(age1)
    inputValues.append(sex.get())
    inputValues.append(chestPain.get())
    inputValues.append(trestbps1)
    inputValues.append(chol1)
    inputValues.append(FBS.get())
    inputValues.append(ECG.get())
    inputValues.append(thalach1)
    inputValues.append(trestbps1)
    inputValues.append(oldpeak1)
    inputValues.append(slope.get())
    inputValues.append(ca.get())
    inputValues.append(thal.get())

    print(inputValues)

    print("\n")

    final_Result = regressor.predict([inputValues])

    print(final_Result)

    substituteWindow = tkinter.Tk()
    substituteWindow.title("HEART DISEASE RESULT")

    substituteWindow['padx'] = 30
    substituteWindow['pady'] = 30

    if final_Result[0] == 1:
        label_1 = tkinter.Label(substituteWindow, text="HEART DISEASE DETECTED", fg='#0080ff',font=('Impact', -35))
        label_1.grid(row=0, column=1, columnspan=6)
        label_2 = tkinter.Label(substituteWindow, text="PLEASE VISIT NEAREST CARDIOLOGIST AT THE EARLIEST", fg='red',font=('Impact', -20))
        label_2.grid(row=1, column=1, columnspan=6)
    else:
        label_1 = tkinter.Label(substituteWindow, text="NO DETECTION OF HEART DISEASES", font=('Impact', -35))
        label_1.grid(row=2, column=1, columnspan=6)
        label_2 = tkinter.Label(substituteWindow, text="Do not forget to exercise daily. ", font=('Impact', -20),
                                fg='green')
        label_2.grid(row=3, column=1, columnspan=6)

    substituteWindow.mainloop()


heart = pd.read_csv("heart.csv")

# we have unknown values '?'  change unrecognized value '?' into mean value through the column

min_max = MinMaxScaler()
columns_to_scale = ['age', 'trestbps', 'chol', 'thalach', 'oldpeak']
heart[columns_to_scale] = min_max.fit_transform(heart[columns_to_scale])

y = heart['target']
X = heart.drop(['target'], axis=1)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

regressor = RandomForestClassifier(n_estimators=100)
regressor.fit(X_train, y_train)

y_pred = regressor.predict(X_test)

print(accuracy_score(y_test, y_pred) * 100, "%")

mainWindow = tkinter.Tk()
mainWindow['padx'] = 30
mainWindow['pady'] = 30
p1 = tkinter.PhotoImage(file='heart.png')

mainWindow.iconphoto(False, p1)
mainWindow.title("HEART DISEASE PREDICTION")

label1 = tkinter.Label(mainWindow, text="HEART DISEASE PREDICTION MODEL", bg='#ff8000')
label1.grid(row=0, column=0, columnspan=6)

label2 = tkinter.Label(mainWindow, text="Enter the details carefully", fg='white', bg='#ff00bf')
label2.grid(row=1, column=0, columnspan=6)

# input Entry
ageFrame = tkinter.LabelFrame(mainWindow, text="Age(yrs)")
ageFrame.grid(row=2, column=0)
age = tkinter.Entry(ageFrame)
age.grid(row=2, column=2)

sexFrame = tkinter.LabelFrame(mainWindow, text="Sex")
sexFrame.grid(row=2, column=1)
sex = tkinter.Entry(sexFrame)
sex.grid(row=2, column=2)

chestPainFrame = tkinter.LabelFrame(mainWindow, text="CP (0-4)")
chestPainFrame.grid(row=2, column=2)
chestPain = tkinter.Entry(chestPainFrame)
chestPain.grid(row=2, column=2)

rbpFrame = tkinter.LabelFrame(mainWindow, text="RBP (94-200)")
rbpFrame.grid(row=3, column=0)
rbp = tkinter.Entry(rbpFrame)
rbp.grid(row=2, column=2)

serumCholFrame = tkinter.LabelFrame(mainWindow, text="Serum Chol")
serumCholFrame.grid(row=3, column=1)
serumChol = tkinter.Entry(serumCholFrame)
serumChol.grid(row=2, column=2)

FBSFrame = tkinter.LabelFrame(mainWindow, text="Fasting BP(0-4)")
FBSFrame.grid(row=3, column=2)
FBS = tkinter.Entry(FBSFrame)
FBS.grid(row=2, column=2)

ECGFrame = tkinter.LabelFrame(mainWindow, text="ECG (0,1,2)")
ECGFrame.grid(row=4, column=0)
ECG = tkinter.Entry(ECGFrame)
ECG.grid(row=2, column=2)

thalachFrame = tkinter.LabelFrame(mainWindow, text="thalach(71-202)")
thalachFrame.grid(row=4, column=1)
thalach = tkinter.Entry(thalachFrame)
thalach.grid(row=2, column=2)

exangFrame = tkinter.LabelFrame(mainWindow, text="exAngina(0/1)")
exangFrame.grid(row=4, column=2)
exang = tkinter.Entry(exangFrame)
exang.grid(row=2, column=2)

oldpeakFrame = tkinter.LabelFrame(mainWindow, text="Old Peak(0-6)")
oldpeakFrame.grid(row=5, column=0)
oldpeak = tkinter.Entry(oldpeakFrame)
oldpeak.grid(row=2, column=2)

slopeFrame = tkinter.LabelFrame(mainWindow, text="Slope(0,1,2)")
slopeFrame.grid(row=5, column=1)
slope = tkinter.Entry(slopeFrame)
slope.grid(row=2, column=2)

caFrame = tkinter.LabelFrame(mainWindow, text=" C. A (0-3)")
caFrame.grid(row=5, column=2)
ca = tkinter.Entry(caFrame)
ca.grid(row=2, column=2)

thalFrame = tkinter.LabelFrame(mainWindow, text=" THAL(0,1,2,3)")
thalFrame.grid(row=6, column=1)
thal = tkinter.Entry(thalFrame)
thal.grid(row=2, column=2)

analyseButton = tkinter.Button(mainWindow, text="PREDICT", bg='red', command=takeInput)
analyseButton.grid(row=8, column=0, columnspan=10)
analyseButton = tkinter.Button(mainWindow, text="HELP", bg='green', command=Help)
analyseButton.grid(row=8, column=1, columnspan=10)

mainWindow.mainloop()
