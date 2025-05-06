import random
from job_seeker import JobSeeker
from job_creator import JobCreator
from typing import List

def create_job_seekers(num_seekers: int) -> List[JobSeeker]:
    """Create a list of job seekers."""
    return [JobSeeker(i) for i in range(num_seekers)]

def create_job_creators(num_creators: int) -> List[JobCreator]:
    """Create a list of job creators."""
    return [JobCreator(i) for i in range(num_creators)]

def main():
    # Create job seekers and creators
    num_seekers = 100
    num_creators = 10
    
    job_seekers = create_job_seekers(num_seekers)
    job_creators = create_job_creators(num_creators)
    
    # Process each job creator
    for creator in job_creators:
        print(f"\n{creator}")
        print(f"Looking for: {creator.job_description['title']}")
        print(f"Required skills: {', '.join(creator.job_description['required_skills'])}")
        print(f"Required experience: {creator.job_description['required_experience']} years")
        
        # Get available candidates (not hired yet)
        available_candidates = [seeker for seeker in job_seekers if not seeker.is_hired]
        
        if not available_candidates:
            print("No available candidates left!")
            continue
            
        # Shuffle candidates to simulate random order
        random.shuffle(available_candidates)
        
        # Find and hire the best candidate
        hired_candidate = creator.find_best_candidate(available_candidates)
        
        if hired_candidate:
            print(f"\nHired: {hired_candidate}")
            print("Work History:")
            for job in hired_candidate.work_history:
                print(f"- {job['position']} at {job['company']} ({job['years_experience']} years)")
            print(f"Skills: {', '.join(hired_candidate.get_skills())}")
        else:
            print("No suitable candidate found!")

if __name__ == "__main__":
    main() 