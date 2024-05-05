from tkinter import *

class Calculator:
  def __init__(self):
    self.GUI = Tk()
    self.expression = ""
    self.operation = StringVar()

    self.GUI.configure(background = "pink")
    self.GUI.title("Kids Calculator")
    self.GUI.geometry("700x500")

    self.create_widgets()

  def create_widgets(self):
    self.expression_field = Entry(
      self.GUI,
      textvariable = self.operation,
      font=('Colibry', 15),
      borderwidth=3,
      justify='right'
    )

    self.expression_field.grid(row=0, column=0, columnspan=4, pady=5, ipadx=50, ipady=10)

    buttons_data = [
      ('1', 'red'), ('2', 'red'), ('3', 'red'), ('+', 'orange'),
      ('4', 'red'), ('5', 'red'), ('6', 'red'), ('-', 'orange'),
      ('7', 'red'), ('8', 'red'), ('9', 'red'), ('*', 'orange'),
      ('C', 'red'), ('0', 'red'), ('=', 'red'), ('/', 'orange'),
      ('M+', 'yellow'), ('MRC', 'yellow'), ('MC', 'yellow')
    ]

    row_Number = 1
    column_Number = 0
  
    for (text, bg_color) in buttons_data:
      button = Button(
        self.GUI,
        text=text,
        fg='black',
        bg=bg_color,
        font=('Colibry', 15),
        height=2,
        width=7,
        borderwidth=0,
        relief="groove"
        ) 
      button.grid(
        row=row_Number,
        column=column_Number,
        pady=5,
        padx=5
        )
  
      if text == 'C':
        button.config(command=self.clear)
      elif text == '=':
        button.config(command=self.calculate)
      elif text == 'M+':
        button.config(command=self.save_to_memory)
      elif text == 'MRC':
        button.config(command=self.retrieve_from_memory)
      elif text == 'MC':
        button.config(command=self.clear_memory)
      else:
        button.config(command=lambda t=text: self.press(t)) 
  
      column_Number += 1
      if column_Number > 3:
          column_Number = 0
          row_Number += 1

  def press(self, num):
    self.expression += str(num)
    self.operation.set(self.expression)

  def calculate(self):
    try:
        result = eval(self.expression)
        self.operation.set(result)
    except Exception:
        self.operation.set("Error")
    finally:
        self.expression = ""

  def clear(self):
    self.expression = ""
    self.operation.set("")

  def save_to_memory(self):
    value = self.operation.get()
    with open("memory.txt", "w") as file:
      file.write(value)

  def retrieve_from_memory(self):
    try:
      with open("memory.txt", "r") as file:
          value = file.read()
          self.expression += value
          self.operation.set(self.expression)
    except FileNotFoundError:
      self.operation.set("Nothing stored yet 🤓")

  def clear_memory(self):
    with open("memory.txt", "w") as file:
      file.write("")
      self.operation.set("Memory Cleared")

  def run_calculator(self):
    self.GUI.mainloop()

if __name__ == "__main__":
  calculator = Calculator()
  calculator.run_calculator()
