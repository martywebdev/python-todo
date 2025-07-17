import streamlit as st
import  functions

todos = functions.get_todos()

def add_todo():
    try:
        todo = st.session_state["new_todo"]
        if (todo + "\n") in todos:
            st.warning("This todo already exists!")
            return
        todos.append(todo + "\n")
        functions.write_todos(todos)
        st.session_state["new_todo"] = ""
    except Exception as e:
        print(e)


st.title("My Todo App")
st.subheader("This is my todo app")
st.write("This app is to increase your productivity")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="add", placeholder="Add a new todo", on_change=add_todo,
                     key="new_todo")

# st.session_state