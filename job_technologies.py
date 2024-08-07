import ahocorasick

technologies = {
    "Python": "Programming Language",
    "Java": "Programming Language",
    "JavaScript": "Programming Language",
    "C#": "Programming Language",
    "C++": "Programming Language",
    "Ruby": "Programming Language",
    "PHP": "Programming Language",
    "Swift": "Programming Language",
    "Kotlin": "Programming Language",
    "Go": "Programming Language",
    "Rust": "Programming Language",
    "TypeScript": "Programming Language",
    "HTML": "Frontend Web Development",
    "CSS": "Frontend Web Development",
    "React": "Frontend Web Development",
    "Vue.js": "Frontend Web Development",
    "Angular": "Frontend Web Development",
    "Bootstrap": "Frontend Web Development",
    "Sass": "Frontend Web Development",
    "Tailwind CSS": "Frontend Web Development",
    "Node.js": "Backend Web Development",
    "Django": "Backend Web Development",
    "Flask": "Backend Web Development",
    "Spring": "Backend Web Development",
    "Ruby on Rails": "Backend Web Development",
    "Express.js": "Backend Web Development",
    "ASP.NET": "Backend Web Development",
    "Laravel": "Backend Web Development",
    "MySQL": "Database",
    "PostgreSQL": "Database",
    "MongoDB": "Database",
    "SQLite": "Database",
    "Oracle DB": "Database",
    "Microsoft SQL Server": "Database",
    "Redis": "Database",
    "Firebase": "Database",
    "Cassandra": "Database",
    "REST": "API",
    "GraphQL": "API",
    "Docker": "DevOps",
    "Kubernetes": "DevOps",
    "Jenkins": "DevOps",
    "GitHub Actions": "DevOps",
    "Terraform": "DevOps",
    "Ansible": "DevOps",
    "Puppet": "DevOps",
    "Chef": "DevOps",
    "Git": "Version Control",
    "SVN": "Version Control",
    "Bitbucket": "Version Control",
    "GitLab": "Version Control",
    "AWS": "Cloud Platform",
    "Azure": "Cloud Platform",
    "Google Cloud Platform": "Cloud Platform",
    "Heroku": "Cloud Platform",
    "DigitalOcean": "Cloud Platform",
    "JUnit": "Testing",
    "Selenium": "Testing",
    "PyTest": "Testing",
    "Mocha": "Testing",
    "Jest": "Testing",
    "Cypress": "Testing",
    "TensorFlow": "Machine Learning",
    "PyTorch": "Machine Learning",
    "scikit-learn": "Machine Learning",
    "Keras": "Machine Learning",
    "Hadoop": "Big Data",
    "Spark": "Big Data",
    "Kafka": "Big Data",
    "Unity": "Game Development",
    "Unreal Engine": "Game Development"
}

def get_technologies():
    return technologies

def get_automaton():

    words = list(technologies.keys())

    A = ahocorasick.Automaton()


    for idx, word in enumerate(words):
        A.add_word(word, (idx, word))

    A.make_automaton()


    return A