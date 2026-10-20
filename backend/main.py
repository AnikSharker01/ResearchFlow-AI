
import traceback
from fastapi.responses import Response
from backend.pdf_generator import create_report_pdf

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from backend.research import search_web
from backend.tasks import generate_research_report


app = FastAPI(
    title="ResearchFlow AI",
    description="Multi-Agent Research and Report Writer",
    version="1.0.0",
)


class ResearchRequest(BaseModel):
    topic: str = Field(
        ...,
        min_length=5,
        max_length=300,
        description="Enter the topic you want to research",
    )

    report_length: str = Field(
        default="standard",
        pattern="^(short|standard|detailed)$",
        description="Choose short, standard, or detailed",
    )

class PDFRequest(BaseModel):
    topic: str
    report_markdown: str
    sources: list[dict] = Field(default_factory=list)


@app.get("/")
def home():
    return {
        "message": "Welcome to ResearchFlow AI!",
        "status": "running",
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
    }


@app.post("/research")
def start_research(request: ResearchRequest):
    topic = request.topic.strip()

    if len(topic) < 5:
        raise HTTPException(
            status_code=422,
            detail="Topic must contain at least 5 characters.",
        )

    try:
        # Step 1: Search the web
        sources = search_web(topic, max_results=5)

        if not sources:
            raise HTTPException(
                status_code=502,
                detail="No research sources were found.",
            )

        # Step 2: Run the AI agents
        report = generate_research_report(
            topic=topic,
            sources=sources,
            report_length=request.report_length,
        )

        if not report or not report.strip():
            raise HTTPException(
                status_code=502,
                detail="The AI agents returned an empty report.",
            )

        # Step 3: Return the completed report
        return {
            "status": "success",
            "message": "Research report generated successfully.",
            "topic": topic,
            "number_of_sources": len(sources),
            "report_markdown": report,
            "sources": sources,
            "agent_workflow": [
                {
                    "agent": "Researcher",
                    "status": "completed",
                },
                {
                    "agent": "Analyst",
                    "status": "completed",
                },
                {
                    "agent": "Writer",
                    "status": "completed",
                },
                {
                    "agent": "Editor",
                    "status": "completed",
                },
            ],
        }

    except HTTPException:
        raise

    except Exception as error:
        print("\n===== RESEARCH WORKFLOW ERROR =====")
        print(f"Error type: {type(error).__name__}")
        print(f"Error message: {error}")
        traceback.print_exc()
        print("===== END OF ERROR =====\n")

        raise HTTPException(
            status_code=500,
            detail=(
                "Research generation failed. "
                "Check the VS Code terminal for the actual error."
            ),
        ) from error

@app.post("/reports/pdf")
def download_report_pdf(request: PDFRequest):
    try:
        pdf_bytes = create_report_pdf(
            topic=request.topic,
            report_markdown=request.report_markdown,
            sources=request.sources,
        )

        return Response(
            content=pdf_bytes,
            media_type="application/pdf",
            headers={
                "Content-Disposition": (
                    'attachment; filename="research_report.pdf"'
                )
            },
        )

    except Exception as error:
        print(f"PDF generation failed: {error}")

        raise HTTPException(
            status_code=500,
            detail="PDF generation failed. Check the VS Code terminal.",
        ) from error
