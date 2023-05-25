import streamlit as st
import functions

todos = functions.get_todos()

st.set_page_config(layout="wide")

def add_todo():
    todo = st.session_state["new_todo"]
    todos.append(todo + '\n')
    functions.write_todos(todos)
    new = st.empty()


st.title("My To-Do app")
st.subheader("This is my to-do app")
st.write("This app is to <b>increase your productivity</b>",
         unsafe_allow_html=True)

st.text_input(label="", placeholder="Add a new todo... ",
              on_change=add_todo, key="new_todo")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()





