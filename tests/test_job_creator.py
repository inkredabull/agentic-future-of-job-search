import os
import sys
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from job_creator import JobCreator
from job_seeker import JobSeeker


def make_seeker(id_, skills, years_exp):
    seeker = JobSeeker(id_)
    seeker.work_history = [
        {
            'company': 'TestCo',
            'position': 'Dev',
            'duration': years_exp,
            'skills': skills,
            'years_experience': years_exp,
        }
    ]
    return seeker


def make_creator(required_skills, required_experience):
    creator = JobCreator(0)
    creator.job_description = {
        'title': 'Role',
        'company': 'Comp',
        'required_skills': required_skills,
        'required_experience': required_experience,
        'salary_range': (1, 1),
    }
    return creator


def test_hire_first_best_candidate():
    # candidate 0 perfectly matches
    s0 = make_seeker(0, ['python', 'sql'], 4)
    # candidate 1 lacks skills
    s1 = make_seeker(1, ['java'], 6)

    creator = make_creator(['python', 'sql'], 3)

    hired = creator.find_best_candidate([s0, s1])
    assert hired is s0
    assert s0.is_hired


def test_hire_late_better_candidate():
    s0 = make_seeker(0, ['x'], 2)
    s1 = make_seeker(1, ['y'], 1)
    s2 = make_seeker(2, ['x', 'y'], 5)

    creator = make_creator(['x', 'y'], 4)

    hired = creator.find_best_candidate([s0, s1, s2])
    assert hired is s2
    assert s2.is_hired
