import time
from ZipScrape import get_jobs
from job_technologies import get_automaton
from location_module import Location  # Import the Location class correctly

Automaton = get_automaton()

while True:
    try:
        jobs = get_jobs()
        break
    except:
        pass  # Use pass instead of None for an empty exception handler

# Create a list of jobs with technologies
valid_jobs = []

for job in jobs:
    job.get_matches(Automaton)
    if len(job.technologies) > 0:
        valid_jobs.append(job)

test_loc = Location('test', jobs)

test_loc.print_sorted_frequency_map()
