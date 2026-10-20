
import os
import requests
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(
    page_title="ResearchFlow AI",
    page_icon="🔎",
    layout="wide",
)


try:
    BACKEND_URL = st.secrets["BACKEND_URL"].rstrip("/")
except Exception:
    BACKEND_URL = os.getenv(
        "BACKEND_URL",
        "http://127.0.0.1:8000",
    ).rstrip("/")



st.title("🔎 ResearchFlow AI")
st.subheader("Multi-Agent Research & Report Writer")

st.write(
    "Enter a research topic. Our AI workflow will search the web, "
    "analyse evidence, write a report and review the result."
)

with st.sidebar:
    st.header("About ResearchFlow AI")
    st.write("Module 27 — AI Capstone Project")
    st.write("AI workflow: Researcher → Analyst → Writer → Editor")
    st.info(
        "AI-generated information may contain errors. "
        "Check important claims against the original sources."
    )

with st.form("research_form"):
    topic = st.text_area(
        "Research topic",
        placeholder="Example: How can AI improve healthcare?",
        max_chars=300,
    )

    report_length = st.selectbox(
        "Report length",
        ["short", "standard", "detailed"],
        format_func=lambda value: {
            "short": "Short (500–700 words)",
            "standard": "Standard (900–1,200 words)",
            "detailed": "Detailed (1,400–1,800 words)",
        }[value],
    )

    submitted = st.form_submit_button(
        "Start Research",
        type="primary",
        use_container_width=True,
    )


if submitted:
    if len(topic.strip()) < 5:
        st.error("Please enter a topic with at least 5 characters.")

    else:
        try:
            with st.spinner(
                "Researching sources and generating your report..."
            ):
                response = requests.post(
                    f"{BACKEND_URL}/research",
                    json={
                        "topic": topic.strip(),
                        "report_length": report_length,
                    },
                    timeout=900,
                )

            if response.ok:
                st.session_state["research_result"] = response.json()
                st.success("Research report generated successfully!")

            else:
                try:
                    detail = response.json().get(
                        "detail",
                        response.text,
                    )
                except ValueError:
                    detail = response.text

                st.error(
                    f"Research failed ({response.status_code}): {detail}"
                )

        except requests.RequestException as error:
            st.error(
                "Could not connect to the backend. "
                "Make sure FastAPI is running on port 8000."
            )
            st.caption(str(error))


result = st.session_state.get("research_result")

if result:
    st.divider()

    st.header("Research Report")
    st.write(f"**Topic:** {result['topic']}")
    st.write(f"**Sources collected:** {result['number_of_sources']}")

    st.subheader("AI Agent Workflow")

    for item in result.get("agent_workflow", []):
        st.write(
            f"✅ **{item['agent']}** — {item['status'].title()}"
        )

    st.subheader("Generated Report")
    st.markdown(result["report_markdown"])

    sources = result.get("sources", [])

    with st.expander(
        f"View research sources ({len(sources)})",
        expanded=True,
    ):
        for index, source in enumerate(sources, start=1):
            st.markdown(
                f"{index}. [{source.get('title', 'Source')}]"
                f"({source.get('url', '')})"
            )

            if source.get("snippet"):
                st.caption(source["snippet"])

    try:
        with st.spinner("Preparing your PDF..."):
            pdf_response = requests.post(
                f"{BACKEND_URL}/reports/pdf",
                json={
                    "topic": result["topic"],
                    "report_markdown": result["report_markdown"],
                    "sources": sources,
                },
                timeout=60,
            )

        if pdf_response.ok:
            st.download_button(
                label="📄 Download Report as PDF",
                data=pdf_response.content,
                file_name="research_report.pdf",
                mime="application/pdf",
                use_container_width=True,
            )
        else:
            st.error("PDF generation failed. Please check the backend.")

    except requests.RequestException:
        st.error("Could not connect to the PDF endpoint.")
