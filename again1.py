from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
from difflib import SequenceMatcher
from tkinter.messagebox import showinfo
from tkinter import font
from tkinter import colorchooser

splash = Tk()
splash.title("Intro")
splash.geometry("1000x600+145+50")
splash.overrideredirect(True)
splash.iconbitmap("images/ico1.ico")

# Define image as background
bg = ImageTk.PhotoImage(file="images/splash1.png")
bg_label = Label(splash, image=bg)
bg_label.pack()

def mainWindow():
    splash.destroy()
    root = Tk()
    root.title("NotePad")
    root.geometry("1000x600+145+50")
    root.iconbitmap("images/ico1.ico")
    root.resizable(0,0)

    #Set variable for open filename
    global open_status_name
    open_status_name = False

    # Create New File Function
    def new_file():
        text.delete("1.0", END)
        root.title("New File - TextPad!")
        #status_bar.config(text = "New File       ")
        global open_status_name
        open_status_name = False

    # Open txt file
    def open_file():
        text.delete("1.0", END)
        ## Open a existing file
        text_file = filedialog.askopenfilename(initialdir="/Documents",
                                              title="Select a file",
                                              filetypes=(("text files", "*.txt"), ("python files", "*.py"),
                                                        ("all files", "*.*")))
        # Make an existing file global
        if text_file:
            global open_status_name
            open_status_name = text_file

        root.title(f"Opened File- {text_file}")
        #open file
        text_file = open(text_file, 'r')
        stuff = text_file.read()

        text.insert(END, stuff)
        text_file.close()


    # Save as file
    def save_as():
        text_file = filedialog.asksaveasfilename(defaultextension= ".*", initialdir = "/Documents",
                                            title = "Save file",
                                            filetypes = (("text Files", "*.txt"),
                                              ("all files", "*.*")))
        if text_file:
            root.title(f"{text_file}")
            #Save it
            text_file = open(text_file , 'w')
            text_file.write(text.get(1.0, END))
            text_file.close()

    # Save the existing file
    def save():
        global open_status_name
        if open_status_name:
            root.title("Save File")
            # Save it
            text_file = open(open_status_name, 'w')
            text_file.write(text.get(1.0, END))
            text_file.close()

            showinfo("Saved", "Your file is saved.")
        else:
            save_as()

    # Cut and copy text
    def cut():
        text.event_generate(("<<Cut>>"))

    # Copy text
    def copy():
        text.event_generate(("<<Copy>>"))

    #Paste text
    def paste():
        text.event_generate(("<<Paste>>"))

    #Undo the task
    def undo():
        text.event_generate(("<<Undo>>"))

    #Redo the task
    def redo():
        text.event_generate(("<<Redo>>"))

    def about():
        showinfo("Notepad", "Notepad by SID")

    #help Function
    def help():
        showinfo("Help", "Please visit the website mentioned below for help.")

    def bold():
        #Create our font
        bold = font.Font(text, text.cget("font"))
        bold.configure(weight = "bold")
        #Configure
        text.tag_configure("bold", font = bold)

        current_tags = text.tag_names("sel.first")
        if "bold" in current_tags:
            text.tag_remove("bold", "sel.first", "sel.last")
        else:
            text.tag_add("bold", "sel.first", "sel.last")

    # Create italic font
    def italic():
        #Create our font
        italic = font.Font(text, text.cget("font"))
        italic.configure(slant = "italic")
        #Configure
        text.tag_configure("italic", font = italic)

        current_tags = text.tag_names("sel.first")
        if "italic" in current_tags:
            text.tag_remove("italic", "sel.first", "sel.last")
        else:
            text.tag_add("italic", "sel.first", "sel.last")

    # Create text colour
    def color_txt():
        #pick a color
        my_color = colorchooser.askcolor()[1]
        if my_color:
            #Create our font
            color = font.Font(text, text.cget("font"))

            #Configure a tag
            text.tag_configure("colored", font = color, foreground = my_color)

            current_tags = text.tag_names("sel.first")
            if "colored" in current_tags:
                text.tag_remove("colored", "sel.first", "sel.last")
            else:
                text.tag_add("colored", "sel.first", "sel.last")


    #Define image as background
    bg1 =ImageTk.PhotoImage(file ="images/notepad.png")
    bg_label = Label(root, image = bg1)
    bg_label.place(x = 0, y = 0)

    #Create Main Frame
    frame = Frame(root)
    frame.place(x=90, y=90)

    #Create Vertical Scrollbar
    scroll_bar = Scrollbar(frame)
    scroll_bar.pack(side = RIGHT, fill = Y)

    #Create Horizontal Scrollbar
    scroll_hor = Scrollbar(frame, orient = "horizontal")
    scroll_hor.pack(side = BOTTOM, fill = X)

    #Create Text
    text = Text(frame, width = 103, height = 27, selectbackground = "green", selectforeground = "white", undo = True, yscrollcommand = scroll_bar.set, xscrollcommand = scroll_hor.set, wrap = "none")
    text.pack()

    #Configure our scrollbar
    scroll_bar.config(command = text.yview)
    scroll_hor.config(command= text.xview)

    #create Menu
    my_menu = Menu(root)
    root.config(menu = my_menu)

    #Add file menu
    file_menu = Menu(my_menu, tearoff = 0)
    my_menu.add_cascade(label = "File", menu = file_menu)
    file_menu.add_command(label = "New", command = new_file)
    file_menu.add_command(label = "Open", command = open_file)
    file_menu.add_command(label = "Save", command = save)
    file_menu.add_command(label = "Save as", command = save_as)
    file_menu.add_separator()
    file_menu.add_command(label = "Exit", command = root.destroy)

    #Add Edit Menu
    edit_menu = Menu(my_menu, tearoff = 0)
    my_menu.add_cascade(label = "Edit", menu = edit_menu)
    edit_menu.add_command(label = "Cut", command = cut)
    edit_menu.add_command(label = "Copy", command = copy)
    edit_menu.add_command(label = "Paste", command = paste)
    edit_menu.add_command(label = "Undo", command = undo)
    edit_menu.add_command(label = "Redo", command = redo)

    #Add Help Menu
    help_menu = Menu(my_menu, tearoff = 0)
    my_menu.add_cascade(label = "Help",menu = help_menu)
    help_menu.add_command(label = "Help", command = help)

    #bold button
    bold = Button(root, text = "Bold", font='sans 10 bold', borderwidth = 0, cursor="hand2", command = bold)
    bold.place(x = 100, y = 62)

    italic = Button(root, text = "Italics", font='sans 10', borderwidth = 0, cursor="hand2", command = italic)
    italic.place(x = 150, y = 62)

    text_color = Button(root, text = "Text Color", font = 'sans 10', borderwidth = 0, cursor = "hand2", command = color_txt)
    text_color.place(x = 200, y = 62)
    #status_bar = Label(root, text = "Ready         ", anchor = E)
    #status_bar.pack(fill = X , side = BOTTOM, ipady = 5)


    # Create a new window
    def newWindow():
        top = Toplevel()
        top.title("Notepad2")
        top.geometry("1000x600+145+50")
        top.iconbitmap("images/ico1.ico")
        top.resizable(0,0)

        # Open txt file
        def open_file1():
            text1.delete("1.0", END)
            ## Open a existing file
            text_file1 = filedialog.askopenfilename(initialdir="/Documents",
                                                   title="Select a file",
                                                   filetypes=(("text files", "*.txt"), ("python files", "*.py"),
                                                              ("all files", "*.*")))
            # Make an existing file global
            if text_file1:
                global open_status_name1
                open_status_name1 = text_file1

            top.title(f"Opened File- {text_file1}")
            # open file
            text_file1 = open(text_file1, 'r')
            stuff1 = text_file1.read()

            text1.insert(END, stuff1)
            text_file1.close()

        #Function to detect plag
        def plag():
            '''Similarity between two text files is being checked and the result is
            being provided in percentage.'''
            # Create new window for result
            ans = Toplevel()
            ans.overrideredirect(True)
            ans.geometry("600x400+200+80")

            # Define image as background
            bg2 = ImageTk.PhotoImage(file="images/result.png")
            bg_label2 = Label(ans, image=bg2)
            bg_label2.pack()

            file1 = open(open_status_name, 'r')
            file2 = open(open_status_name1, 'r')
            file1data = file1.read()
            file2data = file2.read()
            similarity = SequenceMatcher(None, file1data, file2data).ratio()
            result = similarity * 100

            percentage1 = Label(ans, text = "The Similarity between these two files is", font = '10', bg = "#ededed")
            percentage1.place(x = 130, y = 130)
            percentage = Label(ans, text= result, bg = "#ededed", fg = "RED", font = "10")
            percentage.place(x = 270, y = 190)
            per = Label(ans, text = "%", bg = "#ededed", fg = "RED", font = "10")
            per.place(x=330, y=190)
            #Exit Button
            exit = Button(ans, text = "EXIT", font = ("Lucida Sans", 12), bg = "#9d9d9c", fg = "BLACK", activebackground = "#9d9d9c",
                          borderwidth = 0, cursor="hand2", command = ans.destroy)
            exit.place(x = 280, y = 287)

            ans.mainloop()

        # Define image as background
        bg1 = ImageTk.PhotoImage(file="images/notepad.png")
        bg_label1 = Label(top, image=bg1)
        bg_label1.place(x=0, y=0)

        # Create Main Frame
        frame1 = Frame(top)
        frame1.place(x=90, y=90)

        # Create Vertical Scrollbar
        scroll_bar1 = Scrollbar(frame1)
        scroll_bar1.pack(side=RIGHT, fill=Y)

        # Create Horizontal Scrollbar
        scroll_hor1 = Scrollbar(frame1, orient="horizontal")
        scroll_hor1.pack(side=BOTTOM, fill=X)

        # Create Text
        text1 = Text(frame1, width=103, height=27, selectbackground="green", selectforeground="white", undo=True,
                    yscrollcommand=scroll_bar1.set, xscrollcommand=scroll_hor1.set, wrap="none")
        text1.pack()
        #text1.config(state='disabled')

        # Configure our scrollbar
        scroll_bar1.config(command=text.yview)
        scroll_hor1.config(command=text.xview)

        # create Menu
        my_menu1 = Menu(top)
        top.config(menu=my_menu1)

        # Add file menu
        file_menu1 = Menu(my_menu1, tearoff=0)
        my_menu1.add_cascade(label="File", menu=file_menu1)
        file_menu1.add_command(label="Open", command=open_file1)
        file_menu1.add_separator()
        file_menu1.add_command(label="Exit", command=top.destroy)

        plag_button1 = Button(top, text = "Check Plagiarism", font = ("Lucida Sans", 12), bg = "#9d9d9c", fg = "BLACK",
                              activebackground = "#9d9d9c", borderwidth = 0, cursor="hand2", command = plag)
        plag_button1.place(x = 780, y = 13)

        top.mainloop()
    plag_button = Button(root, text = "Check Plagiarism", font = ("Lucida Sans", 12), bg = "#9d9d9c", fg = "BLACK", activebackground = "#9d9d9c",
                          borderwidth = 0, cursor="hand2",  command = newWindow)
    plag_button.place(x = 780, y = 13)

    root.mainloop()

#Splash Screen Timer
splash.after(600, mainWindow)

splash.mainloop()