from streamlit_card import card
import streamlit as st

st.set_page_config(
    page_title="Softsquare AI",
    page_icon="🤖",
    layout="wide"
)

# with open("style.css", "r") as f:
#     st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


hide_st_style = """ 
    <style>
        #MainMenu {visibility:hidden;}
       footer {visibility:hidden;}
        header {visibility:hidden;}
        
    </style>
"""
st.markdown(hide_st_style, unsafe_allow_html=True)


st.markdown("""
            
    
    <div style="position: fixed; top: 10px; left: 10px; padding: 10px;">
    <img src="https://www.softsquare.biz/wp-content/uploads/2021/09/Softsquare-logo-v2.png" 
         alt="Logo" style="height: 38px; width: auto;">
</div>
    <h1 id="chat-header" style="position: relative;
                top: 150;
                left: 0;
                width: 100%;
                text-align: center;
                color: black;
                "
                           >
        Softsquare's AI Chatbot: Your Expert Product Guide!
    </h1>
        <br>   
    <h5 id="chat-header1" style="position: relative;
                top: 1;
                left: 0;
                width: 100%;
                text-align: center;
                color: black;
                z-index: 9">
        Get personalized support from our AI assistant for everything from configuration and feature insights to 
            <br>troubleshooting,ensuring a seamless experience
    </h5>
            <br>
""", unsafe_allow_html=True)

st.markdown("""
    <div style="position: absolute; background-color: #FFCCCB; padding: 50px;padding-bottom:30px; height: 90vh; width: 112%; margin-left: -6%; box-sizing: border-box;">
            
       <h2 style="text-align: center; color: #333; margin-top: -30px;font-size:27px">Our Products</h2>
    </div>
""", unsafe_allow_html=True)


st.markdown("""
    <style>
        .stColumns {
            margin-bottom: 50vh ;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
    <style>
        .st-emotion-cache-13k62yr {
            background-color : white ;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
    <style>
        .box {
            display: flex;
            align-items: left;
            padding: 20px;
            margin: 20px;
            background-color: white;
            border-radius: 15px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            transition: transform 0.2s;
            text-decoration: none;
        }
        .box:hover {
            transform: scale(1.05);
            text-decoration: none;
        }
        .box img {
            max-width: 80px;
            margin-right: 20px;
            display: block;
        }
        .box-text {
            font-size: 18px;
            color: #333;
            text-decoration: none;
            text-align: left; /* Align text to the left */
        }
        .box-text h4, .box-text p {
            margin: 0;
            padding: 0;
            text-decoration: none;
        }
      
    </style>
""", unsafe_allow_html=True)


col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
        <a href="https://agridchatbot-vcd4ehhmbkb5x54enrsrbi.streamlit.app/" target="_blank" class="box">
            <div style="display: flex; align-items: center;">
                <img src="https://raw.githubusercontent.com/softsquareadmin/chatbotgallery/main/AGrid%20Logo%203.png" alt="AGrid Logo">
                <div class="box-text">
                    <h4>AGrid</h4>
                    <p id="txtp" >One-stop solution for managing and visualizing Salesforce data effortlessly.</p>
                </div>
            </div>
        </a>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
        <a href="https://user360bot-4pxrknjb8zo2fxgz2hafug.streamlit.app/" target="_blank" class="box">
            <div style="display: flex; align-items: center;">
                <img src="https://raw.githubusercontent.com/softsquareadmin/chatbotgallery/main/User360.png" alt="User 360 Logo">
                <div class="box-text">
                    <h4>User 360</h4>
                    <p>Comprehensive user management and optimization for Salesforce environments.</p>
                </div>
            </div>
        </a>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
        <a href="https://mediamanagerchatbot-abzbrpflvgqnpd7ak9tcdr.streamlit.app/" target="_blank" class="box">
            <div style="display: flex; align-items: center;">
                <img src="https://raw.githubusercontent.com/softsquareadmin/chatbotgallery/main/Media%20Manager%203.png" alt="Media Manager Logo">
                <div class="box-text">
                    <h4>Media Manager</h4>
                    <p>Streamline and mange yourmedia assets within Salesforce.</p>
                </div>
            </div>
        </a>
    """, unsafe_allow_html=True)

col11, col21, col31 = st.columns(3)

with col21:
    st.markdown("""
        <a href="https://devappanalystics-eve9yjazayqvexttmutt2h.streamlit.app/" target="_blank" class="box">
            <div style="display: flex; align-items: center;">
                <img src="https://raw.githubusercontent.com/softsquareadmin/chatbotgallery/main/ISVAppAnalytics.png" alt="App Analytics Logo">
                <div class="box-text">
                    <h4>ISV App Analytics</h4>
                    <p>Powerful insights into app performance and user behavior.</p>
                </div>
            </div>
        </a>
    """, unsafe_allow_html=True)


st.markdown("</div></div>", unsafe_allow_html=True)