import streamlit as st

st.title("Session state examples")
options = ["Button control", "Counter example", "Toggle example"]

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

        # create teh button that the person presses to run the app
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
