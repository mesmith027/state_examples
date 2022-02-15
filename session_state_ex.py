import streamlit as st
import pandas as pd

st.title("Session state examples")
options = ["Button control", "Counter example", "Toggle example", "Link widgets", "Callbacks", "Dataframes"]
# add basics example, with stuff from state video

with st.sidebar:
    page = st.radio("Pick an example", options)

if page == options[0]:
    st.header(options[0])
    st.subheader("Use this to nest widgets after a button press")
    with st.echo():
        # initialize flag that will track if button has been pressed
        if "open" not in st.session_state:
            st.session_state["open"] = False

        # callback function to update the key:value pair in state
        def app_open():
            st.session_state["open"] = True
            return

        # create the button that the person presses to run the app
        st.button("Press me to run the rest of the app", on_click=app_open)

        # the rest of the app runs based on the session state value
        if st.session_state["open"]:
            st.write("The rest of the app runs!")
            if st.checkbox("click me"):
                st.write("🥳🥳🥳🥳🥳🥳🥳")
        
        
    st.write("---")
    st.subheader("Use a button to reset another widgets value")
    st.echo():
        # call back function -> runs BEFORE the rest of the app
        def reset_button():
            st.session_state["p"] = False
        return

        #button to control reset
        reset=st.button('Reset', on_click=reset_button)

        #checkbox you want the button to un-check
        check_box = st.checkbox("p", key='p')

        #write out the current state to see that our flow works
        st.write(st.session_state)
        
elif page == options[1]:
    st.header(options[1])
    with st.echo():
        # add key:value pair to track
        if 'count' not in st.session_state:
            st.session_state.count = 0

        # create a button that will add one to our counter
        add_one = st.button("Add one")

        # if pressed add one to count in state
        if add_one:
            st.session_state.count += 1

        # write current count
        st.write(st.session_state.count)

elif page == options[2]:
    st.header(options[2])
    with st.echo():
        # add key:value pair to track
        if 'toggle' not in st.session_state:
            st.session_state.toggle = False

        # create button that will control the toggle
        toggle = st.button("Change toggle")

        # if pressed update toggle key in state
        if toggle:
            st.session_state.toggle = not st.session_state.toggle

        # check state toggle
        st.write("Current state of toggle:", st.session_state.toggle)

        # use toggle to control output on your app
        if st.session_state.toggle:
            st.write("You opened the app! 🥳🥳🥳")
        else:
            st.write("Open the app by pressing the button above 👆")

elif page == options[3]:
    st.header(options[3])
    st.subheader("To link a widget to a key in session state, simply use the `key` parameter")
    with st.echo():
        # initalize the key in session states
        if "slider" not in st.session_state:
            st.session_state.number = 0
            st.session_state.slider = 0

        # when you create the slider, assign the `key` to be the same
        # as the `key` you initialized already
        st.slider("A slider", key="slider")

        # display the state, "slider" value is is updated each time you change
        # the slider value, but the "link" key does not change
        st.write(st.session_state)
        # linking widgets together

    st.write("""Use this when you want a value in state to _always_ be up to date with the value of a widget""")
    st.write("---")

    st.subheader("To link a widget with another, use callbacks")

elif page == options[4]:
    st.header(options[4])
    st.write("""Use a callback function when you need a variable to be updated before your script re-runs.
    This is used when you want a widget to reflect the changes before it is rendered again on the page.""")
    st.write("Using a callback function with a button:")
    with st.echo():
        # create callback function, this executes BEFORE the script reruns
        def button_pressed():
            if st.session_state.btn_name == "Next":
                # will switch the button to say "Back" and turn page to true
                st.session_state.btn_name = "Back"
                st.session_state.page = True
            else:
                # button will say "next", and set page to False
                st.session_state.btn_name = "Next"
                st.session_state.page = False
            return

        # initialize the button name and page state
        if "btn_name" not in st.session_state:
            st.session_state.btn_name = "Next"
            st.session_state.page = False

        # make a button that's name will change, and will change page value in state
        st.button(st.session_state.btn_name, on_click = button_pressed)

        # depending on what "page" you are on, change what display's to the screen
        if st.session_state.page:
            st.write("You moved to next")
            st.balloons()
        else:
            st.write("Click next to move on")
    st.write("---")
    st.header("Mirror widgets")
    st.write("""Use this when you want the value of one widget to be affected by another.
    This is useful when widgets are interdependant.""")
    with st.echo():
        #define the call back functions
        def slider_one():
            # depending on the value of slider 1, we will change slider 2's value
            st.session_state.sldr_2 = float(st.session_state.sldr_1/2)
            return

        def slider_two():
            # update slider 1's value based on the value for slider 2
            st.session_state.sldr_1 = int(st.session_state.sldr_2*2)
            return

        # slider 1's value will be 2 times slider 2's value, and always be between 1-10
        st.slider("Slider 1", min_value = 1,max_value = 10,
        on_change=slider_one, key="sldr_1")

        # slider 2's value will be half of slider 1's value
        st.slider("Slider 2",min_value=0.5,max_value=5.0,step=0.5,
        on_change=slider_two, key ="sldr_2")

    st.write("---")
    st.subheader("Using number inputs:")
    with st.echo():
        # define call back functions
        def lbs_to_kg():
            # will set kilogram input to convert from pounds
            st.session_state.kg = st.session_state.lbs/2.2046

        def kg_to_lbs():
            # will set pounds to convert from kilograms
            st.session_state.lbs = st.session_state.kg*2.2046

        # set up columns to put the inputs side-by-side
        col1, col2 = st.columns(2)

        with col1:
            # pass lbs_to_kg function on_change parameter, use
            # key to link number_input to session state
            pounds = st.number_input("Pounds:", key="lbs",
                        on_change = lbs_to_kg)

        with col2:
            # pass kg_to_lbs function on_change parameter, use
            # key to link number_input to session state
            kilogram = st.number_input("Kilograms:", key="kg",
                          on_change= kg_to_lbs)

        # print the session state to the app to see the values
        st.write("weight in lbs:",st.session_state.lbs)
        st.write("weight in kg:",st.session_state.kg)

elif page == options[5]:
    st.subheader(options[5])
    with st.echo():
        # initialize list of lists
        data = {'col1': [1, 2, 3, 4], 'col2': [300, 400, 500, 600]}

        # Create the pandas DataFrame
        df = pd.DataFrame(data)

        # print dataframe.
        st.dataframe(df)

        # initalize state with row
        if "row" not in st.session_state:
            st.session_state.row = 0

        def next_row():
            # will move value of row in state to next one
            st.session_state.row += 1
            return

        def prev_row():
            # mill move value of row in state to previous one
            st.session_state.row -= 1
            return

        # create columns to hold the < and > buttons
        col1, col2, _, _ = st.columns([0.1, 0.17, 0.1, 0.63])

        # button that moves forwards
        if st.session_state.row < len(df.index)-1:
            col2.button(">", on_click=next_row)
        else:
            # if at the last row, no next button
            col2.write("")

        # button that moves backwards
        if st.session_state.row > 0:
            col1.button("<", on_click=prev_row)
        else:
            # if at the first row, no back button
            col1.write("")

        # show the current row selected
        st.write(df.iloc[st.session_state.row])
