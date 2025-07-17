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

# def edit_todo(index):
#     st.session_state["selected_todo_index"] = index
#     st.session_state["todo_input"] = todos[index]

st.title("My Todo App")
st.subheader("This is my todo app")
st.write("This app is to increase your productivity")

remove_indices = []
for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    # if checkbox:
    #     remove_indices.append(index)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

# if remove_indices:
#     for i in sorted(remove_indices, reverse=True):
#         todos.pop(i)
#     functions.write_todos(todos)


# this is capturing todo
# for index, todo in enumerate(todos):
#     if st.checkbox(todo, key=f"{index}-todo"):
#         if st.session_state.get("selected_todo_index") != index:
#             edit_todo(index)
#
st.text_input(label="add", placeholder="Add a new todo", on_change=add_todo,
                     key="new_todo")

# if "todo_input" in st.session_state:
#     st.text_input("Edit Todo", value=st.session_state["todo_input"], key="todo_input_field")

st.session_state