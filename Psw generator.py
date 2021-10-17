import tkinter as tk
from tkinter import ttk, messagebox
from csv import DictWriter, DictReader, reader, writer
import random
import os



# Main window 
root = tk.Tk()
root.title("Password Generator")
root.geometry("440x200")
root.resizable(0,0)

##################################### Funcationality #########################################

# Color Funcation
def color_changer(file_name, *args):
    with open(file_name, 'r') as rf:
        file_reader = DictReader(rf, fieldnames=['Value', 'DefaultLength', 'DefaultType'])
        next(file_reader)
        for value in file_reader:
            if value['Value']=='Dark':
                bg_color = "Black"
                fg_color = "White"
                break
            else:
                bg_color = "White"
                fg_color = "Black"
                break
    for arg in args:
        try:
            arg.config(bg=bg_color, fg=fg_color)
        except tk.TclError:
            arg.config(bg=bg_color)
        except:
            messagebox.showerror("New Error", "Tell to Rihan Its a new error")


# Update Funcation
def update_data(password, csv_file):
    if os.path.exists(csv_file):
        pass
    else:
        a = open(csv_file, 'w').close()
    with open(csv_file, 'r') as rf:
            file_reader = reader(rf)
            data_list = []
            for row in file_reader:
                data_list.append(row)
            if len(data_list)==6:
                with open(csv_file, 'w', newline='') as wf:
                    file_writer = writer(wf)
                    dict_file_writer = DictWriter(wf, fieldnames=['psw'])
                    data_list.pop(1)
                    for row in data_list:
                        file_writer.writerow(row)
                    dict_file_writer.writerow({'psw':password})
            else:
                 with open(csv_file, 'a', newline='') as af:
                    file_writer = DictWriter(af, fieldnames=['psw'])
                    if os.stat(csv_file).st_size==0:
                        file_writer.writeheader()
                    file_writer.writerow({'psw':password})


# Copy Funcation
def copy():
    copied= psw_entbx.get()
    if copied == "":
        messagebox.showerror("Empty", "Password is not Generated")
    else:
        copy_btn.config(text="Copied")
        root.clipboard_clear()
        root.clipboard_append(copied)


# Generate Funcation 
def generate():
    genrate_btn.config(text="Re Generate")
    copy_btn.config(text="Copy")
    length = length_var.get()
    psw_type= psw_type_var.get()
    length = int(length)

    # generating random numbers Symbols and letters 
    num = tuple(range(0,10))
    symbol = ('!','@','#','$','%','&','*','-','_','+','?')
    letrs=(
        'a','A','b','B','c','C','d','D','e','E','f','F','g','G','h','H','i','I','j','J','k','K','l','L','m','M',
        'n','N','o','O','p','P','q','Q','r','R','s','S','t','T','u','U','v','V','w','W','x','X','y','Y','z','Z'
    )
    if psw_type == "Numeric":
        psw_list = []
        i = 0
        while i < length:
            number= random.choice(num)
            psw_list.append(number)
            i = i +1
    else:
        if psw_type == "Alphabet":
            psw_list = []
            i = 0
            while i < length:
                letter = random.choice(letrs)
                psw_list.append(letter)
                i = i+1

        if psw_type == "Symbol":
            psw_list =[]
            i =0
            while i < length:
                symb = random.choice(symbol)
                psw_list.append(symb)
                i = i+1

        if psw_type == "Alphabet, Numeric":
            psw_list = []
            i = 0
            while i < length:
                number= random.choice(num)
                psw_list.append(number)
                i= i+1
                if i== length:
                    break
                letter = random.choice(letrs)
                psw_list.append(letter)
                i = i +1
        if psw_type == "Alphabet, Symbol":
            psw_list = []
            i = 0
            while i < length:
                letter = random.choice(letrs)
                psw_list.append(letter)
                i= i+1
                if i== length:
                    break
                symb = random.choice(symbol)
                psw_list.append(symb)
                i = i +1

        if psw_type == "Numeric, Symbol":
            psw_list =[]
            i = 0
            while i < length:
                number= random.choice(num)
                psw_list.append(number)
                i= i+1
                if i== length:
                    break
                symb = random.choice(symbol)
                psw_list.append(symb)
                i = i +1

        if psw_type == "Alphabet, Numeric, Symbol":
            psw_list =[]
            i = 0
            while i < length:
                letter = random.choice(letrs)
                psw_list.append(letter)
                i= i+1
                if i== length:
                    break
                number= random.choice(num)
                psw_list.append(number)
                i= i+1
                if i== length:
                    break
                symb = random.choice(symbol)
                psw_list.append(symb)
                i = i +1

    password = str(psw_list)
    password = password.replace(",", "")
    password = password.replace("'", "")
    password = password.replace(" ", "")
    password = password.replace("[", "")
    password = password.replace("]", "")

    psw_entbx.delete(0, tk.END)
    psw_entbx.insert(0, password)

    # writing Passwords in CSV file
    update_data(password, "Password.csv")


