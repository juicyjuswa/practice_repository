from tkinter import *

texteula= """...TERMS & CONDITION...
Welcome to (Assignment_2)! We are committed to protecting your privacy and 
ensuring that your personal information is handled in a safe and responsible 
manner. As part of the normal operation of our program, we collect and, in some 
cases, disclose information about you. This Privacy Policy describes the 
information we collect about you and what may happen to that information.

1. Information We Collect
We may collect the following information when you use our program:
- Name
- Age
- Address

2. How We Use Your Information
We use your information for:
- My Grades

3. Sharing Your Information
We do not sell, trade, or otherwise transfer your personal information to 
outside parties. This does not include trusted third parties who assist us 
in operating our program, conducting our business, or servicing you, so long 
as those parties agree to keep this information confidential.

4. Security of Your Information
We implement a variety of security measures to maintain the safety of your 
personal information when you enter, submit, or access your personal
information.

5. Changes to Our Privacy Policy
If we decide to change our privacy policy, I will post those changes
 on this page in the README.md.

6. Contacting Us
If there are any questions regarding this privacy policy, you may contact
me using the information below:
[134273315+juicyjuswa@users.noreply.github.com]

By pressing ACCEPT, you consent to our privacy policy.
"""

Eula = Tk()
Eula.title('End User Agreement')

scroll = Scrollbar(Eula)
scroll.pack(side=RIGHT, fill=Y)

eula = Text(Eula, wrap=NONE, yscrollcommand=scroll.set)
eula.insert("1.0", texteula)
eula.pack()
button= Button(Eula,text='ACCEPT',command=Eula.destroy)
button.pack(side=LEFT)
button2= Button(Eula,text='DECLINE')
button2.pack(side=RIGHT)

scroll.config(command=eula.yview)
mainloop()

from tkinter import *

def action ():
    name = entryName.get ()

    age = int(entryAge.get())

    age_1 = entryAge.get ()

    address = entryAddress.get()

    if age < 18:
        lblResult['text'] = "Welcome :\n " + name + " who is " + age_1 + " Years Old \n" + " and lives at " + address + " You are minor ! "
    else : 
        lblResult['text'] = "Welcome :\n " + name + " who is " + age_1 + " Years Old \n" + "and lives at " + address +  " You are adult ! "

root = Tk ()
root.geometry ("650x250")

lblName = Label (root, text = "Enter your name")
lblName.place (x = 50, y = 20)
entryName = Entry (root)
entryName.place (x = 230, y = 20 , width = 200)

lblAge = Label (root, text = "Enter your age :")
lblAge.place (x = 50, y = 50)
entryAge = Entry (root)
entryAge.place (x = 230, y = 50 , width = 200)

lblAddress = Label (root, text = "Enter your Address :")
lblAddress.place (x = 50, y = 80)
entryAddress = Entry (root)
entryAddress.place (x = 230, y = 80 , width = 200)

lblResult = Label (root, text = "..............................................")
lblResult.place (x = 230, y = 110)

Validate = Button (root, text = "Validate", command = action)
Validate.place (x = 230, y = 180, width = 200)
                
root.mainloop ()