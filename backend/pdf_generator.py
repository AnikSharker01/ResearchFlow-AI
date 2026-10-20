
from io import BytesIO
from xml.sax.saxutils import escape

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    HRFlowable,
)


def create_report_pdf(
    topic: str,
    report_markdown: str,
    sources: list[dict],
) -> bytes:
    """Create a downloadable PDF research report."""

    buffer = BytesIO()

    document = SimpleDocTemplate(
        buffer,
        pagesize=A4,
        rightMargin=20 * mm,
        leftMargin=20 * mm,
        topMargin=18 * mm,
        bottomMargin=18 * mm,
        title=f"ResearchFlow AI - {topic[:100]}",
        author="ResearchFlow AI",
    )

    styles = getSampleStyleSheet()

    styles.add(
        ParagraphStyle(
            name="ReportTitle",
            parent=styles["Title"],
            alignment=TA_CENTER,
            fontSize=19,
            leading=24,
            textColor=colors.HexColor("#17365D"),
            spaceAfter=12,
        )
    )

    styles.add(
        ParagraphStyle(
            name="ReportBody",
            parent=styles["BodyText"],
            fontSize=9.5,
            leading=14,
            spaceAfter=7,
        )
    )

    story = [
        Paragraph("ResearchFlow AI", styles["ReportTitle"]),
        Paragraph(escape(topic), styles["Heading2"]),
        Paragraph(
            "Multi-Agent Research Report",
            styles["Italic"],
        ),
        Spacer(1, 5 * mm),
        HRFlowable(
            width="100%",
            thickness=1,
            color=colors.HexColor("#AAB7C4"),
        ),
        Spacer(1, 5 * mm),
    ]

    # Convert the report's basic Markdown headings to PDF headings.
    for raw_line in report_markdown.splitlines():
        line = raw_line.strip()

        if not line:
            story.append(Spacer(1, 2 * mm))
            continue

        if line.startswith("### "):
            story.append(
                Paragraph(escape(line[4:]), styles["Heading3"])
            )

        elif line.startswith("## "):
            story.append(
                Paragraph(escape(line[3:]), styles["Heading2"])
            )

        elif line.startswith("# "):
            story.append(
                Paragraph(escape(line[2:]), styles["Heading1"])
            )

        elif line.startswith(("- ", "* ")):
            story.append(
                Paragraph(
                    "&#8226; " + escape(line[2:]),
                    styles["ReportBody"],
                )
            )

        else:
            story.append(
                Paragraph(escape(line), styles["ReportBody"])
            )

    if sources:
        story.append(Spacer(1, 5 * mm))
        story.append(
            Paragraph("Retrieved Sources", styles["Heading2"])
        )

        for index, source in enumerate(sources, start=1):
            title = escape(str(source.get("title", "Source")))
            url = escape(str(source.get("url", "")))

            story.append(
                Paragraph(
                    f"[{index}] {title}<br/>"
                    f'<font size="8">{url}</font>',
                    styles["ReportBody"],
                )
            )

    document.build(story)

    return buffer.getvalue()