# Setting Funcation
def setting_button():
    
    ############# Funcations inside Setting ##################
    def back_button():
        root.title("Password Genrator")
        back_btn.grid_forget()
        frame_inside_setting.grid_forget()

        # Arrangement of main GUI 
        psw_frame.grid(row=2, columnspan=5, padx=15, pady=30)
        setting_btn_frame.grid(row=4, columnspan=2)
        btn_frame.grid(row=4, column=4)
        length_lbl.grid(row=0, column=0, padx=5, pady=10)
        space_lbl.grid(row=0, column=2, padx=20)
        psw_type_lbl.grid(row=0, column=3, padx=5, pady=10, sticky=tk.E)
        psw_lbl.grid(row=0, column=0, padx=10, pady=5)
        length_cmbx.grid(row=0, column=1, padx=5, pady=10, sticky=tk.W)
        psw_type_cmbx.grid(row=0, column=4, padx=5)
        psw_entbx.grid(row=0, column=1, padx=10, pady=5)
        exit_btn.grid(row=0, column=0, padx=5, sticky=tk.W)
        genrate_btn.grid(row=0, column=1, padx=5, sticky=tk.E)
        copy_btn.grid(row=1, column=1)
        setting_btn.grid(row=4, column=0)

        color_changer("Themevalue.csv", root, psw_frame, setting_btn_frame, btn_frame, length_lbl, psw_lbl, 
        psw_type_lbl, space_lbl)

    # Creating "Default" setting
    def set_default():

        ########### Funcations inside Default Setting #################
        def back_button2():
            back_btn2.grid_forget()
            default_length_lbl.grid_forget()
            default_type_lbl.grid_forget()
            set_length_cmbx.grid_forget()
            set_type_cmbx.grid_forget()
            cancel_button.grid_forget()
            submt_btn.grid_forget()

            root.title("Setting")
            back_btn.grid(row=0, column=0)
            frame_inside_setting.grid(row=1, column=1)
        
        # creating exit button 
        def exit_button():
            back_button2()
            back_button()

        #Creating Submit button 
        def submit_button():
            length = set_length_var.get()
            format_type = set_type_var.get()
            with open("Themevalue.csv", 'r') as reading_file:
                file_reader = DictReader(reading_file, fieldnames=['Value', 'DefaultLength', 'DefaultType'])
                next(file_reader)
                value_data = []
                for row in file_reader:
                    value_data.append(row['Value'])
                    break
            with open("Themevalue.csv", 'w', newline='') as w:
                file_writer = DictWriter(w, fieldnames=['Value', 'DefaultLength', 'DefaultType'])
                if os.stat("Themevalue.csv").st_size==0:
                    file_writer.writeheader()
                for i in value_data:
                    file_writer.writerow({'Value':str(i), 'DefaultLength':length, 'DefaultType':format_type})
            messagebox.showinfo("Restart", "Restart app to apply Changes")

        # forgeting main setting
        back_btn.grid_forget()
        frame_inside_setting.grid_forget()
        root.title("Default Setting")

        # Creating GUI for "Default Setting"
        back_btn2 = ttk.Button(root, text="Back", width=5, command=back_button2)
        back_btn2.grid(row=0, column=0)

        # Creating Labels 
        default_length_lbl = tk.Label(root, text="Set Default Length")
        default_length_lbl.grid(row=1, column=1, pady=2)
        
        default_type_lbl = tk.Label(root, text="Set Default Type")
        default_type_lbl.grid(row=2, column=1, pady=2)

        # Creating Combobox
        set_length_var = tk.StringVar()
        set_length_cmbx = ttk.Combobox(root, width=25, textvariable=set_length_var, state='readonly')
        set_length_cmbx['values']=tuple(range(4,21))
        set_length_cmbx.grid(row=1, column=2, padx=10, pady=10)

        set_type_var = tk.StringVar()
        set_type_cmbx = ttk.Combobox(root, width=25, textvariable=set_type_var, state='readonly')
        set_type_cmbx['values']=(
            "Numeric", "Alphabet", "Symbol", "Alphabet, Numeric", 
            "Alphabet, Symbol", "Numeric, Symbol", "Alphabet, Numeric, Symbol",
        )
        set_type_cmbx.grid(row=2, column=2, padx=10, pady=10)
        with open("Themevalue.csv",'r') as reading_file:
            file_reader = DictReader(reading_file, fieldnames=['Value', 'DefaultLength', 'DefaultType'])
            for i in file_reader:
                set_length_cmbx.set(i['DefaultLength'])
                set_type_cmbx.set(i['DefaultType'])


        # Creating Buttons
        cancel_button= ttk.Button(root, text="Exit", command=exit_button)
        cancel_button.grid(row=4, column=2, padx=5, pady=20, sticky=tk.E)
    
        submt_btn = ttk.Button(root, text="Submit", command=submit_button)
        submt_btn.grid(row=4, column=3, pady=20, sticky=tk.W)
    
        # Activating Theme 
        color_changer("Themevalue.csv", root, default_length_lbl, default_type_lbl)

    # Creating recent Passwords setting
    def recent_password():
        
        ############ Funcations inside recent setting #############
        def back_button3():
            back_btn3.grid_forget()
            frame_inside_recent_passwords.grid_forget()

            root.title("Setting")
            back_btn.grid(row=0, column=0)
            frame_inside_setting.grid(row=1, column=1)

        # Creating exit button
        def exit_button():
            back_button3()
            back_button()

        # forgeting main setting 
        back_btn.grid_forget()
        frame_inside_setting.grid_forget()
        root.title("Recent Generated Passwords")
        
        # Creating GUI for Recent Password Setting 
        back_btn3 = ttk.Button(root, text="Back", width=5, command=back_button3)
        back_btn3.grid(row=0, column=0)

        # creating frame 
        frame_inside_recent_passwords = tk.Frame(root)
        frame_inside_recent_passwords.grid(row=1, column=1)

        # creating exit button
        exit_btn = ttk.Button(frame_inside_recent_passwords, text="Exit", command=exit_button)
        exit_btn.grid(row=5, column=2, pady=5)

        # labels 
        space_lbl2 = tk.Label(frame_inside_recent_passwords)
        space_lbl2.grid(row=0, column=0, padx=10)

        r_psw1 = tk.Label(frame_inside_recent_passwords, text="Recent Password 1")
        r_psw1.grid(row=0, column=1, padx=8, pady=3)
        r_psw2 = tk.Label(frame_inside_recent_passwords, text="Recent Password 2")
        r_psw2.grid(row=1, column=1, padx=8, pady=3)
        r_psw3 = tk.Label(frame_inside_recent_passwords, text="Recent Password 3")
        r_psw3.grid(row=2, column=1, padx=8, pady=3)
        r_psw4 = tk.Label(frame_inside_recent_passwords, text="Recent Password 4")
        r_psw4.grid(row=3, column=1, padx=8, pady=3)
        r_psw5 = tk.Label(frame_inside_recent_passwords, text="Recent Password 5")
        r_psw5.grid(row=4, column=1, padx=8, pady=3)
        
        # entry box 
        r_psw1_entbx = tk.Entry(frame_inside_recent_passwords, width=25)
        r_psw1_entbx.grid(row=0, column=2, padx=8)
        r_psw2_entbx = tk.Entry(frame_inside_recent_passwords, width=25)
        r_psw2_entbx.grid(row=1, column=2, padx=8)
        r_psw3_entbx = tk.Entry(frame_inside_recent_passwords, width=25)
        r_psw3_entbx.grid(row=2, column=2, padx=8)
        r_psw4_entbx = tk.Entry(frame_inside_recent_passwords, width=25)
        r_psw4_entbx.grid(row=3, column=2, padx=8)
        r_psw5_entbx = tk.Entry(frame_inside_recent_passwords, width=25)
        r_psw5_entbx.grid(row=4, column=2, padx=8)
        
        # inserting recent password
        with open ("Password.csv", 'r') as rf:
            file_reader = reader(rf)
            r_psw5_entbx.delete(0, tk.END)
            r_psw4_entbx.delete(0, tk.END)
            r_psw3_entbx.delete(0, tk.END)
            r_psw2_entbx.delete(0, tk.END)
            r_psw1_entbx.delete(0, tk.END)
            try:
                next(file_reader)
                r_psw5_entbx.insert(0, next(file_reader))
                r_psw4_entbx.insert(0, next(file_reader))
                r_psw3_entbx.insert(0, next(file_reader))
                r_psw2_entbx.insert(0, next(file_reader))
                r_psw1_entbx.insert(0, next(file_reader))
            except StopIteration:
                pass
    
        r_psw1_entbx.config(state="readonly")
        r_psw2_entbx.config(state="readonly")
        r_psw3_entbx.config(state="readonly")
        r_psw4_entbx.config(state="readonly")
        r_psw5_entbx.config(state="readonly")

        # Activating Theme 
        color_changer("Themevalue.csv", root, frame_inside_recent_passwords, space_lbl2, 
        r_psw1, r_psw2, r_psw3, r_psw4, r_psw5)

    # Creating Theme Setting
    def theme_changer():
        ################ local funcations of theme_changer #################  

        # Creating back button
        def back_button4():
            back_btn4.grid_forget()
            frame_inside_theme_changer.grid_forget()
        
            root.title("Setting")
            back_btn.grid(row=0, column=0)
            frame_inside_setting.grid(row=1, column=1)

        # creating exit button
        def exit_button():
            back_button4()
            back_button()
        
        # Creating Submit Button 
        def submit_button2():
            value = theme_var.get()
            with open("Themevalue.csv", 'r') as reading_file:
                file_reader = DictReader(reading_file, fieldnames=['Value', 'DefaultLength', 'DefaultType'])
                next(file_reader)
                length_type_list = []
                for row in file_reader:
                    length_type_list.append(row['DefaultLength'])
                    length_type_list.append(row['DefaultType'])
                    break
            with open("Themevalue.csv", 'w', newline='') as theme_value:
                file_writer = DictWriter(theme_value, fieldnames=['Value', 'DefaultLength', 'DefaultType'])
                if os.stat("Themevalue.csv").st_size==0:
                    file_writer.writeheader()
                default_length = length_type_list[0]
                default_type = length_type_list[1]
                file_writer.writerow({'Value':value, 'DefaultLength':default_length, 'DefaultType':default_type})
            #Going back to main window
            exit_button()

        # forgeting main setting 
        back_btn.grid_forget()
        frame_inside_setting.grid_forget()
        root.title("Change Theme")

        # Creating GUI Theme Setting 
        back_btn4= ttk.Button(root, text="Back", width=5, command=back_button4)
        back_btn4.grid(row=0, column=0)

        frame_inside_theme_changer=tk.Frame(root)
        frame_inside_theme_changer.grid(row=1, column=1)

        # creating labels    
        slct_lbl = tk.Label(frame_inside_theme_changer, text="Select Theme")
        slct_lbl.grid(row=0, column=0, padx=10, pady=10)
        
        space_lbl2 = tk.Label(frame_inside_theme_changer)
        space_lbl2.grid(row=3, column=0, pady=30)
        
        # creating Combobox
        theme_var = tk.StringVar()
        theme_cmbx = ttk.Combobox(frame_inside_theme_changer, width=20, textvariable=theme_var, state='readonly')
        theme_cmbx['values']=("Light", "Dark")
        theme_cmbx.grid(row=0, column=1, padx=10)
        with open("Themevalue.csv", 'r')as r:
            file_reader = DictReader(r, fieldnames=['Value', 'DefaultLength', 'DefaultType'])
            for row in file_reader:
                theme_cmbx.set(row['Value'])

        # creating Buttons
        exit_btn= ttk.Button(frame_inside_theme_changer, text="Exit", command=exit_button)
        exit_btn.grid(row=4, column=1, padx=5, sticky=tk.E)
 
        submt_btn2 = ttk.Button(frame_inside_theme_changer, text="Submit", command=submit_button2)
        submt_btn2.grid(row=4, column=2, sticky=tk.W)

        # Activating Theme
        color_changer("Themevalue.csv",root, frame_inside_theme_changer, slct_lbl, space_lbl2)

    # Creating about setting
    def about_button():

        # local funcations of about button
        def back_button5():
            back_btn5.grid_forget()
            frame_inside_about.grid_forget()

            root.title("Setting")
            back_btn.grid(row=0, column=0)
            frame_inside_setting.grid(row=1, column=1)
        
        # forgeting main setting 
        back_btn.grid_forget()
        frame_inside_setting.grid_forget()
        root.title("About Password Generator")

        # Creating GUI for About setting
        back_btn5= ttk.Button(root, text="Back", width=5, command=back_button5)
        back_btn5.grid(row=0, column=0)

        space_lbl2 = tk.Label(frame_inside_setting, width=5)
        space_lbl2.grid(row=2, column=2)

        frame_inside_about = tk.Frame(root, highlightthickness=0.5, highlightbackground="Black")
        frame_inside_about.grid(row=1, column=1)
        if os.path.exists("about.txt"):
            with open('about.txt') as about:
                pass
        else:            
            with open('about.txt', 'w', newline='') as about:
                about.write('''Thanks for using Password Generator.

                Does not matter how hard is your password, If it is related to you. Than it is easier to crack it, for someone who knows you. So there will be always a chance to be hacked. To be safe please use "RANDOM PASSWORD'S". If you will use random password's, Than there is not any chance to be Hacked by the someone who knows you.''')

        with open("about.txt") as about:
            file_data = about.read()
            
        text_lbl = tk.Label(frame_inside_about, text=file_data, wraplength=370, justify=tk.LEFT)
        text_lbl.grid()

        # Activating Theme 
        color_changer("Themevalue.csv", root, frame_inside_about, text_lbl, space_lbl2)

    ################### GUI of Main Setting ##############
    # destroying main window GUI
    psw_frame.grid_forget()
    setting_btn_frame.grid_forget()
    btn_frame.grid_forget()
    length_lbl.grid_forget()
    space_lbl.grid_forget()
    psw_type_lbl.grid_forget()
    length_cmbx.grid_forget()
    psw_type_cmbx.grid_forget()
    root.title("Setting")

    back_btn = ttk.Button(root, text="Back", width=5, command=back_button)
    back_btn.grid(row=0, column=0)

    frame_inside_setting = tk.Frame(root)
    frame_inside_setting.grid(row=1, column=1)

    default_setting = ttk.Button(frame_inside_setting, text="Set Default", command=set_default)
    default_setting.grid(row=0, column=0, pady=2)

    recent_psw = ttk.Button(frame_inside_setting, text="Recent", command=recent_password)    
    recent_psw.grid(row=1, column=0, pady=2)

    change_theme = ttk.Button(frame_inside_setting, text="Themes", command=theme_changer)
    change_theme.grid(row=2, column=0, pady=2)

    about_psw= ttk.Button(frame_inside_setting, text="About", command=about_button)
    about_psw.grid(row=3, column=0, pady=2)
    
    exit_btn = ttk.Button(frame_inside_setting, text="Exit", command=back_button)
    exit_btn.grid(row=4, column=0, pady=2)

    # Activating Theme
    color_changer("Themevalue.csv", root, frame_inside_setting)



