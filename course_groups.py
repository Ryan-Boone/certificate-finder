from __future__ import annotations
from dataclasses import dataclass
from typing import List, Optional, Tuple

@dataclass
class CourseGroup:
    name: str
    courses: List[Tuple[str, int]]
    subgroups: List[CourseGroup]
    required_count: int
    credits_min: Optional[int] = None
    credits_max: Optional[int] = None
    optional: bool = False

@dataclass
class Certificate:
    name: str
    required_credits: int
    minimum_gpa: float
    required_courses: List[Tuple[str, int]]
    course_groups: List[CourseGroup]

data_science_cert = Certificate(
    name="Data Science",
    required_credits=16,
    minimum_gpa=2.0,
    required_courses=[],  # No standalone required courses
    course_groups=[
        CourseGroup(
            name="Foundation Courses",
            courses=[],
            subgroups=[
                CourseGroup(
                    name="Programming Requirement",
                    courses=[
                        ("STAT 240", 4),
                        ("ECE 204", 3)
                    ],
                    subgroups=[
                        CourseGroup(
                            name="Python",
                            courses = [
                                ("COMP SCI 220", 4),
                                ("COMP SCI 320", 4)
                            ],
                            subgroups = [],
                            required_count = 0,
                            credits_min = 0,
                            credits_max = 4
                        )
                    ],
                    required_count=2,
                    credits_min=7,
                    credits_max=8
                ),
                CourseGroup(
                    name="Ethics Requirement",
                    courses=[
                        ("LIS 461", 4),
                        ("ECE/ISYE 570", 3)
                    ],
                    subgroups=[],
                    required_count=1,
                    credits_min=3,
                    credits_max=4
                )
            ],
            required_count=3,
            credits_min=10,
            credits_max=12
        ),
        CourseGroup(
            name = "Elective Courses",
            courses = [],
            subgroups = [
                CourseGroup(
                    name = "Fundamental Electives",
                    courses = [
                        ("BIOCORE 382", 2),
                        ("BIOCORE 384", 2),
                        ("BIOCORE 486", 2),
                        ("COMP SCI 320", 4),
                        ("COMP SCI 544", 3)
                    ],
                    subgroups = [],
                    required_count = 1,
                    credits_min = 3,
                    credits_max = 6
                ),
                CourseGroup(
                    name = "Domain Electives",
                    courses = [
                        ("AAE/ECON 421", 4),
                        ("LIS 440", 3),
                        ("LSC 460", 3),
                        ("LSC 660", 3),
                        ("SOC 351", 4)
                    ],
                    subgroups = [],
                    required_count = 0,
                    credits_min = 0,
                    credits_max = 3
                )
            ],
            required_count = 2,
            credits_min = 6,
            credits_max = 6
        )
    ]
)
