# Job Agent Simulation

This project simulates a job market with job seekers and job creators using the secretary problem (optimal stopping problem) for hiring decisions.

## Features

- Simulates 100 job seekers with unique work histories
- Simulates 10 job creators with unique job descriptions
- Uses the secretary problem (37% rule) for optimal hiring decisions
- Evaluates candidates based on skills and experience
- Provides detailed output of hiring decisions and candidate information

## Requirements

- Python 3.7+
- numpy
- faker

## Installation

1. Clone this repository
2. Install the required packages:
```bash
pip install -r requirements.txt
```

## Usage

Run the simulation:
```bash
python main.py
```

The program will:
1. Create 100 job seekers with random work histories
2. Create 10 job creators with random job descriptions
3. Process each job creator's hiring decision
4. Output detailed information about each hiring decision

## How it Works

- Each job seeker has a unique work history with multiple jobs, skills, and years of experience
- Each job creator has a unique job description with required skills and experience
- The hiring process uses the secretary problem (37% rule) to make optimal hiring decisions
- Once a job seeker is hired, they are removed from the available candidate pool
- The evaluation process considers both skill matches (70%) and experience matches (30%)
