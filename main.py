class ThisIsMrIsmail:
    def __init__(self):
        """
        Google DSC MENA '24 Lead @Google, ex-AI Intern @ITIDA, 2x ECPC,
        ex-Forward Program @McKinsey 🚀
        
        I like Machine Learning;
        """
        self.name = "Ismail Sherif"
        self.email = "ismailsherifwork@gmail.com"

    def __projects__(self):
        self.project_1 = "Lung Cancer Detection"
        self.details_1 = """
        A Convolutional Neural Network Model that detects lung cancer disease
        through CT-scanned images, classifies it into 4 classes.
        """
        
        self.project_2 = "Trible T Academy"
        self.details_2 = """
        A platform that enables users to register & buy courses online.
        """
        
        self.project_3 = "Derny Online"
        self.details_3 = """
        A system that manages all about human resource, employees, payroll,
        leaves, and more.
        """

    def __skills__(self):
        self.langs = ["Python", "C++", "JavaScript", "PHP", "PowerShell", "Bash"]
        self.tools = ["TensorFlow", "SciKit-Learn", "Pandas", "NumPy", "OpenCV"]
        self.others = {
            
            "Talks": """
            I have given talks about Machine Learning, Web Development, and more.
            """,
            
            "Events": """
            I have organized events, workshops, and hackathons. I have also
            been a speaker in some of them.
            """,
            
            "Leadership": """
            I have been a leader in many communities, clubs, and organizations.
            """,

            "Fast Typing": """
            I can type at average of 95 words per minute.
            Visit: monkeytype.com/profile/ThisIsMrIsmail
            """
        }


if __name__ == "__main__":

    NewIsmail = ThisIsMrIsmail()

    print("""
        Ohh, I forget to say.. I HAAAATE VIM.
        Don't use it, VS Code is BETTER.
    """)