from tkinter import * 
from tkinter import filedialog
from Internal_functionality import *
files = []
current_page = 0

def home_button():
    try:
        pass
    except:
        pass
def reset_main():
    global main_frame
    main_frame.destroy()
    main_frame = Frame(root)
    main_frame.grid(row=0, column=1)
def close_root():
    root.destroy()
def close_add(preset_name):

    main_frame.destroy()
    run_add(preset_name, files)  
    reset_main()
    main_menu()
def load_preset_buttons():
    # buttons = dict()
    row = 2
    column = 0
    for i in preset_dict:
        buttons[i] = Button(preset_frame, text=i, command=lambda i=i:[run_start_up(i), close_root()], padx=50, pady=10, bg= "#B9E8AB")
        buttons[i].grid(row=row, column=column)
        if column == 3:
            column = 0
            row += 1
        column += 1
def settings():
    reset_main()
    frame1 = Frame(main_frame)
    frame2 = Frame(main_frame)
    frame1.grid(row=0, column=0)
    frame2.grid(row=1, column=0)
    greet = Label(frame1, text="Settings Menu", font=("Arial", 20))
    greet.pack()
    del_but = Button(frame2, text="Delete a preset", bg="#d15c5c", command= lambda: delete_preset_win())
    add_but = Button(frame2, text="Add/Change a preset", bg="#59c9ab", command=lambda:browse_files())
    add_but.grid(row=0, column=0)
    del_but.grid(row=0, column=1)
def delete_preset(i):
    global del_frame
    preset_dict.pop(i, None)
    with open(r'presets.json', 'w') as f:
        json.dump(preset_dict, f)
        del_frame.destroy()
        del_frame = Frame(main_frame)
        del_frame.grid(row=1, column=0)
        load_del_buttons()
def delete_preset_win():
    reset_main()
    global del_frame
    frame1 = Frame(main_frame)
    del_frame= Frame(main_frame)
    frame1.grid(row=0, column=0)
    del_frame.grid(row=1, column=0)
    greet = Label(frame1, text="Select a preset to delete")
    greet.grid(row=0, column=0)
    load_del_buttons()
def load_del_buttons():
    row = 0
    column = 0
    for i in preset_dict:
        del_buttons[i] = Button(del_frame, text=i, command=lambda i=i:[delete_preset(i)], padx=50, pady=10, bg= "#c95959")
        del_buttons[i].grid(row=row, column=column)
        if column == 3:
            column = 0
            row += 1
        column += 1
def browse_files():
    global files
    files = []
    files_pre = filedialog.askopenfilenames(initialdir = "/",
                                          title = "Select a File",
                                          filetypes = (("Applications",
                                                        "*.exe*"),
                                                        ("Shortcuts", ".lnk"),
                                                        ("Internet Shortcuts", ".url"),
                                                       ("All files",
                                                        "*.*")))
    for i in files_pre:
        files.append(i.replace("/", "\\"))
    if files != []:
        entry_preset_num()

def main_menu():
    global preset_frame
    preset_frame = Frame(main_frame)
    preset_frame.grid(row=2, column=0)
    greet = Label(main_frame, text="Preset Windows", font=("Arial", 32))
    load_preset_buttons()

    greet.grid(row=0, column=0)
    run = Label(main_frame, text="Your Presets", padx= 50)
    add_button = Button(main_frame, image=settings1, command=lambda: [settings()])
    run.grid(row=1, column=0)
    add_button.grid(row=0, column=4)


def entry_preset_num():
    reset_main()
    frame2 = Frame(main_frame)
    frame1 = Frame(main_frame)
    frame1.grid(row=1, column=0)
    frame2.grid(row=0, column=0)
    prompt1 = Label(frame2, text="Enter the name of your preset:")
    e1 = Entry(frame2, width=10, bg= "#B9E8AB")
    prompt1.grid(row=0, column=0)
    e1.grid(row=0, column=1)
    but = Button(frame1, text="Confirm", command=lambda: close_add(e1.get()), padx=50, justify=CENTER)
    but.pack()
del_buttons = dict()
buttons = dict()
root = Tk()
settings0 = PhotoImage(file=r"settings_icon.png")
settings1 = settings0.subsample(15, 15)
main_frame = Frame(root)
main_frame.grid(row=0, column=1)
main_menu()


mainloop()