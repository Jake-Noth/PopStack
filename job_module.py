class Job:

    def __init__(self, title, company, description):
        self.title = title
        self.company = company
        self.description = description
        self.technologies = []

    def get_matches(self, Automaton):
        matches = []

        for end_index, (idx, word) in Automaton.iter(self.description):
            start_index = end_index - len(word) + 1
            matches.append(word)
        
        self.technologies = matches
        return matches

    def __del__(self):
        None