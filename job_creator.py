import random

try:
    from faker import Faker
except ImportError:  # pragma: no cover - fallback when Faker is missing
    class Faker:
        """Simple fallback faker for environments without the ``faker`` package."""

        def job(self) -> str:
            return random.choice([
                "Engineer",
                "Developer",
                "Manager",
                "Analyst",
            ])

        def company(self) -> str:
            return random.choice([
                "Acme Corp",
                "Globex",
                "Umbrella",
                "Soylent",
            ])

        def word(self) -> str:
            letters = "abcdefghijklmnopqrstuvwxyz"
            return "".join(random.choice(letters) for _ in range(5))
import math
from typing import List, Dict, Optional
from job_seeker import JobSeeker

class JobCreator:
    def __init__(self, id: int):
        self.id = id
        self.faker = Faker()
        self.job_description = self._generate_job_description()
        self.hired_seeker = None

    def _generate_job_description(self) -> Dict:
        """Generate a random job description."""
        return {
            'title': self.faker.job(),
            'company': self.faker.company(),
            'required_skills': [self.faker.word() for _ in range(random.randint(3, 8))],
            'required_experience': random.randint(1, 10),
            'salary_range': (random.randint(50000, 100000), random.randint(100001, 200000))
        }

    def evaluate_candidate(self, seeker: JobSeeker) -> float:
        """Evaluate a job seeker and return a score between 0 and 1."""
        if seeker.is_hired:
            return 0.0

        # Calculate skill match percentage
        seeker_skills = set(seeker.get_skills())
        required_skills = set(self.job_description['required_skills'])
        skill_match = len(seeker_skills.intersection(required_skills)) / len(required_skills)

        # Calculate experience match
        experience_match = min(1.0, seeker.get_total_experience() / self.job_description['required_experience'])

        # Combine scores (70% skills, 30% experience)
        return 0.7 * skill_match + 0.3 * experience_match

    def hire_candidate(self, seeker: JobSeeker):
        """Hire a candidate and mark them as hired."""
        seeker.is_hired = True
        self.hired_seeker = seeker

    def find_best_candidate(self, candidates: List[JobSeeker]) -> Optional[JobSeeker]:
        """Use the secretary problem to find the best candidate.

        Returns the hired candidate or ``None`` if no suitable candidate is found.
        """
        n = len(candidates)
        if n == 0:
            return None

        # Calculate the optimal stopping point (37% rule)
        stopping_point = math.ceil(n * 0.37)

        # First phase: observe and find the best candidate
        best_score = -1
        best_candidate = None

        for i in range(stopping_point):
            score = self.evaluate_candidate(candidates[i])
            if score > best_score:
                best_score = score
                best_candidate = candidates[i]

        # Second phase: hire the first candidate better than the best from first phase
        for i in range(stopping_point, n):
            score = self.evaluate_candidate(candidates[i])
            if score > best_score:
                self.hire_candidate(candidates[i])
                return candidates[i]

        # If no better candidate found, hire the best from first phase
        if best_candidate:
            self.hire_candidate(best_candidate)
        return best_candidate

    def __str__(self) -> str:
        return f"JobCreator {self.id} hiring for {self.job_description['title']} at {self.job_description['company']}"
