import streamlit as st

st.set_page_config(page_title="Home < KIIT TNP", page_icon='assets/logo.png', layout='wide')

import streamlit as st

def main():
        st.title("👋 Welcome to KIIT TNP Assist")
        st.write("This is a simple interactive minimalist modern single page home page.")

        st.header("About Me")
        st.write("I am KIIT training and placement bot,I'm here to assist you in navigating the world of professional development and career opportunities. Whether you're a student seeking guidance on internships, a recent graduate looking for job placement, or an experienced professional aiming to enhance your skills, I'm here to provide you with personalized assistance. With my advanced AI capabilities, I can offer valuable insights, recommend relevant training programs, and help you discover the best job opportunities tailored to your unique needs and aspirations. Let's embark on this journey together and unlock your full potential in the professional realm.")

        st.header("Contact")
        st.write("Feel free to reach out to me at 2105789@kiit.ac.in")
    
        st.title("🏫 About KIIT")
        st.write("Kalinga Institute of Industrial Technology (KIIT), a household name in the education sector, has become a sought-after destination in India for professional studies. It is admired all over for the quality of its academic courses, its community outreach work and as a university of compassion and humanitarianism. It has become a case study because no other educational institution in India has grown in its scope and scale as much as KIIT has in a short span of 25 years. Its incredible transformation is truly a journey from Soil to Silver.")

if __name__ == "__main__":
    main()


hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

st.sidebar.success("Select a demo")