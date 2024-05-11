import random, time
import customtkinter as ctk
from customtkinter import CTkFont

#password =1234
# user names
UsernameList=['admin', 'Admin', 'user']

#question & answer
Question = [
    {
        "Que": "Capital of Nepal?",
        "options": ["A) Kathmandu", "B) Pokhara", "C) Lalitpur", "D) Bhaktapur"],
        "answer": "0"
    },
    {
        "Que": "Tallest mountain in Nepal and world?",
        "options": ["A) Annapurna", "B) Kanchenjunga", "C) Mount Everest", "D) Dhaulagiri"],
        "answer": "2"
    },
    {
        "Que": "Traditional Nepali attire for women?",
        "options": ["A) Sari", "B) Lehenga", "C) Kurta-Suruwal", "D) Kimono"],
        "answer": "2"
    },
    {
        "Que": "Festival known for bamboo swings?",
        "options": ["A) Holi", "B) Dashain", "C) Tihar", "D) Indra Jatra"],
        "answer": "1"
    },
    {
        "Que": "Nepali bread made from rice flour?",
        "options": ["A) Roti", "B) Sel Roti", "C) Dhido", "D) Bara"],
        "answer": "2"
    },
    {
        "Que": "Dedicated to goddess Durga, 15 days?",
        "options": ["A) Tihar", "B) Indra Jatra", "C) Dashain", "D) Shivaratri"],
        "answer": "2"
    },
    {
        "Que": "Ancient city, capital of Licchavi kingdom?",
        "options": ["A) Bhaktapur", "B) Patan", "C) Lumbini", "D) Gosaikunda"],
        "answer": "1"
    },
    {
        "Que": "Traditional Newar dish of beans and lentils?",
        "options": ["A) Sel Roti", "B) Yomari", "C) Kwati", "D) Bara"],
        "answer": "2"
    },
    {
        "Que": "Holiest river among Hindus in Nepal?",
        "options": ["A) Seti", "B) Gandaki", "C) Koshi", "D) Bagmati"],
        "answer": "3"
    },
    {
        "Que": "Ancient palace complex with woodcarvings?",
        "options": ["A) Basantapur Durbar Square", "B) Patan Durbar Square", "C) Bhaktapur Durbar Square", "D) Gosaikunda"],
        "answer": "0"
    },
    {
        "Que": "Traditional Nepali rice beer?",
        "options": ["A) Raksi", "B) Chyang", "C) Tongba", "D) Jaand"],
        "answer": "0"
    },
    {
        "Que": "National park with one-horned rhinoceros?",
        "options": ["A) Sagarmatha National Park", "B) Rara National Park", "C) Bardia National Park", "D) Chitwan National Park"],
        "answer": "3"
    },
    {
        "Que": "First person to summit Mount Everest?",
        "options": ["A) Tenzing Norgay", "B) Mingma Sherpa", "C) Apa Sherpa", "D) Pasang Lhamu Sherpa"],
        "answer": "0"
    }
    
    ]

class window(ctk.CTk):
    """The main application window class.
    """
    def __init__(self) -> None:
        # setting the window 
        super().__init__()
        self.geometry("380x500")
        self.minsize(370,490)
        self.title("Ko Bancha karot Pati (login)")
        
        # Call the login page; if login is successful, proceed to the game page else throw warn message
        login_page(self)

        #run
        self.mainloop()
        