############################################# Home Window GUI ############################################

# Creating file 
if os.path.exists("Themevalue.csv"):
    if os.stat("Themevalue.csv").st_size==0:
        with open("Themevalue.csv", 'w', newline='') as r:
            file_writer = DictWriter(r, fieldnames=['Value', 'DefaultLength', 'DefaultType'])
            file_writer.writeheader()
            file_writer.writerow({'Value':'Light', 'DefaultLength':4, 'DefaultType':'Numeric'})
    pass

else:
    with open("Themevalue.csv", 'w', newline='') as new_file:
            file_writer = DictWriter(new_file, fieldnames=['Value', 'DefaultLength', 'DefaultType'])
            file_writer.writeheader()
            file_writer.writerow({'Value':'Light', 'DefaultLength':4, 'DefaultType':'Numeric'})




# frames
psw_frame =tk.Frame(root, borderwidth=tk.FALSE)
setting_btn_frame = tk.Frame(root, borderwidth=tk.FALSE)
btn_frame = tk.Frame(root, borderwidth=tk.FALSE)


# labels
length_lbl = tk.Label(root, text="Length")
space_lbl =tk.Label(root)
psw_type_lbl = tk.Label(root, text="Choose Type")
psw_lbl = tk.Label(psw_frame, text="Password", font=("Arial", 15))


