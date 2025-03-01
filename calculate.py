import streamlit as st
import math
from datetime import datetime

# Function for the simple calculator
def simple_calculator():
    st.markdown("""
    <style>
        .calculator-frame {
            background-color: #222;
            padding: 6px;
            border-radius: 8px;
            box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.2);
            max-width: 280px;
            margin: auto;
            text-align: center;
            border-top: 4px solid #4CAF50;
            margin-top: 20px;
        }
        .calculator-screen {
            background-color: #fff;
            padding: 4px;
            border-radius: 4px;
            font-size: 12px;
            text-align: right;
            margin-bottom: 4px;
            min-height: 28px;
            border: 2px solid #4CAF50;
            margin-top: 8px;
            display: flex;
            align-items: center;
            justify-content: flex-end;
            width: 100%;
        }
        .calculator-buttons-container {
            border: 2px solid #4CAF50;
            border-radius: 6px;
            margin-top: 10px;
            background-color: #333;
            padding: 0;
        }
        .stButton > button {
            background-color: #4CAF50;
            color: white;
            font-size: 8px;
            padding: 4px;
            margin: 0;
            border-radius: 0;
            border: 1px solid #4CAF50;
            width: 100%;
            height: 30px;
            box-shadow: 1px 1px 2px rgba(0, 0, 0, 0.3);
            transition: all 0.2s ease-in-out;
        }
        .stButton > button:hover {
            background-color: #45a049;
            transform: scale(1.05);
        }
        .stButton > button:active {
            background-color: #3e8e41;
            transform: scale(0.95);
        }
    </style>
    """, unsafe_allow_html=True)
    
    st.title("➗ Simple Calculator")
    
    # Initialize session state for expression
    if "expression" not in st.session_state:
        st.session_state.expression = ""
    
    st.markdown(f"""
    <div class="calculator-frame">
        <div class="calculator-screen">{st.session_state.expression}</div>
        <div class="calculator-buttons-container">
    """, unsafe_allow_html=True)
    
    buttons = [
        ["7", "8", "9", "/"],
        ["4", "5", "6", "*"],
        ["1", "2", "3", "-"],
        ["0", ".", "=", "+"],
        ["C"]
    ]
    
    for row in buttons:
        cols = st.columns(4)  # Keep 4 columns for consistency
        for col, button in zip(cols, row):
            with col:
                if st.button(button, key=f"btn_{button}", use_container_width=True):
                    if button == "C":
                        st.session_state.expression = ""
                    elif button == "=":
                        try:
                            st.session_state.expression = str(eval(st.session_state.expression))
                        except Exception as e:
                            st.session_state.expression = "Error"
                    else:
                        st.session_state.expression += button
    
    st.markdown("""</div></div>""", unsafe_allow_html=True)

