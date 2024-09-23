import streamlit as st
import plotly.express as px
import matplotlib.pyplot as plt
import numpy as np

# App title and header
st.set_page_config(page_title="AI Smart Study Assistant", layout="wide")
st.title("📚 AI Smart Study Assistant")
st.subheader("Personalized Learning Journey to Help You Succeed")

# Sidebar for user navigation
st.sidebar.header("Navigation")
menu = ["Home", "Create Study Plan", "Take a Quiz", "Track Progress", "Study Resources"]
selection = st.sidebar.radio("Go to", menu)

# Sample Data for Demo
subject_list = ['Math', 'Science', 'History', 'Literature']
study_plan_status = {"Math": 80, "Science": 50, "History": 30, "Literature": 60}
past_scores = {'Math': [80, 85, 78, 90], 'Science': [55, 60, 70, 65], 'History': [30, 40, 50, 55], 'Literature': [60, 70, 80, 85]}
quiz_questions = {
    "Math": ["2 + 2 = ?", "5 x 6 = ?", "10 ÷ 2 = ?"],
    "Science": ["Water is H2O. (True/False)", "The Earth is flat. (True/False)"],
    "History": ["Who discovered America?", "When was the French Revolution?"],
    "Literature": ["Who wrote 'Romeo and Juliet'?", "Name one work by George Orwell."]
}

# Home Page
if selection == "Home":
    st.markdown("""
    Welcome to your personalized **AI Smart Study Assistant**. This assistant helps you with:
    
    - Customizable Study Plans tailored to your learning style.
    - Quizzes to test your knowledge in various subjects.
    - Progress tracking with detailed visual reports.
    - A wide range of study resources, including videos, articles, and notes.
    
    Let's start by setting your study goals, testing your knowledge, or tracking your progress!
    """)

# Create Study Plan Page
elif selection == "Create Study Plan":
    st.header("📅 Create Your Personalized Study Plan")
    
    with st.form("study_plan_form"):
        name = st.text_input("Enter Your Name")
        st.write("Select Subjects to Focus On:")
        selected_subjects = st.multiselect("Choose Subjects", subject_list)
        study_hours = st.slider("How many hours per day will you dedicate to study?", 1, 10, 2)
        study_goal = st.text_area("Set a Study Goal (e.g., Complete Algebra in 2 weeks)")
        
        # Submit form
        if st.form_submit_button("Create Plan"):
            st.success(f"Study plan created for {name}. Focus on {selected_subjects} for {study_hours} hours/day. Goal: {study_goal}.")
            
# Take a Quiz Page
elif selection == "Take a Quiz":
    st.header("📝 Take a Quiz")

    subject = st.selectbox("Choose a Subject to Test", subject_list)
    
    st.write(f"### {subject} Quiz")
    
    if subject in quiz_questions:
        score = 0
        for q in quiz_questions[subject]:
            answer = st.radio(q, options=['Option 1', 'Option 2', 'Option 3', 'Option 4'])
            score += 1  # Placeholder for scoring
        st.write(f"Your score: {score}/{len(quiz_questions[subject])}")
    else:
        st.warning("No quiz available for the selected subject.")

# Track Progress Page
elif selection == "Track Progress":
    st.header("📊 Track Your Learning Progress")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.write("### Subject-Wise Progress")
        
        # Plot progress using Plotly
        subjects = list(study_plan_status.keys())
        progress = list(study_plan_status.values())
        
        fig = px.bar(x=subjects, y=progress, labels={'x': "Subjects", 'y': "Progress (%)"}, color=progress, title="Your Study Progress")
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        st.write("### Recent Scores")
        
        # Plot past performance using Matplotlib
        st.write("Math Performance")
        fig, ax = plt.subplots()
        ax.plot(past_scores['Math'], label="Math", marker='o')
        ax.set_title("Math Progress Over Time")
        ax.set_xlabel("Test Attempts")
        ax.set_ylabel("Scores")
        st.pyplot(fig)
        
        # Add more plots for other subjects as necessary
        
# Study Resources Page
elif selection == "Study Resources":
    st.header("📚 Study Resources")
    
    st.write("""
    Here are some recommended resources based on your current study plan:
    
    - **Math**: [Khan Academy Math Lessons](https://www.khanacademy.org)
    - **Science**: [CrashCourse YouTube Channel](https://www.youtube.com/user/crashcourse)
    - **History**: [History.com Articles](https://www.history.com)
    - **Literature**: [SparkNotes Literature Guides](https://www.sparknotes.com)
    
    Keep exploring these resources to enhance your learning experience!
    """)

# Footer
st.markdown("""
---
© 2024 Smart Study Assistant | All rights reserved.
""")
