import streamlit as st

st.title("Session state examples")
options = ["Button control", "Counter example", "Toggle example", "Link widgets", "Callbacks"]

with st.sidebar:
    page = st.radio("Pick an example", options)

if page == options[0]:
    st.subheader(options[0])
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
elif page == options[1]:
    st.subheader(options[1])
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
    st.subheader(options[2])
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
    st.subheader(options[3])
    with st.echo():
        st.write("work in progress")
elif page == options[4]:
    st.subheader(options[4])
    st.write("""Use a callback function when you need a variable to be updated before your script re-runs.
    This is used when you want a widget to reflect the changes before it is rendered again on the page.""")
    st.write("Using a callback function with a button")
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

        # put the string name of a button in state
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
    st.write("Using a callback function with sliders")
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
        st.slider("Slider 1", min_value = 1,max_value = 10, on_change=slider_one, key="sldr_1")

        # slider 2's value will be half of slider 1's value
        st.slider("Slider 2",min_value=0.5,max_value=5.0,step=0.5, on_change=slider_two, key ="sldr_2")
