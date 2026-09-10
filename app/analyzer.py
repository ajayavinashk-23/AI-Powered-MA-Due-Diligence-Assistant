from app.rag_service import RAGService


class DocumentAnalyzer:

    def __init__(self):
        self.rag = RAGService()

    def analyze(self):

        questions = {

            "Executive Summary":
            "Provide a concise executive summary of this document.",

            "Financial Highlights":
            "List all important financial information present in the document.",

            "Risk Analysis":
            "Identify all business, legal and financial risks.",

            "Important Parties":
            "Who are the important people, organisations or companies mentioned?",

            "Important Dates":
            "List every important date mentioned in the document."

        }

        report = {}

        for section, question in questions.items():

            result = self.rag.ask(question)

            report[section] = result["answer"]

        return report