import streamlit as st

def main():
    st.title("Dummy App")

    # Add some text
    st.header("This is a header")
    st.write("This is a paragraph of text.")

    # Add a slider widget
    st.sidebar.header("Slider Example")
    slider_value = st.sidebar.slider("Select a value", 0, 100, 50)
    st.write("Slider value:", slider_value)

    # Add a button widget
    if st.button("Click Me"):
        st.write("Button clicked!")

    # Add a selectbox widget
    option = st.selectbox("Choose an option", ["Option 1", "Option 2", "Option 3"])
    st.write("You selected:", option)

    # Add a checkbox widget
    checkbox_state = st.checkbox("Check this box")
    st.write("Checkbox state:", checkbox_state)

    # Add a file uploader widget
    uploaded_file = st.file_uploader("Upload a file")
    if uploaded_file is not None:
        st.write("File uploaded:", uploaded_file.name)

if __name__ == "__main__":
    main()
