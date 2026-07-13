import re


class ResumeAnalyzer:

    def __init__(self):

        self.all_skills = [
            "Python", "Java", "C", "C++", "SQL",
            "HTML", "CSS", "JavaScript",
            "React", "Node", "Flask", "Django",
            "MySQL", "MongoDB",
            "Git", "GitHub",
            "Linux", "AWS", "Docker",
            "Kubernetes",
            "Machine Learning",
            "TensorFlow",
            "Pandas",
            "NumPy",
            "Power BI",
            "Excel",
            "Communication",
            "Leadership",
            "Teamwork",
            "Problem Solving",
            "Bootstrap",
            "REST API",
            "Spring Boot",
            "Postman",
            "Firebase"
        ]


    def extract_email(self, text):

        match = re.search(
            r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
            text
        )

        return match.group() if match else "Not Found"


    def extract_phone(self, text):

        match = re.search(
            r"(?:\+91[- ]?)?[6-9]\d{9}",
            text
        )

        return match.group() if match else "Not Found"


    def extract_name(self, text):

        lines = text.split()

        if len(lines) >= 2:
            return lines[0].title() + " " + lines[1].title()

        return "Unknown"


    def find_skills(self, text):

        found = []

        text = text.lower()

        for skill in self.all_skills:

            pattern = r"\b" + re.escape(skill.lower()) + r"\b"

            if re.search(pattern, text):

                found.append(skill)

        return sorted(found)


    def compare_skills(self, resume_skills, required_skills):

        matched = []
        missing = []

        for skill in required_skills:

            if skill in resume_skills:
                matched.append(skill)
            else:
                missing.append(skill)

        return matched, missing


    def has_section(self, text, keywords):

        text = text.lower()

        for word in keywords:

            if word.lower() in text:
                return True

        return False


    def calculate_ats_score(
        self,
        text,
        matched_skills,
        required_skills
    ):

        score = 0

        if len(required_skills) > 0:

            score += (
                len(matched_skills) /
                len(required_skills)
            ) * 60

        if self.extract_email(text) != "Not Found":
            score += 5

        if self.extract_phone(text) != "Not Found":
            score += 5

        if self.has_section(
            text,
            ["education"]
        ):
            score += 10

        if self.has_section(
            text,
            ["project", "projects"]
        ):
            score += 10

        if self.has_section(
            text,
            ["experience", "internship"]
        ):
            score += 5

        if self.has_section(
            text,
            ["certificate", "certifications"]
        ):
            score += 5

        return min(round(score), 100)


    def get_resume_rating(self, score):

        if score >= 90:
            return "Excellent"

        if score >= 75:
            return "Very Good"

        if score >= 60:
            return "Good"

        if score >= 40:
            return "Average"

        return "Poor"


    def generate_suggestions(
        self,
        missing_skills,
        text
    ):

        suggestions = []

        for skill in missing_skills:

            suggestions.append(
                f"Add {skill} to your resume if you possess this skill."
            )

        if not self.has_section(
            text,
            ["project", "projects"]
        ):
            suggestions.append(
                "Include at least one project."
            )

        if not self.has_section(
            text,
            ["experience", "internship"]
        ):
            suggestions.append(
                "Mention internships or work experience."
            )

        if not self.has_section(
            text,
            ["certificate", "certifications"]
        ):
            suggestions.append(
                "Add certifications to strengthen your resume."
            )

        if len(missing_skills) == 0:

            suggestions.append(
                "Great! Your resume matches the selected job role."
            )

        return suggestions


    def analyze_resume(
        self,
        text,
        required_skills
    ):

        name = self.extract_name(text)

        email = self.extract_email(text)

        phone = self.extract_phone(text)

        resume_skills = self.find_skills(text)

        matched_skills, missing_skills = self.compare_skills(
            resume_skills,
            required_skills
        )

        ats_score = self.calculate_ats_score(
            text,
            matched_skills,
            required_skills
        )

        rating = self.get_resume_rating(
            ats_score
        )

        suggestions = self.generate_suggestions(
            missing_skills,
            text
        )

        return {

            "name": name,

            "email": email,

            "phone": phone,

            "resume_skills": resume_skills,

            "matched_skills": matched_skills,

            "missing_skills": missing_skills,

            "ats_score": ats_score,

            "rating": rating,

            "suggestions": suggestions

        }
print("Analyzer loaded successfully")
print(hasattr(ResumeAnalyzer, "analyze_resume"))