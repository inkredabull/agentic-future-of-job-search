import random
try:
    from faker import Faker
except ImportError:  # pragma: no cover - fallback when Faker is missing
    class Faker:
        """Simplified fallback faker used when the real library is unavailable."""

        def company(self) -> str:
            return random.choice([
                "Acme Corp",
                "Globex",
                "Umbrella",
                "Soylent",
            ])

        def job(self) -> str:
            return random.choice([
                "Engineer",
                "Developer",
                "Manager",
                "Analyst",
            ])

        def word(self) -> str:
            letters = "abcdefghijklmnopqrstuvwxyz"
            return "".join(random.choice(letters) for _ in range(5))

from typing import List, Dict

class JobSeeker:
    def __init__(self, id: int):
        self.id = id
        self.faker = Faker()
        self.work_history = self._generate_work_history()
        self.is_hired = False

    def _generate_work_history(self) -> List[Dict]:
        """Generate a random work history for the job seeker."""
        num_jobs = random.randint(1, 5)
        work_history = []

        for _ in range(num_jobs):
            job = {
                'company': self.faker.company(),
                'position': self.faker.job(),
                'duration': random.randint(1, 10),  # years
                'skills': [self.faker.word() for _ in range(random.randint(3, 8))],
                'years_experience': random.randint(1, 15)
            }
            work_history.append(job)

        return work_history

    def get_skills(self) -> List[str]:
        """Get all unique skills from work history."""
        all_skills = []
        for job in self.work_history:
            all_skills.extend(job['skills'])
        return list(set(all_skills))

    def get_total_experience(self) -> int:
        """Calculate total years of experience."""
        return sum(job['years_experience'] for job in self.work_history)

    def __str__(self) -> str:
        return f"JobSeeker {self.id} with {len(self.work_history)} jobs and {self.get_total_experience()} years experience"
