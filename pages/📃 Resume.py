import streamlit as st
from fpdf import FPDF
import base64

# Define a class to create a PDF
class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)

    def chapter_title(self, title):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, title, 0, 1, 'L')
        self.ln(5)

    def chapter_body(self, body):
        self.set_font('Arial', '', 12)
        self.multi_cell(0, 10, body)
        self.ln()

    def add_info(self, title, body):
        if body:  # Only add to PDF if body is not empty
            self.chapter_title(title)
            self.chapter_body(body)

# Function to create a download link
def get_binary_file_downloader_html(bin_file, file_label='File'):
    with open(bin_file, 'rb') as f:
        data = f.read()
    bin_str = base64.b64encode(data).decode()
    href = f'<a href="data:application/octet-stream;base64,{bin_str}" download="{bin_file}">{file_label}</a>'
    return href

# Streamlit app
def app():
    st.set_page_config(page_title="Resume Creator < KIIT TNP", page_icon='assets/logo.png', layout='wide')
    pdf = PDF()
    pdf.add_page()

    st.title('Resume Creator')

    name = st.text_input('Name')
    about = st.text_input('About')
    email = st.text_input('Email')
    phone = st.text_input('Phone')
    linkedin = st.text_input('Linkedin')
    github = st.text_input('GitHub / Portfolio')

    pdf.add_info('Name', name)
    pdf.add_info('About', about)
    pdf.add_info('Email', email)
    pdf.add_info('Phone', phone)
    pdf.add_info('Linkedin', linkedin)
    pdf.add_info('GitHub / Portfolio', github)
    col1, col2, col3 = st.columns(3)

    with col1:
        education_entries = st.number_input('Number of Education Entries', min_value=1, value=1, step=1)
        for i in range(education_entries):
            st.subheader(f'Education Entry {i+1}')
            institution_name = st.text_input(f'Institution Name {i+1}')
            course = st.text_input(f'Course {i+1}')
            year_of_enrollment = st.text_input(f'Year of Enrollment {i+1}')
            year_of_passing = st.text_input(f'Year of Passing {i+1}')

            if institution_name and course and year_of_enrollment and year_of_passing:
                if i==0:
                    pdf.add_info('Education', f'{institution_name}, {course}, {year_of_enrollment}-{year_of_passing}')
                else:
                    pdf.add_info('', f'{institution_name}, {course}, {year_of_enrollment}-{year_of_passing}')

    with col2:
        experience_entries = st.number_input('Number of Experience Entries', min_value=1, value=1, step=1)
        for i in range(experience_entries):
            st.subheader(f'Experience Entry {i+1}')
            company_name = st.text_input(f'Company Name {i+1}')
            position = st.text_input(f'Position {i+1}')
            year_of_joining = st.text_input(f'Year of Joining {i+1}')
            year_of_leaving = st.text_input(f'Year of Leaving {i+1}')

            if company_name and position and year_of_joining and year_of_leaving:
                if i==0:
                    pdf.add_info('Experience', f'{company_name}, {position}, {year_of_joining}-{year_of_leaving}')
                else:
                    pdf.add_info('', f'{company_name}, {position}, {year_of_joining}-{year_of_leaving}')

    with col3:
        certficate_entries = st.number_input('Number of Certificate Entries', min_value=1, value=1, step=1)
        for i in range(certficate_entries):
            st.subheader(f'Certificate Entry {i+1}')
            issuer_name = st.text_input(f'Issuer Name {i+1}')
            certficate_nunmber = st.text_input(f'ID {i+1}')
            year_of_issue = st.text_input(f'Year of Issuing {i+1}')

            if issuer_name and certficate_nunmber and year_of_issue:
                if i==0:
                    pdf.add_info('Certificate', f'{issuer_name}, {certficate_nunmber}, {year_of_issue}')
                else:
                    pdf.add_info('', f'{issuer_name}, {certficate_nunmber}, {year_of_issue}')

    skills = st.text_area('Skills (separated by commas)')
    pdf.add_info('Skills', skills)

    awards_entries = st.number_input('Number of Awards', min_value=1, value=1, step=1)
    for i in range(awards_entries):
        st.subheader(f'Award {i+1}')
        award_title = st.text_input(f'Award Title {i+1}')
        year_of_receiving = st.text_input(f'Year of Receiving {i+1}')
        organization = st.text_input(f'Organization {i+1}')

        if award_title and year_of_receiving and organization:
            if i==0:
                pdf.add_info('Awards', f'{award_title}, {year_of_receiving}, {organization}')
            else:
                pdf.add_info('', f'{award_title}, {year_of_receiving}, {organization}')

        if st.button('Generate PDF'):
            pdf.output('Resume.pdf', 'F')
            with open('Resume.pdf', 'rb') as f:
                pdf_data = f.read()
            b64_pdf = base64.b64encode(pdf_data).decode('utf-8')
            href = f'<a href="data:application/octet-stream;base64,{b64_pdf}" download="Resume.pdf" style="background-color: #4CAF50; color: white; padding: 10px 20px; text-decoration: none; border-radius: 4px;">Download Resume</a>'
            st.markdown(href, unsafe_allow_html=True)

if __name__ == '__main__':
    app()

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)