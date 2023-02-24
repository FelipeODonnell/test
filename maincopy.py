
import streamlit

with streamlit.sidebar: 
    streamlit.image("https://www.onepointltd.com/wp-content/uploads/2020/03/inno2.png")
    streamlit.title("Blueblocks.ai")
    choice = streamlit.radio("Navigation", ["Valuation","Structuring","Swaps"])
    streamlit.info("This project application helps you get instant valuations and structures solutions for your property")

if choice == "Valuation":
    pass



if choice == "Structuring": 
    pass

if choice == "Swaps": 
    pass
