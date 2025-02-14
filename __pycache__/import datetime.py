import datetime

class ProjectReport:
    def __init__(self):
        self.entries = []

    def add_entry(self, date, hours, description):
        """Add a new entry to the report."""
        self.entries.append((date, hours, description))

    def display_report(self):
        """Display the report in a formatted table."""
        print("=============Report====================")
        print("            Time Spent")
        print("   Date       (hours)   Description of Work")
        print("----------  ----------  -------------------------")
        for date, hours, description in self.entries:
            print(f"{date}     {hours:<10}  {description}")
        print("=============Report====================")


report = ProjectReport()
report.add_entry("2024-10-21", 1.0, "Discussed project scope and requirements with a tutor")
report.add_entry("2024-10-22", 2.0, "Researched relevant articles and watched tutorials on project topic")
report.add_entry("2024-10-23", 1.5, "Designed initial project architecture and created diagrams")
report.add_entry("2024-10-24", 3.0, "Wrote experimental code to test initial ideas")
report.add_entry("2024-10-25", 4.0, "Developed core functionality and program features")
report.add_entry("2024-10-26", 2.0, "Created test functions and wrote unit tests")
report.add_entry("2024-10-27", 1.5, "Debugged code and fixed errors identified during testing")
report.add_entry("2024-10-28", 1.0, "Documented project progress and prepared for presentation")
report.display_report()