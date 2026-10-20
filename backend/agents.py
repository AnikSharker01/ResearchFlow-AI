
import os

from dotenv import load_dotenv
from crewai import Agent, LLM

load_dotenv()


def build_agents():
    """Create four AI agents using an OpenRouter model."""

    api_key = os.getenv("OPENROUTER_API_KEY")

    if not api_key:
        raise ValueError(
            "OPENROUTER_API_KEY is missing from your .env file."
        )

    model_name = os.getenv(
        "OPENROUTER_MODEL",
        "nvidia/nemotron-3-ultra:free",
    )

    llm = LLM(
        model=f"openrouter/{model_name}",
        api_key=api_key,
        base_url="https://openrouter.ai/api/v1",
        temperature=0.2,
    )

    researcher = Agent(
        role="Researcher",
        goal="Review supplied web sources and identify relevant evidence.",
        backstory=(
            "You are a careful researcher. You distinguish "
            "supported facts from uncertainty and never invent sources."
        ),
        llm=llm,
        verbose=False,
        allow_delegation=False,
    )

    analyst = Agent(
        role="Research Analyst",
        goal="Compare evidence and identify themes and limitations.",
        backstory=(
            "You critically evaluate evidence and avoid unsupported claims."
        ),
        llm=llm,
        verbose=False,
        allow_delegation=False,
    )

    writer = Agent(
        role="Report Writer",
        goal="Write a clear report based on the supplied evidence.",
        backstory=(
            "You produce structured reports with headings and "
            "references linked to the supplied sources."
        ),
        llm=llm,
        verbose=False,
        allow_delegation=False,
    )

    editor = Agent(
        role="Report Editor",
        goal="Review clarity, logic and source consistency.",
        backstory=(
            "You improve report quality without inventing facts or references."
        ),
        llm=llm,
        verbose=False,
        allow_delegation=False,
    )

    return researcher, analyst, writer, editor

