import csv
from tkinter import *
import random

root = Tk()
root.geometry('400x250')

todoInp = ""
todos = list()

def updateTodo():
    todoTask = addTodoInput.get()
    with open('todoList.csv', 'w', newline='') as todo:
        writer = csv.writer(todo)
        todos.append(todoTask)
        for tasks in todos:
            writer.writerow([tasks, 0])

theLabel = Label(root, text="To-do list")
space = Label(root, text=" ")

addTodoLabel = Label(root, text="Add to-do:")
addTodoInput = Entry(root, textvariable = todoInp)

sub_btn = Button(root,text = 'Submit', command = updateTodo)


def readTodos():
    with open('todoList.csv', mode='r',newline="\n") as todo:
        csvFile = csv.reader(todo)
        data=list(csvFile)
        for row in data:
            todos.append(row[0])

def generateTodo():
    readTodos()
    rnum = random.randint(0, len(todos)-1)
    dispLabel = Label(root, text="Here's something:")
    todoDisp = Label(root, text = todos[rnum], width=10)
    todoDisp.grid(row=6,column=1)
    dispLabel.grid(row=6,column=0)

gen_btn = Button(root,text = 'What do I do?', command = generateTodo)

def viewUpdate():
    theLabel.grid(row=0,column=1)
    space.grid(row=1,column=2)
    addTodoLabel.grid(row=2,column=0)
    addTodoInput.grid(row=2,column=1)
    space.grid(row=2,column=2)
    sub_btn.grid(row=2,column=3)
    space.grid(row=3,column=2)
    gen_btn.grid(row=4,column=1)

root.after(1000, viewUpdate)

root.mainloop()
