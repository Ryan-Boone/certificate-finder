import PyPDF2
import re
from dataclasses import dataclass
from typing import List, Dict
import os

@dataclass
class Course:
    department: str
    number: str
    credits: float
    grade: str
    name: str
    term: str = ""

def darsProcessor(pdf_path: str) -> List[Course]:
    # Read PDF
    with open(pdf_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()

    # Pattern to match course entries with term codes
    course_pattern = r'((?:FA|SP|SU)\d{2})\s+([A-Z]+\s*[A-Z]*\d+)\s+(\d+\.\d+)\s+([A-Z]+|INP)\s+([^|\n]+)'
    
    courses = []
    for match in re.finditer(course_pattern, text):
        term, course_code, credits, grade, name = match.groups()
        
        # Split department and number
        dept_match = re.match(r'([A-Z& ]+)(\d+|X\d+)', course_code.strip())
        if dept_match:
            dept, num = dept_match.groups()
        else:
            dept = course_code
            num = ""
        
        course = Course(
            department=dept.strip(),
            number=num.strip(),
            credits=float(credits),
            grade=grade,
            name=name.strip(),
            term=term
        )
        courses.append(course)
    
    # Remove duplicates while keeping most recent grade
    unique_courses: Dict[str, Course] = {}
    for course in courses:
        key = f"{course.department}{course.number}"
        if key not in unique_courses or course.grade == 'INP':
            unique_courses[key] = course
    
    # Sort by department and number
    return sorted(unique_courses.values(), key=lambda x: (x.department, x.number))

def print_courses_by_department(courses: List[Course]):
    # Group courses by department
    departments: Dict[str, List[Course]] = {}
    for course in courses:
        if course.department not in departments:
            departments[course.department] = []
        departments[course.department].append(course)
    
    # Print courses by department
    for dept in sorted(departments.keys()):
        print(f"\n{dept} Department:")
        print("-" * 80)
        print(f"{'Term':<6} {'Course':<12} {'Credits':<8} {'Grade':<6} {'Name'}")
        print("-" * 80)
        for course in departments[dept]:
            print(f"{course.term:<6} {course.department}{course.number:<12} "
                  f"{course.credits:<8.2f} {course.grade:<6} {course.name}")

def main():
    # Get user's home directory
    home_dir = os.path.expanduser("~")
    # Assuming the PDF is in Downloads folder
    pdf_path = os.path.join(home_dir, "Downloads", "audit.pdf")
    
    try:
        courses = darsProcessor(pdf_path)
        print_courses_by_department(courses)
    except FileNotFoundError:
        print(f"Could not find PDF file at {pdf_path}")
        print("Please ensure your DARS audit PDF is in your Downloads folder and named 'audit.pdf'")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
    