import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()


class Database:

    def __init__(self):
        self._connection = None
        self._cursor = None

    @property
    def connection(self):
        if self._connection is None:
            self._ensure_connection()
        return self._connection

    @property
    def cursor(self):
        if self._cursor is None:
            self._ensure_connection()
        return self._cursor

    def _connect(self):
        if self._connection is not None and self._cursor is not None:
            return

        self._connection = mysql.connector.connect(
            host=os.getenv("DB_HOST", "localhost"),
            user=os.getenv("DB_USER", "root"),
            password=os.getenv("DB_PASSWORD", "12345"),
            database=os.getenv("DB_NAME", "resume")
        )
        self._cursor = self._connection.cursor(buffered=True)

    def _ensure_connection(self):
        if self._connection is None:
            self._connect()
        if self._cursor is None:
            self._cursor = self._connection.cursor(buffered=True)
        return self._connection, self._cursor

    def save_result(
        self,
        name,
        email,
        phone,
        job_role,
        ats_score,
        matched_skills,
        missing_skills,
        suggestions
    ):

        query = """
        INSERT INTO resume_analysis
        (
            name,
            email,
            phone,
            job_role,
            ats_score,
            matched_skills,
            missing_skills,
            suggestions
        )
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
        """

        values = (
            name,
            email,
            phone,
            job_role,
            ats_score,
            ", ".join(matched_skills),
            ", ".join(missing_skills),
            "\n".join(suggestions)
        )

        self._ensure_connection()
        self.cursor.execute(query, values)
        self.connection.commit()

    def get_all_results(self):

        self._ensure_connection()
        self.cursor.execute(
            "SELECT * FROM resume_analysis ORDER BY id DESC"
        )

        return self.cursor.fetchall()

    def search_candidate(self, name):

        self._ensure_connection()
        self.cursor.execute(
            "SELECT * FROM resume_analysis WHERE name LIKE %s",
            ("%" + name + "%",)
        )

        return self.cursor.fetchall()

    def delete_result(self, candidate_id):

        self._ensure_connection()
        self.cursor.execute(
            "DELETE FROM resume_analysis WHERE id=%s",
            (candidate_id,)
        )

        self.connection.commit()

    def close(self):

        if self._cursor is not None:
            self._cursor.close()

        if self._connection is not None:
            self._connection.close()

        self._cursor = None
        self._connection = None