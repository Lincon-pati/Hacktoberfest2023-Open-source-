class MarketingResearch:
    def __init__(self, company_name):
        self.company_name = company_name

    def conduct_survey(self):
        print(f"Conducting a survey for {self.company_name}...")

        # Simulate data collection (in a real scenario, you'd collect data from various sources)
        survey_results = {
            "age": [25, 30, 35, 40, 45],
            "satisfaction": [4, 5, 3, 4, 5],
            "interest": [7, 8, 6, 7, 9]
        }

        return survey_results

    def analyze_survey_results(self, survey_results):
        print("Analyzing survey results...")

        # Simulate data analysis (in a real scenario, you'd perform more complex analysis)
        average_satisfaction = sum(survey_results["satisfaction"]) / len(survey_results["satisfaction"])
        average_interest = sum(survey_results["interest"]) / len(survey_results["interest"])

        print(f"Average satisfaction: {average_satisfaction}")
        print(f"Average interest: {average_interest}")

    def run_marketing_research(self):
        print(f"Starting marketing research for {self.company_name}...\n")
        survey_results = self.conduct_survey()
        self.analyze_survey_results(survey_results)
        print("\nMarketing research completed for", self.company_name)


# Example usage
company_name = "ABC Company"
marketing_research = MarketingResearch(company_name)
marketing_research.run_marketing_research()