class login_page(ctk.CTkFrame): 
    """Initialize the login page & call the widget(the inner login page widgets)
        
            Args:
            window: The main application window.
            
            Attributes:
            window (ctk.CTk): The main application window.

            Methods:
            widgets: Creates and displays the login window name, buttons, (password, username box) ...etc.
            clear_words: it is for clearing the text in password, username box.
            loggin_into: Check the login credentials and navigate to the game page if successful.
            animate_warning:  Display a warning message for a 3 second as various text.
        """
    def __init__(self,window):

        super().__init__(window,fg_color="#279EFF",corner_radius=0)

        # packing the Frame
        self.pack(expand=True,fill="both")

        #  making window instance, 
        self.window=window
        self.widgets()

    def widgets(self):   
        """ Create and layout widgets for the login page. """

        # Create the app title label
        ctk.CTkLabel(self,text="Ko Bancha Karod Pati", corner_radius=30,font= ctk.CTkFont("Freestyle Script",50,weight="bold")
                     ,text_color="#0C356A",fg_color="#97FFF4"
                     ).place(relx=0.069,rely=.1,relwidth=.9)
       
        # Create the login title label
        ctk.CTkLabel(self,text="LOGIN PAGE",font=ctk.CTkFont("Informal Roman",50,weight="bold")
                     ).place(relx=0.1,rely=.3,relwidth=.8,relheight=.060)
        
        # Create and place entry boxes for username and password
        self.username=ctk.CTkEntry(self)
        self.username.insert(0,"UserName here")
        self.password=ctk.CTkEntry(self)
        self.password.insert(0,"Password here")

        #placing the username and the password
        self.username.place(relx=0.1,rely=.6,relwidth=.8,relheight=.060)
        self.password.place(relx=0.1,rely=.7,relwidth=.8,relheight=.060)

        # Bind entry boxes to clear text on click
        self.username.bind("<Button-1>",self.clear_words)
        self.password.bind("<Button-1>",self.clear_words)

        # Create the login button
        self.button= ctk.CTkButton(self,text='Login',command=lambda :self.loggin_into(0))
        self.button.place(relx=0.5,rely=.84,relwidth=.5,relheight=.1,anchor="center")

        # Create the WARNING box
        self.warning_Box_value= ctk.StringVar()
        self.warning_Box=ctk.CTkLabel(self,textvariable=self.warning_Box_value,corner_radius=20)
        self.warning_Box.place(relx=0.1,rely=.5,relwidth=.8,relheight=.04)

        # Bind the Enter key of board to the login function
        self.username.bind("<Return>",self.loggin_into)
        self.password.bind("<Return>",self.loggin_into)

    def clear_words(self,event):
        """Clear the default text in the entry boxes on click

        Args:
            event: The click event. 
        """
        if event.widget.get() == "UserName here": 
            #when text is default, adds "*" in password and clears the text of spefic box as clicked ones
            self.password.configure(show="*")
            self.password.delete(0,"end")
            self.username.delete(0,"end")

        elif event.widget.get() == "Password here": 
            # when clicked the password box then it will only clear the password text  
            event.widget.delete(0,"end")

        elif self.username.get()=="":# if username is empty, then fill it again to let user know what to type in particular box
            self.username.insert(0,"UserName here")

    def loggin_into(self,event):
        """
        Check the login credentials and navigate to the game page if successful.

        Args:
            event: The event triggering the login attempt. >>but not usefull
        """
        if (self.username.get()).upper() in UsernameList and self.password.get() == "1234":
            # gets here when login is success
            self.username_ = self.username.get() # saving the username and destroying everything
            self.destroy()
            Game_page(self.window,self) # calls the game page
            
        elif not self.username.get() or not self.password.get(): 
            #if the entry box are empty then print warning message
            self.animate_warning("Please fill both entry First",True)
       
        else:
            # when the password is wrong throws message  
            self.animate_warning("Wrong password or username",True)
    
    def animate_warning(self,text,visiable):
        """
        Display a warning message for a 3 second as various text.

        Args:
            text: The warning message.
            visible: Whether the warning should be visible or not.
        """
        if visiable==True: # if visiable is true then show the warn text/message
            self.warning_Box_value.set(text)
            self.warning_Box.configure(fg_color="red")
            self.window.after(3000, self.animate_warn,"",False) #call the same function after 3 second, and will redirect to else part becayuse of visible = False.  
        else:   
            # after 3 sec, removes the warn mesg & show normal
            self.warning_Box_value.set("") 
            self.warning_Box.configure(fg_color="#279EFF")  

