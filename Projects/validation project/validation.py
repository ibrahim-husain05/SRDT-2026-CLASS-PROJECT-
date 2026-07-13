import re


class Validation:
    def is_empty(self, value: str) -> bool:
        return bool(value and value.strip())

    def validate_name(self, name: str) -> bool:
        return bool(name and re.fullmatch(r"[A-Za-z ]{2,50}", name.strip()))

    def validate_email(self, email: str) -> bool:
        return bool(email and re.fullmatch(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", email.strip()))

    def validate_mobile(self, mobile: str) -> bool:
        mobile = mobile.strip()
        return bool(re.fullmatch(r"\d{10,15}", mobile))

    def validate_username(self, username: str) -> bool:
        return bool(username and re.fullmatch(r"[A-Za-z0-9_]{3,30}", username.strip()))

    def validate_password(self, password: str) -> bool:
        if not password or len(password) < 8:
            return False
        if not re.search(r"[A-Z]", password):
            return False
        if not re.search(r"[a-z]", password):
            return False
        if not re.search(r"\d", password):
            return False
        if not re.search(r"[!@#$%^&*()_+\-=[\]{};':\"\\|,.<>/?]", password):
            return False
        return True

    def confirm_password(self, password: str, confirm: str) -> bool:
        return password == confirm
