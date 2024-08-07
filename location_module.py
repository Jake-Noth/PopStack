class Location:

    def __init__(self, location, jobs):
        self.location = location
        self.frequency_map = self.get_map(jobs)

    def get_map(self, jobs):
        freq_dict = {}

        for job in jobs:
            for technology in job.technologies:
                if technology not in freq_dict:
                    freq_dict[technology] = 1
                else:
                    freq_dict[technology] += 1
        
        return freq_dict

    def print_sorted_frequency_map(self):
        # Sort the dictionary by value in descending order
        sorted_items = sorted(self.frequency_map.items(), key=lambda item: item[1], reverse=True)
        
        # Print each item in sorted order
        for technology, count in sorted_items:
            print(f"{technology}: {count}")
