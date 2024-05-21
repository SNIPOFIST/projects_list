import streamlit as st



#Mention the Projects in list and add a good UI to it 
# have a description about the project in click of a button 
# add the socials in the footer 
# add the side bar menu that has the list of options and have a anchor tag to it 
# add the link for the websites 
# the heading of the project name should be bold and simple 
# add a photo of yours and add a personal identification to prove that the website is yours

# Set the page configuration
st.set_page_config(
    page_title = "Projects_Hari_Ram",
    page_icon=":📑:",
    layout='wide')
#----------------------------------------------#
# A dd a title for the page
col_1, col_2, col_3 = st.columns(3)
with col_1:
    st.title(":orange[List of Projects]")

with col_2:
    pass 


with col_3:
    st.write("")
    st.header(" _:orange[My Portfolio]_")
    st.markdown('[Click me](https://hariram-portfolio.streamlit.app/) ',unsafe_allow_html = True) 
    st.subheader("_:orange[Certifications]_")
    st.markdown('[Click me](https://hariramcertifications.streamlit.app/) ',unsafe_allow_html = True) 
    
        

    

nebula = 'https://cdn.pixabay.com/photo/2023/01/10/10/47/space-7709489_1280.jpg'

pg_bg =  """
<style>
[data-testid="stAppViewContainer"]{
background-image: url('https://cdn.pixabay.com/photo/2016/04/23/18/45/planet-1348079_1280.jpg');
background-size: cover;
}
</style>"""

style = '''
'''

st.markdown(pg_bg,unsafe_allow_html=True)


#----------------------------------------------#
st.write("")
st.write("")
st.write("")

st.header("1. NLP - Text to Speech ")
with st.expander("About project"):
    st.caption(":orange[Interactive Text-to-Speech web app using Python and Streamlit. This project leverages the Google Text-to-Speech (GTTS) module to convert user input into real-time audio speech output, delivering an engaging user experience. The user after entering thre text can convert the speech to an audio file and download it for thier own purpose.]")
st.subheader("Link : https://nlp-text-to-speech.streamlit.app/ ")
st.write("------------------------------------------------------------------")

st.header("2.Weather forecast using python")
with st.expander("Project Description"):
    st.caption(":orange[Developed a real-time weather forecasting web app using Streamlit and OpenWeatherMap API. Users input location (state, country, or region), and the app retrieves and displays weather data (fetched via API key) using charts and visualizations.]")
    
st.subheader("Link : https://howstheweatherlike.streamlit.app/")
st.caption("")
st.write("------------------------------------------------------------------")

#----------------------------------------------#

st.header("3.Stock analysis ")
with st.expander("About project"):
    st.caption(":orange[Developed a real-time weather forecasting web app using Streamlit and OpenWeatherMap API. Users input location (state, country, or region), and the app retrieves and displays weather data (fetched via API key) using charts and visualizations.]")
st.subheader("Link : https://stocksinfo.streamlit.app/")
st.caption("")
st.write("------------------------------------------------------------------")
#----------------------------------------------#

st.header("4. Metal Band: Vortex, Portfolio")
with st.expander("About project"):
    st.caption(":orange[An interactive portfolio website using Streamlit, HTML, and CSS to showcase a local rock band VORTEX. The website features band member information, photos, and potentially music samples via gallery view in google drive, offering a dynamic online presence.]")
st.subheader("Link : https://vortex.streamlit.app/")
st.caption("")
st.write("------------------------------------------------------------------")
#----------------------------------------------#

#----------------------------------------------#

st.header("5. Portfolio website ")
with st.expander("About project"):
    st.caption(":orange[Constructed a dynamic personal portfolio website for myself using Streamlit, HTML, and CSS. This interactive platform showcases my academic and professional journey, including social links, contact information, and certification credentials.]")
st.subheader("Link : https://hariram-portfolio.streamlit.app/")
st.caption("")
st.divider()
#----------------------------------------------#
#----------------------------------------------#

# seperate the UI for each project and add a button with description in it 
#----------------------------------------------#




















#----------------------------------------------#
# The footer section 
st.write("")
st.write("")
st.write("")
st.divider()
st.subheader("Let's Connect !!!")
st.write("")
st.write("")
st.write("")
footer_col1 , footer_col2, footer_col3 , footer_col4 = st.columns(4)
with footer_col1:
    st.markdown('[<img src="https://imgs.search.brave.com/TQTym5qzpizZ5GHIgpHu6-RTEchhOps_4v-FWSI8ZIE/rs:fit:32:32:1/g:ce/aHR0cDovL2Zhdmlj/b25zLnNlYXJjaC5i/cmF2ZS5jb20vaWNv/bnMvNGE1YzZjOWNj/NmNiODQ4NzI0ODg1/MGY5ZGQ2YzhjZTRm/N2NjOGIzZjc1NTlj/NDM2ZGI5Yjk3ZWI1/YzBmNzJmZS93d3cu/bGlua2VkaW4uY29t/Lw" height=30 width=30> </img> <b> Hari Ram S <b>]("https://www.linkedin.com/in/hari-ram-s-342a7621b/")', unsafe_allow_html=True)
with footer_col2:
    st.markdown('[✉️ HariramSelvaraj@yahoo.com](mailto:HariramSelvaraj@yahoo.com)',unsafe_allow_html = True) 
with footer_col3:
    st.markdown('[<img src="https://static.xx.fbcdn.net/rsrc.php/v3/yx/r/tBxa1IFcTQH.png" height=30 width=30> </img><b>hari____7<b>](https://www.instagram.com/hari____7/) ',unsafe_allow_html = True) 



st.divider()