class Game_page(ctk.CTkFrame):
    """
    Represents the game page where questions, options are displayed and answered.

    Args:
        window (ctk.CTk): The main application window.
        login_page_value (login_page): An instance of the login_page class.

    Attributes:
        window (ctk.CTk): The main application window.
        user_name (str): The username of the player.
        current_question (int): The index of the current question being displayed.
        Money (int): The amount of money earned by the player.
        Asked (list): A list of questions that have been asked.

    Methods:
        upper_segment: Creates and displays the upper segment of the game page.
        down_segment: Creates and displays the question segment of the game page.
        display_the_question: Displays the current question and answer options.
        check: Checks the player's answer and handles display accordingly.
        money_plus: Increases the player's money and updates the display.
        end_game: Displays the end of the game message.
    """
    
    def __init__(self,window,login_page_value):
        super().__init__(window,fg_color="#614BC3",corner_radius=0)
        self.pack(expand=True,fill="both")

        #window setup
        self.window= window
        self.window.geometry("1000x500")
        self.window.title("Ko Bancha karot Pati")

        # definig value    
        self.l_value= login_page_value
        self.user_name=self.l_value.username_
        self.current_question=0
        self.Money=0
        self.Asked=[]
        
        #calling the segments
        self.upper_segment()
        self.down_segment()

    def upper_segment(self):
        #creating the upper segmaent frame
        self.frame_u1= ctk.CTkFrame(self,fg_color="green",corner_radius=0)
        self.frame_u1.place(relx=0,rely=0,relwidth=1,relheight=0.2,anchor="nw")

        # defining the grid for the first frame 
        self.frame_u1.columnconfigure((0,1,2),weight=1,uniform="a")
        self.frame_u1.rowconfigure((0),weight=1,uniform="a")

        #total money
        self.total_money_var=ctk.StringVar(value="Money Earned: Rs.0")
        ctk.CTkLabel(self.frame_u1,textvariable=self.total_money_var,font=CTkFont("Dubai Medium",30,weight="bold")).grid(row=0,column=0,sticky="w",padx=15)
        
        # THE user name
        ctk.CTkLabel(self.frame_u1,text=f"User Name: \" {self.user_name} \"",font=CTkFont("Cooper Black",25)).grid(row=0,column=1,sticky="we")

        # Date
        todays_date=time.strftime(" %Y/%m/%d    ,%H : %M")
        ctk.CTkLabel(self.frame_u1,text=f"Date: {todays_date}").grid(row=0,column=2,sticky="e",padx=14)

    def down_segment(self):
        self.current_question +=1
        #creating the second frame
        self.frame_u2=ctk.CTkFrame(self,corner_radius=0)
        self.frame_u2.place(relx=0,rely=.2,relwidth=1,relheight=0.8,anchor="nw")

        # defining the gridding for second frame
        self.frame_u2.columnconfigure((0,1,2,3),weight=1,uniform="a")
        self.frame_u2.rowconfigure((0,1,2,3,4),weight=1,uniform="a")

        if self.current_question <= len(Question): # only ask the question as the number of question
            # checking and asking only the unasked random question,
            self.selected_question=random.choice([item for item in Question if item not in self.Asked]) #here form questions only reading the number that is not present in asked question list
            self.Asked.append(self.selected_question) # adding the question that is selected into asked list. 

            # calling the displaing the question function
            self.display_the_question()
        else:# if finish the questions then call end_game 
            self.end_game()

    def display_the_question(self):

            ctk.CTkLabel(self.frame_u2,text=f"{self.current_question}){self.selected_question['Que']}",font=CTkFont("Cooper Black",25)
                        ).grid(row=0,column=0,columnspan=4,sticky="nswe")

            self.option=(self.selected_question['options']) # from dictonary retriving the options of particular question

            self.button__=ctk.StringVar(value=9) # setting different value so that it will return to the box without performing any task, when no button are selected
            
            # four radio choose botton, with same text variable, and value from 0 to 3, so that we could know which button is selected
            self.button1=ctk.CTkRadioButton(self.frame_u2,text=self.option[0],variable=self.button__,value=0).grid(row=1,column=1,sticky="w",padx=10)
            self.button2=ctk.CTkRadioButton(self.frame_u2,text=self.option[1],variable=self.button__,value=1).grid(row=1,column=2,sticky="w",padx=10)
            self.button3=ctk.CTkRadioButton(self.frame_u2,text=self.option[2],variable=self.button__,value=2).grid(row=2,column=1,sticky="w",padx=10)
            self.button4=ctk.CTkRadioButton(self.frame_u2,text=self.option[3],variable=self.button__,value=3).grid(row=2,column=2,sticky="w",padx=10)
            
            # defing the next button, which enable when ticked answer
            self.next=ctk.CTkButton(self.frame_u2,text="next")
            self.next.forget()

            # defing the submmit button & call "check function", which check the answer
            self.subbmit=ctk.CTkButton(self.frame_u2,command=self.check,text="Submmit")
            self.subbmit.grid(row=3,column=1,sticky="se",padx=10)

            # right and wrong answer displaing label
            self.rigth_wrong_var= ctk.StringVar()
            self.r_w=ctk.CTkLabel(self.frame_u2,textvariable=self.rigth_wrong_var)
            self.r_w.grid(row=4,column=1,columnspan=2,sticky="we",padx=20)

    def check(self):  
        # it is dedicated to check answer is right or wrong  
        if str(self.button__.get())==self.selected_question["answer"]:
            # when the answer is right call money_plus function that add money and show money added
            self.money_plus()

        elif int(self.button__.get()) == 9:
            # this function works when no button are selected
            return  

        else:
            # when the anwer is wrong it display what is right answer in red back ground
            self.rigth_wrong_var.set(f"Wrong!!, Right answer is \" {self.option[int(self.selected_question['answer'])]}\"")
            self.r_w.configure(fg_color="red")


        self.subbmit.forget()
        self.next=ctk.CTkButton(self.frame_u2,command=self.down_segment ,text="Next")
        self.next.grid(row=3,column=1,sticky="se",padx=10)
                 
    def money_plus(self):
        # this function add the money & display the right answer 
        self.rigth_wrong_var.set("Right Answer, awarded rs.10")
        self.r_w.configure(fg_color="light green",text_color="black")
        self.Money+=10
        self.total_money_var.set(f"Money Earned: Rs.{self.Money}")
        
    def end_game(self):
        # when out of question, this function is runned
        # it display the my total earning with user name
        ctk.CTkLabel(self, text=f"Congratulations {self.user_name}! You earned Rs. {self.Money}",
                     font=CTkFont("Cooper Black", 25)).place(relx=0.5, rely=0.5, anchor="center")


if __name__=="__main__":      
    # calling the main window 
    window()
