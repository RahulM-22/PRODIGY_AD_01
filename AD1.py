import tkinter as tk

# Initialize the main window
root = tk.Tk()
root.title("Calculator")

# Entry widget to display the input and output
entry = tk.Entry(root, width=16, font=('Arial', 24), bd=8, insertwidth=4, bg='powder blue', justify='right')
entry.grid(row=0, column=0, columnspan=4)

# Define button click event
def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(number))

# Define clear button
def button_clear():
    entry.delete(0, tk.END)

# Define equals button
def button_equal():
    try:
        result = str(eval(entry.get()))
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Define buttons for the calculator
buttons = [
    '7', '8', '9', '/', 
    '4', '5', '6', '*', 
    '1', '2', '3', '-', 
    '0', 'C', '=', '+'
]

# Arrange buttons in a grid
row_val = 1
col_val = 0
for button in buttons:
    if button == '=':
        tk.Button(root, text=button, padx=20, pady=20, font=('Arial', 18), bg='green', fg='white', command=button_equal).grid(row=row_val, column=col_val, columnspan=2, sticky="nsew")
        col_val += 1
    elif button == 'C':
        tk.Button(root, text=button, padx=20, pady=20, font=('Arial', 18), bg='red', fg='white', command=button_clear).grid(row=row_val, column=col_val, sticky="nsew")
    else:
        tk.Button(root, text=button, padx=20, pady=20, font=('Arial', 18), command=lambda num=button: button_click(num)).grid(row=row_val, column=col_val, sticky="nsew")
    
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Run the main loop
root.mainloop()
