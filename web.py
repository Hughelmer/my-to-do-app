import streamlit as ST
import functions

todos = functions.get_todos()

def add_todo():
    todo = ST.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)


ST.title("My Todo App")
ST.subheader("This is my todo app.")
ST.write("This app is to increase your productivity.")


for index, todo in enumerate(todos):
    checkbox = ST.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del ST.session_state[todo]
        ST.experimental_rerun()

ST.text_input(label="", placeholder="Add new todo...",
              on_change=add_todo, key='new_todo')