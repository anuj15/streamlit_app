import streamlit as st

from common_functions import read_file, write_file


todo_list = read_file()


def add_item():
    new_item = st.session_state.input + '\n'
    if new_item.strip() != '':
        todo_list.append(new_item)
        write_file(todo_list)
        st.session_state.input = ''


def remove_item():
    for item in todo_list:
        if st.session_state[item]:
            todo_list.remove(item)
            write_file(todo_list)
            del st.session_state[item]

TITLE = 'To Do App'
st.write(f'<h1 style=text-align:center>{TITLE}</h1><hr>', unsafe_allow_html=True)
st.write('Enter a task in text field to create a To-Do. Click the checkbox to mark the task as completed.')

for i in todo_list:
    st.checkbox(label=i, value=False, on_change=remove_item, key=i)

st.text_input(label='Add To-Do', placeholder='Add new todo', key='input', on_change=add_item, label_visibility='hidden')
