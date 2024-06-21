import streamlit as st
import os
import pandas as pd
from langchain.chains import RetrievalQA
from langchain.llms import OpenAI
from langchain.vectorstores import Qdrant
from langchain.embeddings.openai import OpenAIEmbeddings
import qdrant_client
from dotenv import load_dotenv

st.set_page_config(page_title="Support - KIIT TNP", page_icon='assets/logo.png', layout='wide')
col1, col2 = st.columns(2)

with col1:
    pages = {
        'Training & Placement Contact': """
            ## Training & Placement Contact
            ---
            ## Training & Placement Help Desk

            - Tel: +916742725733
            - 0674 2725 733

            Present and past students may contact the Help Desk for issues relating to Training & Placement. The Help Desk In-charge will resolve the issues on the spot as far as possible. If the issue deserves detailed attention, he/she will intimate the same and request an E-mail to be sent. Students can send an E-mail to [email protected] directly. Such queries shall be resolved within 48 hours.
            """,
        'West Zone': """
            ## Industry Engagement and Placement Team - West Zone

            - Mr. Pradeep Nambiar
                - Email: pradeep.sreedhar@kiit.ac.in
                - Phone: 9322836323
            """,
        'South Zone': """
            ## Industry Engagement and Placement Team - South Zone

            - Mr. Navendu Kar
                - Email: navendu.kar@kiit.ac.in
                - Phone: 9437072960
            - Mr. Mrutyunjay Ray
                - Email: mrutyunjay.ray@kiit.ac.in
                - Phone: 7682845230
            - Ms. Mahasweta Mohanty
                - Email: mahasweta.mohanty@kiit.ac.in
                - Phone: 9341057074
            - Ms. Anuradha Nayak
                - Email: nayak.anuradha@kiit.ac.in
                - Phone: 9861350515
            """,
        'North Zone': """
            ## Industry Engagement and Placement Team - North Zone

            - Mr. Debraj Mitra
                - Email: debraj.mitra@kiit.ac.in
                - Phone: 6370524489
            - Mr. Manish Verma
                - Email: manish.verma@kiit.ac.in
                - Phone: 8949349670
            """,
        'East Zone': """
            ## Industry Engagement and Placement Team - East Zone

            - Mr. Navendu Kar
                - Email: navendu.kar@kiit.ac.in
                - Phone: 9437072960
            """,
        'Directors': """
            ## Industry Engagement and Placement Team - Directors

            - Dr. Saranjit Singh
                - Email: ssingh@kiit.ac.in
                - Phone: 9437020233
            - Dr. Kumar Mohanty
                - Email: m.kumar@kiit.ac.in
                - Phone: 9937220236
            """,
        'Placement Officers': """
            ## Placement Officers

            - Mr. T P Bakshi
                - Email: t.bakshi@kiit.ac.in
                - Phone: 9238314803
            - Mr. Abhijeet R Sharma
                - Email: kiitcr.nn@kiit.ac.in
                - Phone: 7894427740
            """
    }

    # Create a dropdown menu to select the page or tab
    selected_page = st.sidebar.selectbox('Select a page', list(pages.keys()))

    # Display the selected page content
    st.markdown(pages[selected_page])

    # Create a table for the Industry Engagement and Placement Team
    team_data = {
        'Zone': ['West Zone', 'South Zone', 'South Zone', 'South Zone', 'South Zone', 'North Zone', 'North Zone', 'East Zone', 'Directors', 'Directors'],
        'Name': ['Mr. Pradeep Nambiar', 'Mr. Navendu Kar', 'Mr. Mrutyunjay Ray', 'Ms. Mahasweta Mohanty', 'Ms. Anuradha Nayak', 'Mr. Debraj Mitra', 'Mr. Manish Verma', 'Mr. Navendu Kar', 'Dr. Saranjit Singh', 'Dr. Kumar Mohanty'],
        'Email': ['pradeep.sreedhar@kiit.ac.in', 'navendu.kar@kiit.ac.in', 'mrutyunjay.ray@kiit.ac.in', 'mahasweta.mohanty@kiit.ac.in', 'nayak.anuradha@kiit.ac.in', 'debraj.mitra@kiit.ac.in', 'manish.verma@kiit.ac.in', 'navendu.kar@kiit.ac.in', 'ssingh@kiit.ac.in', 'm.kumar@kiit.ac.in'],
        'Phone': ['9322836323', '9437072960', '7682845230', '9341057074', '9861350515', '6370524489', '8949349670', '9437072960', '9437020233', '9937220236']
    }

    team_df = pd.DataFrame(team_data)

    st.subheader('Industry Engagement and Placement Team')
    st.table(team_df)


with col2:
    st.title("Chat with us")

    load_dotenv()

    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

    def get_vector_store():
        client = qdrant_client.QdrantClient(
            os.getenv("HOST"),
            api_key=os.getenv("API_KEY")
        )
        embeddings = OpenAIEmbeddings()

        vector_store = Qdrant(
            client=client,
            collection_name=os.getenv("COLLECTION_NAME"),
            embeddings=embeddings,
        )
        return vector_store

    qa = RetrievalQA.from_chain_type(
        llm=OpenAI(model="text-davinci-003"),  # Updated model here
        chain_type="stuff",
        retriever=get_vector_store().as_retriever()
    )

    def main():
        load_dotenv()

        vector_store = get_vector_store()

        qa = RetrievalQA.from_chain_type(
            llm=OpenAI(model="text-davinci-003"),  # Updated model here
            chain_type="stuff",
            retriever=vector_store.as_retriever()
        )

        user_question = st.text_input("Ask your doubts")
        if user_question:
            st.write(f"Question: {user_question}")
            answer = qa.run(user_question)
            st.write(f"Answer: {answer}")

            # Store the question and answer in a list
            history = st.session_state.get('history', [])
            history.append((user_question, answer))
            st.session_state['history'] = history

        # Display the history of previous messages in reverse order
        st.subheader("Message History")
        history = st.session_state.get('history', [])
        for question, answer in reversed(history):
            st.write(f"Question: {question}")
            st.write(f"Answer: {answer}")
            st.write("---")

    if __name__ == '__main__':
        main()

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

