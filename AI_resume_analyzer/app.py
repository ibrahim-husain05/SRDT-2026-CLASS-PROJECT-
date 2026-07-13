import streamlit as st
import tempfile

try:
    from .pdf_reader import PDFReader
    from .preprocess import Preprocessor
    from .analyzer import ResumeAnalyzer
    from .database import Database
except ImportError:
    from pdf_reader import PDFReader
    from preprocess import Preprocessor
    from analyzer import ResumeAnalyzer
    from database import Database

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)

reader = PDFReader()
processor = Preprocessor()
analyzer = ResumeAnalyzer()

jobs = {
    "Software Developer": [
        "Python", "SQL", "Git", "HTML", "CSS",
        "JavaScript", "Flask", "Communication",
        "Problem Solving", "MySQL"
    ],

    "Python Developer": [
        "Python", "Flask", "Django", "SQL",
        "Git", "Linux", "MySQL",
        "REST API", "Problem Solving", "Docker"
    ],

    "Java Developer": [
        "Java", "Spring Boot", "SQL",
        "Git", "MySQL", "REST API",
        "Problem Solving", "Communication",
        "Docker", "Linux"
    ],

    "Frontend Developer": [
        "HTML", "CSS", "JavaScript",
        "React", "Git", "Bootstrap",
        "Communication",
        "Problem Solving"
    ],

    "Backend Developer": [
        "Python", "SQL", "Flask",
        "Django", "MySQL", "Git",
        "REST API", "Docker",
        "Linux", "AWS"
    ],

    "Full Stack Developer": [
        "HTML", "CSS", "JavaScript",
        "React", "Python",
        "Flask", "SQL",
        "Git", "Docker",
        "MySQL"
    ],

    "Data Analyst": [
        "Python", "SQL",
        "Excel", "Power BI",
        "Pandas", "NumPy",
        "Communication",
        "Problem Solving"
    ],

    "Machine Learning Engineer": [
        "Python",
        "Machine Learning",
        "TensorFlow",
        "Pandas",
        "NumPy",
        "SQL",
        "Git",
        "Docker",
        "Linux"
    ],

    "AI Engineer": [
        "Python",
        "Machine Learning",
        "TensorFlow",
        "Pandas",
        "NumPy",
        "Git",
        "Docker",
        "Linux",
        "SQL"
    ],

    "DevOps Engineer": [
        "Linux",
        "Docker",
        "Kubernetes",
        "AWS",
        "Git",
        "Python",
        "SQL"
    ]
}

st.title("🤖 AI Resume Analyzer")
st.write("Upload your resume and get an ATS score.")

uploaded_file = st.file_uploader(
    "Upload Resume",
    type=["pdf"]
)

job_role = st.selectbox(
    "Select Job Role",
    list(jobs.keys())
)

if st.button("Analyze Resume"):

    if uploaded_file is None:
        st.warning("Please upload a resume.")
        st.stop()

    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_file:
        temp_file.write(uploaded_file.read())
        pdf_path = temp_file.name

    text = reader.extract_text(pdf_path)

    clean_text = processor.clean_text(text)

    result = analyzer.analyze_resume(
        clean_text,
        jobs[job_role]
    )

    result["job_role"] = job_role

    st.session_state["result"] = result

if "result" in st.session_state:

    result = st.session_state["result"]

    st.divider()

    st.subheader("📊 Resume Analysis Result")

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "ATS Score",
            f"{result['ats_score']}%"
        )

    with col2:
        st.metric(
            "Resume Rating",
            result["rating"]
        )

    st.divider()

    st.subheader("👤 Candidate Details")

    st.write("*Name:*", result["name"])
    st.write("*Email:*", result["email"])
    st.write("*Phone:*", result["phone"])
    st.write("*Job Role:*", result["job_role"])

    st.divider()

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("✅ Matched Skills")

        if len(result["matched_skills"]) == 0:
            st.info("No matched skills found.")
        else:
            for skill in result["matched_skills"]:
                st.success(skill)

    with col2:

        st.subheader("❌ Missing Skills")

        if len(result["missing_skills"]) == 0:
            st.success("No missing skills")
        else:
            for skill in result["missing_skills"]:
                st.error(skill)

    st.divider()

    st.subheader("💡 Suggestions")

    for suggestion in result["suggestions"]:
        st.write("•", suggestion)

    st.divider()

    if st.button("💾 Save To Database"):
        try:
            db = Database()
            db.save_result(
                result["name"],
                result["email"],
                result["phone"],
                result["job_role"],
                result["ats_score"],
                result["matched_skills"],
                result["missing_skills"],
                result["suggestions"]
            )
            st.success("Resume analysis saved successfully!")
        except Exception as e:
            st.error(f"Database Error: {e}")