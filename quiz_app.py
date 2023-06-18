import streamlit as st
import pandas as pd
from datetime import datetime
import time
import os.path

# Set the title of the quiz
st.markdown("<h1 style='text-align: center;'>Quiz Mil</h1>", unsafe_allow_html=True)
st.markdown("---")

# Ask user for their name
name = st.text_input("Enter your name:")
st.markdown("---")

# Check if a valid name is entered
if name:
    # Define the quiz questions and answer options
    questions = [
    {
        "question": "Pertains to the output of a person's intellectual pursuit such as literary and artistic works, inventions, logos, symbols, and signs, as well as names and images used for commercial purpose or advertisements.",
        "options": ["Intellectual Property", "Copyright","None of the above"],
        "correct_answer": "Intellectual Property"
    },
    {
        "question": "What is the set of rights granted to the author or creator of a work, to restrict others' ability to copy, redistribute, and reshape the content?",
        "options": ["Plagiarism", "Copyright","None of the above"],
        "correct_answer": "Copyright"
    },
    {
        "question": "It is the use or production of copyright-protected material without the permission of the copyright holder.",
        "options": ["Copyright Infringement", "Copyright","None of the above"],
        "correct_answer": "Copyright Infringement"
    },
    {
        "question": "An exclusive right granted to an invention.",
        "options": ["Trademark", "Patent","None of the above"],
        "correct_answer": "Patent"
    },
    {
        "question": "It is the act of engaging in a prohibited act with respect to a patented invention without permission from the patent holder.",
        "options": ["Patent", "Patent Infringement","None of the above"],
        "correct_answer": "Patent Infringement"
    },
    {
        "question": "A specific sign associated with a particular brand of goods or services.",
        "options": ["Patent", "Trademark","None of the above"],
        "correct_answer": "Trademark"
    },
    {
        "question": "It is the unauthorized use of a trademark or service mark on or in connection with goods and/or services in a manner that is likely to cause confusion, deception, or mistake about the source of the goods and/or services.",
        "options": ["Trademark", "Trademark Infringement","None of the above"],
        "correct_answer": "Trademark Infringement"
    },
    {
        "question": "What term refers to the copying of a copyrighted material, with the purpose of using it for a review, commentary, critic, or parody, without the need to ask permission from the copyright owner?",
        "options": ["Copyright", "Fair Use","None of the above"],
        "correct_answer": "Fair Use"
    },
    {
        "question": "Using someone else's work without giving proper credit, such as failing to cite adequately, using someone else's creative work without authorization or compensation, if compensation is appropriate.",
        "options": ["Copyright", "Plagiarism","None of the above"],
        "correct_answer": "Plagiarism"
    },
    {
        "question": "What term means the use of good manners in online communication, such as e-mail, forums, blogs, and social networking sites?",
        "options": ["Netiquette", "Internet","None of the above"],
        "correct_answer": "Netiquette"
    }
]


    # Initialize variables for tracking user's answers and score
    user_answers = {}
    score = 0

    # Display each question and its options
    for i, question in enumerate(questions):
        st.subheader(f"Question {i+1}:")
        st.write(question["question"])

        # Create an empty placeholder
        options_placeholder = st.empty()
        
        # Display answer options as radio buttons
        selected_option = options_placeholder.radio("Select your answer:", options=question["options"], index=2, key=f"question_{i}")


        # Check if user's answer is not "None of the above"
        if selected_option != "None of the above":
            options_placeholder.write("")
            # Check if user's answer is correct and update the score
            # Store user's selected answer
            user_answers[i] = selected_option
            if selected_option == question["correct_answer"]:
                score += 10
                st.markdown(f'<div style="background-color: green; color: white; padding: 10px;">{selected_option} ✅</div>', unsafe_allow_html=True)  # Display green tick mark for correct answer
            else:
                st.markdown(f'<div style="background-color: red; color: white; padding: 10px;">{selected_option} ❌</div>', unsafe_allow_html=True)  # Display red cross mark for incorrect answer

            # Display correct answer below the question
            st.markdown(f'<div style="background-color: yellow; color: black; padding: 10px;">Correct answer : {question["correct_answer"]}</div>', unsafe_allow_html=True)  # Display red cross mark for incorrect answer            

        st.markdown("---")

    # Create an button empty placeholder
    button_placeholder = st.empty()
    
    # Check score button
    if len(user_answers) == len(questions):
        if button_placeholder.button("Check Score"):
            # Calculate percentage score
            percentage_score = (score / (len(questions) * 10)) * 100

            # Display the score with animation
            with st.spinner("Calculating score..."):
                time.sleep(3)
                st.balloons()
                st.success(f"Congratulations Your score: {score} % ")

            # Store progress report in Excel
            file_exists = os.path.isfile("progress_reports.xlsx")
            df = pd.DataFrame({
                "Name": [name],
                "Score": [score],
                "Timestamp": [datetime.now()]
            })
            if file_exists:
                existing_df = pd.read_excel("progress_reports.xlsx")
                updated_df = existing_df.append(df, ignore_index=True)
                updated_df.to_excel("progress_reports.xlsx", index=False, header=True)
            else:
                df.to_excel("progress_reports.xlsx", index=False, header=True)
           
            button_placeholder.write("Thank You for the participation. Refresh to try again")