# Combobox 
length_var = tk.StringVar()
length_cmbx =ttk.Combobox(root, width=6, state="readonly", textvariable=length_var)
length_cmbx['values']=tuple(range(4,21))


psw_type_var = tk.StringVar()
psw_type_cmbx = ttk.Combobox(root, width=25, state="readonly", textvariable=psw_type_var)
psw_type_cmbx['values']=(
    "Numeric", "Alphabet", "Symbol", "Alphabet, Numeric", 
    "Alphabet, Symbol", "Numeric, Symbol", "Alphabet, Numeric, Symbol",  
)
with open ("Themevalue.csv", 'r')as reading:
    file_reader = DictReader(reading, fieldnames=['Value', 'DefaultLength', 'DefaultType'])
    for i in file_reader:
        length_cmbx.set(i['DefaultLength'])
        psw_type_cmbx.set(i['DefaultType'])


# entry box 
psw_var = tk.StringVar()
psw_entbx = ttk.Entry(psw_frame, width=30)

# Buttons 
exit_btn = ttk.Button(btn_frame, text="Exit", command=exit)
genrate_btn = ttk.Button(btn_frame, text="Generate", command=generate)
copy_btn = ttk.Button(psw_frame, text="Copy", command=copy)
setting_btn = ttk.Button(setting_btn_frame, text="Setting", command=setting_button)



####################### Griding of Home Window ###########################
psw_frame.grid(row=2, columnspan=5, padx=15, pady=30)
setting_btn_frame.grid(row=4, columnspan=2)
btn_frame.grid(row=4, column=4)
length_lbl.grid(row=0, column=0, padx=5, pady=10)
space_lbl.grid(row=0, column=2, padx=20)
psw_type_lbl.grid(row=0, column=3, padx=5, pady=10, sticky=tk.E)
psw_lbl.grid(row=0, column=0, padx=10, pady=5)
length_cmbx.grid(row=0, column=1, padx=5, pady=10, sticky=tk.W)
psw_type_cmbx.grid(row=0, column=4, padx=5)
psw_entbx.grid(row=0, column=1, padx=10, pady=5)
exit_btn.grid(row=0, column=0, padx=5, sticky=tk.W)
genrate_btn.grid(row=0, column=1, padx=5, sticky=tk.E)
copy_btn.grid(row=1, column=1)
setting_btn.grid(row=4, column=0)



# Activating Theme
color_changer("Themevalue.csv", root, psw_frame, setting_btn_frame, btn_frame, length_lbl, psw_lbl, 
psw_type_lbl, space_lbl)

root.mainloop()

# Programmed By RIHAN AHMED
