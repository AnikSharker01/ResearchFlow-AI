
from crewai import Crew, Process, Task

from backend.agents import build_agents


def generate_research_report(
    topic: str,
    sources: list[dict],
    report_length: str = "standard",
) -> str:
    """Generate an evidence-based report using four AI agents."""

    researcher, analyst, writer, editor = build_agents()

    # Give every source a number so the report can cite it.
    source_blocks = []

    for index, source in enumerate(sources, start=1):
        source_blocks.append(
            f"[{index}]\n"
            f"Title: {source.get('title', 'Untitled source')}\n"
            f"URL: {source.get('url', '')}\n"
            f"Search excerpt: {source.get('snippet', '')}"
        )

    source_text = "\n\n".join(source_blocks)

    length_rules = {
        "short": (
            "Write 500-700 words for the report body. "
            "Keep the report concise."
        ),
        "standard": (
            "Write 900-1200 words for the report body."
        ),
        "detailed": (
            "Write 1400-1800 words for the report body."
        ),
    }

    length_instruction = length_rules.get(
        report_length,
        length_rules["standard"],
    )

    # Task 1: Researcher
    research_task = Task(
        description=(
            f"Research topic: {topic}\n\n"
            "Review the supplied search results critically. "
            "Identify relevant claims, useful evidence and limitations.\n\n"
            "SOURCE QUALITY RULES:\n"
            "- Prefer peer-reviewed studies, official institutions "
            "and recognised professional organisations.\n"
            "- Identify commercial, promotional or opinion-based sources.\n"
            "- Treat old sources cautiously when current evidence matters.\n"
            "- Search excerpts are not full papers. Do not claim to have "
            "read a full paper when only an excerpt is supplied.\n"
            "- Do not invent authors, dates, statistics or findings.\n\n"
            f"SUPPLIED SOURCES:\n{source_text}"
        ),
        expected_output=(
            "An evidence brief with numbered source references, "
            "source quality notes, supported findings and evidence gaps."
        ),
        agent=researcher,
    )

    # Task 2: Analyst
    analysis_task = Task(
        description=(
            f"Analyse the evidence about: {topic}\n\n"
            "Compare the claims supported by the supplied sources. "
            "Distinguish established findings from suggestions, "
            "opinions and future possibilities. Explain disagreements "
            "and limitations. Do not add unsupported facts.\n\n"
            "Use the original source numbers [1], [2], etc. "
            "Do not create new source numbers."
        ),
        expected_output=(
            "A concise critical analysis of the evidence, source "
            "quality, key themes and limitations."
        ),
        agent=analyst,
        context=[research_task],
    )

    # Task 3: Writer
    writing_task = Task(
        description=(
            f"Write a research report about: {topic}\n\n"
            f"WORD LIMIT: {length_instruction}\n\n"
            "Use this structure:\n"
            "# Title\n"
            "## Executive Summary\n"
            "## 1. Introduction\n"
            "## 2. Key Findings\n"
            "## 3. Analysis and Discussion\n"
            "## 4. Limitations of the Evidence\n"
            "## 5. Conclusion\n"
            "## References\n\n"
            "CITATION RULES:\n"
            "- Cite claims using source numbers, for example [1].\n"
            "- Each citation must refer to the matching supplied source.\n"
            "- Include only supplied sources in the reference list.\n"
            "- Never invent a journal, author, publication date or DOI.\n"
            "- Do not present a search excerpt as proof of clinical "
            "effectiveness.\n"
            "- If the evidence is weak, say so clearly.\n\n"
            "Avoid repeating the same idea in multiple sections. "
            "Use simple, professional academic English."
        ),
        expected_output=(
            "A concise, structured Markdown report with accurate "
            "source numbering, a clear conclusion and references."
        ),
        agent=writer,
        context=[research_task, analysis_task],
    )

    # Task 4: Editor
    editing_task = Task(
        description=(
            "Edit the draft report before returning it.\n\n"
            "Check all of the following:\n"
            "1. The report answers the user's topic.\n"
            "2. The requested word limit is followed as closely as possible.\n"
            "3. Every numbered citation refers to a supplied source.\n"
            "4. No sources, authors, dates or statistics are invented.\n"
            "5. Commercial or outdated sources are not treated as "
            "strong clinical evidence.\n"
            "6. Unsupported claims are removed or qualified.\n"
            "7. The report has all required headings and no unnecessary "
            "repetition.\n\n"
            "Return only the complete revised Markdown report. "
            "Do not return a safety label, a progress message or a "
            "description of your editing process."
        ),
        expected_output=(
            "The final revised research report in Markdown, "
            "with source citations and references."
        ),
        agent=editor,
        context=[research_task, analysis_task, writing_task],
    )

    crew = Crew(
        agents=[researcher, analyst, writer, editor],
        tasks=[
            research_task,
            analysis_task,
            writing_task,
            editing_task,
        ],
        process=Process.sequential,
        verbose=True,
    )

    result = crew.kickoff()

    return str(result)
