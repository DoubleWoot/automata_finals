# Importing the regular expression module for the string match
import re
# Importing the tkinter expression module to draw the window
import tkinter as tk

# Initialization of the Window using tkinter
window = tk.Tk()
window.title("Automata Finals Project")
window.geometry("800x600")

#labels for App Header and Instruction for Main text get_substring box
app_header = tk.Label(window, text = "String Matching from a user given text", font =('Arial', 14)).pack(pady=20)
instruction1 = tk.Label(window, text="Enter Text Here:",font =("Arial", 12, "bold")).pack(pady=10)

# Function that gets the text from the text box and the subtring from the entry box
def show_result():
    global show_result #Makes the show_result variable obtainable for the restart() function
    
    # gets the input from the entry and the text_box and converts them to lower case for case sensitivity
    substring = get_substring.get().lower() 
    get_textbox = text_box.get("1.0", "end-1c").lower()
    
    # calls the regular_expression function and puts in into an variable
    result = regular_expression(get_textbox, substring)
    output = "" # Initialization of the output string for the label below
    
    # If else statement for the output string
    if result == 0:
        output = "Your substring doesn't show up in this string!"
    elif result == 1:
        output = "The substring shows up only 1 time!"
    else:
        output = (f"The substring shows up {result} times!")
    
    # This label function prints the output variable on to the window
    show_result = tk.Label(label_frame, text=output, font=("Arial", 10))
    show_result.grid(row=0,column=0)
    
    # acts as a lever switch for the search and restart button
    search_button.config(state=tk.DISABLED)
    restart_button.config(state=tk.ACTIVE)

# this function gets called when the restart_button gets pressed
def restart():
    show_result.destroy() #this function destroys previous output
    
    # these 2 config functions work a lever switche for one another
    search_button.config(state=tk.ACTIVE)
    restart_button.config(state=tk.DISABLED)

    
# main script that uses regular expression to check match between substring to string
def regular_expression(string, substring):
    count = 0
    pattern = re.escape(substring)
    
    # for loop that increments once it detects a match
    for match in re.finditer(pattern, string):
        count += 1
    
    # returns the count variable for printing in the get_text function
    return count

    
#main text get_substring box(big one)
text_box = tk.Text(window, width=110, height=10,font=("Arial", 9))
text_box.pack(pady=10,padx=2)

#instruction and get_substring window for substring
inst_label = tk.Label(window, text="Enter Substring:",font =("Arial", 12, "bold")).pack(pady=10)
get_substring = tk.Entry(window, font =("Arial", 9, ))
get_substring.pack(pady=10)

#search button, needs command attribute
search_button = tk.Button(window, text = "Search!", command=show_result)
search_button.pack(pady=10,padx=20)

#initialization of the label frame which puts the output inside a box
label_frame = tk.LabelFrame(window, text="Result:")
label_frame.pack(pady=20,padx=10)

# label that is inside the label frame initialize previously
lmao = tk.Label(label_frame, text="Click the search button", font=("Arial", 10))
lmao.grid(row=0,column=0)

# initialization of a button that resets the label frame
restart_button = tk.Button(window, text="Restart", command=restart)
restart_button.config(state=tk.DISABLED)
restart_button.pack(pady=15, padx=10)

# this function makes the window show up
window.mainloop()