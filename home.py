from streamlit_card import card
import streamlit as st


st.set_page_config(
    page_title="Softsquare AI",
    page_icon="🤖",
    layout="wide"
)


hide_st_style = """ <style>
                    #MainMenu {visibility:hidden;}
                    footer {visibility:hidden;}
                    header {visibility:hidden;}
                    </style>"""
st.markdown(hide_st_style, unsafe_allow_html=True)
st.markdown("""
    <h1 id="chat-header" style="position: fixed;
                top: 0;
                left: 0;
                width: 100%;
                text-align: center;
                background-color: #f1f1f1;
                z-index: 9">
        Softsquare's AI Gallery
    </h1>
""", unsafe_allow_html=True)



col1, col2, col3 = st.columns(3)


with col1:
     hasClicked = card(
    key='1',
    title=["AGrid", " ", " "],
    text = "chatbot",
    # text="Are you looking for a faster, more efficient way to manage your data on Salesforce? Look no further than AGrid. Our lightning-fast grids and powerful features streamline workflows, boost productivity, and enhance data quality across your organization. Experience the ultimate Salesforce data management solution with AGrid. Chat with us to explore more about the product.",
    image=f"""https://raw.githubusercontent.com/softsquareadmin/chatbotgallery/main/AGrid%20Logo%203.png""",
    url="https://agridchatbot-vcd4ehhmbkb5x54enrsrbi.streamlit.app/",
    styles={
        "card": {
            # "width": "400px",
            # "height": "500px",
            # "width": "auto",
            # "height":"auto",
            "border-radius": "20px",
            "box-shadow": "0 0 10px rgba(17, 95, 250, 0.88)",
            
        }
    }
)

with col2:
    hasClicked = card(
    key='2',
    title=["User 360"],
    text = "chatbot",
    # text="Are you seeking an efficient solution for user management within Salesforce? Look no further than User360. Our platform offers robust features to streamline workflows, enhance productivity, and elevate data quality across your organization. User360 automates user management tasks, ensuring a seamless and efficient user experience. Chat with us to explore more about the product.",
    image=f"""https://raw.githubusercontent.com/softsquareadmin/chatbotgallery/main/User360.png""",
    url="https://user360bot-4pxrknjb8zo2fxgz2hafug.streamlit.app/",
    styles={
        "card": {
            # "width": "400px",
            # "height": "500px",
            "border-radius": "20px",
            "box-shadow": "0 0 10px rgba(17, 95, 250, 0.88)",
            
        }
    }
)
   
with col3:
    hasClicked = card(
    key='3',
    title=["Media Manager"],
    text = "chatbot",
    # text="Media Manager, designed for the Lightning Experience, simplifies file management within Salesforce records. With built-in viewer modes, file controls, and powerful search capabilities, it enhances productivity and customization to meet your business needs. Chat with us to explore more about the product.",
    image="https://raw.githubusercontent.com/softsquareadmin/chatbotgallery/main/Media%20Manager%203.png",
    url="",
    styles={
        "card": {
            # "width": "400px",
            # "height": "500px",
            "border-radius": "20px",
            "box-shadow": "0 0 10px rgba(17, 95, 250, 0.88)", 
                       
        },
        # "filter": {
        #     "background-color": "rgba(255, 255, 255, 255)" 
            
        # }
    }
)

col11, col21, col31 = st.columns(3)

with col11:
    hasClicked = card(
    key='21',
    title=["App Analytics"],
    text = "Dashboard",
    # text="Media Manager, designed for the Lightning Experience, simplifies file management within Salesforce records. With built-in viewer modes, file controls, and powerful search capabilities, it enhances productivity and customization to meet your business needs. Chat with us to explore more about the product.",
    image="https://raw.githubusercontent.com/softsquareadmin/chatbotgallery/main/analytics-icon.png",
    url="https://devappanalystics-eve9yjazayqvexttmutt2h.streamlit.app/",
    styles={
        "card": {
            # "width": "400px",
            # "height": "500px",
            "border-radius": "20px",
            "box-shadow": "0 0 10px rgba(17, 95, 250, 0.88)", 
                       
        },
        # "filter": {
        #     "background-color": "rgba(255, 255, 255, 255)" 
            
        # }
    }
)