# Function for the advanced calculator
def advanced_calculator():
    st.markdown("""
    <style>
        .calculator-frame {
            background-color: #222;
            padding: 6px;
            border-radius: 8px;
            box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.2);
            max-width: 280px;
            margin: auto;
            text-align: center;
            border-top: 4px solid #4CAF50;
            margin-top: 20px;
        }
        .calculator-screen {
            background-color: #fff;
            padding: 4px;
            border-radius: 4px;
            font-size: 12px;
            text-align: right;
            margin-bottom: 4px;
            min-height: 28px;
            border: 2px solid #4CAF50;
            margin-top: 8px;
            display: flex;
            align-items: center;
            justify-content: flex-end;
            width: 100%;
        }
        .calculator-buttons-container {
            border: 2px solid #4CAF50;
            border-radius: 6px;
            margin-top: 10px;
            background-color: #333;
            padding: 0;
        }
        .stButton > button {
            background-color: #4CAF50;
            color: white;
            font-size: 6px;
            padding: 2px;
            margin: 0;
            border-radius: 0;
            border: 1px solid #4CAF50;
            width: 100%;
            height: 20px;
            box-shadow: 1px 1px 2px rgba(0, 0, 0, 0.3);
            transition: all 0.2s ease-in-out;
        }
        .stButton > button:hover {
            background-color: #45a049;
            transform: scale(1.05);
        }
        .stButton > button:active {
            background-color: #3e8e41;
            transform: scale(0.95);
        }
    </style>
    """, unsafe_allow_html=True)
    
    st.title("🔢 Advanced Calculator")
    
    # Initialize session state for expression
    if "expression" not in st.session_state:
        st.session_state.expression = ""
    
    st.markdown(f"""
    <div class="calculator-frame">
        <div class="calculator-screen">{st.session_state.expression}</div>
        <div class="calculator-buttons-container">
    """, unsafe_allow_html=True)
    
    buttons = [
        ["7", "8", "9", "/"],
        ["4", "5", "6", "*"],
        ["1", "2", "3", "-"],
        ["0", ".", "=", "+"],
        ["sqrt", "exp", "^", "C"]
    ]
    
    for row in buttons:
        cols = st.columns(4)  # Keep 4 columns for advanced calculator for consistency
        for col, button in zip(cols, row):
            with col:
                if st.button(button, key=f"btn_{button}", use_container_width=True):
                    if button == "C":
                        st.session_state.expression = ""
                    elif button == "=":
                        try:
                            st.session_state.expression = str(eval(st.session_state.expression))
                        except Exception as e:
                            st.session_state.expression = "Error"
                    elif button == "sqrt":
                        try:
                            st.session_state.expression = str(math.sqrt(float(st.session_state.expression)))
                        except Exception as e:
                            st.session_state.expression = "Error"
                    elif button == "exp":
                        try:
                            st.session_state.expression = str(math.exp(float(st.session_state.expression)))
                        except Exception as e:
                            st.session_state.expression = "Error"
                    elif button == "^":
                        st.session_state.expression += "**"  # Replace ^ with exponentiation operator
                    else:
                        st.session_state.expression += button
    
    st.markdown("""</div></div>""", unsafe_allow_html=True)

# Function for the To-Do List
def todo_list():
    st.title("📝 To-Do List")
    
    # Initialize session state for To-Do List
    if "todos" not in st.session_state:
        st.session_state.todos = []
    
    # Input for new task
    new_task = st.text_input("Add a new task:")
    
    # Add task button
    if st.button("Add Task"):
        if new_task:
            st.session_state.todos.append(new_task)
    
    # Display tasks
    if st.session_state.todos:
        st.write("### Your Tasks:")
        for i, task in enumerate(st.session_state.todos):
            col1, col2 = st.columns([4, 1])
            with col1:
                st.write(f"{i + 1}. {task}")
            with col2:
                if st.button(f"Delete {i + 1}", key=f"delete_{i}"):
                    st.session_state.todos.pop(i)
                    st.rerun()  # Updated to st.rerun()
    else:
        st.write("No tasks added yet.")

# Function for the Calendar
def calendar_page():
    st.title("📅 Calendar")
    
    selected_date = st.date_input("Select a Date", datetime.today())
    st.write(f"Selected Date: {selected_date}")

# Function for Compass
def compass_page():
    st.title("🧭 Compass")
    
    if st.button("Get Direction"):
        directions = ["North", "East", "South", "West"]
        selected_direction = directions[datetime.now().second % 4]  # Randomize direction based on time
        st.write(f"The current direction is: {selected_direction}")
    
    st.write("You can use the button to simulate a direction!")

# Main function
def main():
    st.set_page_config(page_title="Calculator & To-Do List", page_icon="🔢", layout="centered")
    
    # Sidebar navigation
    st.sidebar.title("Navigation")
    app_mode = st.sidebar.radio("Choose an App", ["Simple Calculator", "Advanced Calculator", "To-Do List", "Calendar", "Compass"])

    if app_mode == "Simple Calculator":
        simple_calculator()
    elif app_mode == "Advanced Calculator":
        advanced_calculator()
    elif app_mode == "To-Do List":
        todo_list()
    elif app_mode == "Calendar":
        calendar_page()
    elif app_mode == "Compass":
        compass_page()

if __name__ == "__main__":
    main()
