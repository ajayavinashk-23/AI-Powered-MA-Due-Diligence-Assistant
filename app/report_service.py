import os
from datetime import datetime

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph
from reportlab.platypus import Spacer


class ReportService:

    def generate_report(
        self,
        dashboard,
        analysis,
        questions=None
    ):

        if questions is None:
            questions = []

        report = f"""
# AI-Powered M&A Due Diligence Report

Generated On:
{datetime.now().strftime("%d-%m-%Y %H:%M")}

====================================================

DOCUMENT STATISTICS

Pages : {dashboard['pages']}

Words : {dashboard['words']}

Characters : {dashboard['characters']}

Chunks : {dashboard['chunks']}

====================================================

EXECUTIVE SUMMARY

{analysis['Executive Summary']}

====================================================

FINANCIAL HIGHLIGHTS

{analysis['Financial Highlights']}

====================================================

RISK ANALYSIS

{analysis['Risk Analysis']}

====================================================

IMPORTANT PARTIES

{analysis['Important Parties']}

====================================================

IMPORTANT DATES

{analysis['Important Dates']}

====================================================

QUESTIONS ASKED

"""

        for question in questions:

            report += f"\n• {question}"

        report += """

====================================================

DISCLAIMER

This report has been generated using the
AI-Powered M&A Due Diligence Assistant.

The report should be reviewed by a human
analyst before making legal, financial or
business decisions.

====================================================

END OF REPORT

"""

        return report

    def save_markdown(
        self,
        report,
        filename="Due_Diligence_Report.md"
    ):

        os.makedirs("reports", exist_ok=True)

        path = os.path.join(
            "reports",
            filename
        )

        with open(path, "w", encoding="utf-8") as f:

            f.write(report)

        return path

    def save_pdf(
        self,
        dashboard,
        analysis,
        filename="Due_Diligence_Report.pdf"
    ):

        os.makedirs("reports", exist_ok=True)

        pdf_path = os.path.join(
            "reports",
            filename
        )

        doc = SimpleDocTemplate(pdf_path)

        styles = getSampleStyleSheet()

        story = []

        story.append(
            Paragraph(
                "<b>AI-Powered M&A Due Diligence Report</b>",
                styles["Title"]
            )
        )

        story.append(
            Paragraph(
                datetime.now().strftime(
                    "%d-%m-%Y %H:%M"
                ),
                styles["Normal"]
            )
        )

        story.append(Spacer(1, 20))

        story.append(
            Paragraph(
                "<b>Document Statistics</b>",
                styles["Heading2"]
            )
        )

        story.append(
            Paragraph(
                f"""
Pages : {dashboard['pages']}<br/>
Words : {dashboard['words']}<br/>
Characters : {dashboard['characters']}<br/>
Chunks : {dashboard['chunks']}
                """,
                styles["BodyText"]
            )
        )

        story.append(Spacer(1, 15))

        sections = [

            "Executive Summary",

            "Financial Highlights",

            "Risk Analysis",

            "Important Parties",

            "Important Dates"

        ]

        for section in sections:

            story.append(
                Paragraph(
                    f"<b>{section}</b>",
                    styles["Heading2"]
                )
            )

            story.append(
                Paragraph(
                    analysis[section],
                    styles["BodyText"]
                )
            )

            story.append(Spacer(1, 15))

        story.append(
            Paragraph(
                "<b>Disclaimer</b>",
                styles["Heading2"]
            )
        )

        story.append(
            Paragraph(
                """
This report has been generated automatically
using the AI-Powered M&A Due Diligence Assistant.

Always validate the findings manually before
making financial or legal decisions.
                """,
                styles["BodyText"]
            )
        )

        doc.build(story)

        return pdf_path