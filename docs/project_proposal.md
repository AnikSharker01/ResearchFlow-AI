# ResearchFlow AI: Multi-Agent Research and Report Writer

## 1. Problem Statement

Preparing a research report requires users to find relevant information, compare sources, organise findings and write a clear document. This process can take time, particularly when information comes from different websites. Reports may also contain unsupported claims or weak references if the source material is not checked carefully.

ResearchFlow AI aims to support this process through a web application that combines web search with a coordinated team of artificial intelligence (AI) agents. The system assists with research and report drafting while allowing users to inspect the retrieved sources.

## 2. Aim and Objectives

The main aim is to develop a Python-based application that automates parts of the research and report-writing workflow.

The objectives are to:

1. Provide a simple interface for entering a research topic.
2. Retrieve relevant web sources using a search API.
3. Use separate AI agents for research, analysis, writing and editing.
4. Generate a structured report with source links.
5. Convert the report into a downloadable PDF.
6. Test the application locally and deploy it online.
7. document the design, implementation, testing and limitations.

## 3. Proposed Solution

ResearchFlow AI uses a Streamlit frontend and a FastAPI backend. Users enter a topic and select the desired report length through the interface. The backend obtains search results through the Tavily API and passes the retrieved source information to a workflow managed by CrewAI.

The workflow contains four agents: Researcher, Analyst, Writer and Editor. The Researcher reviews the retrieved information, the Analyst identifies key themes and limitations, the Writer prepares the report, and the Editor reviews its clarity and source consistency. The application then presents the report and source links and provides a PDF download option.

The language model is accessed through OpenRouter, which provides access to different models, including models offered under free usage tiers. Availability and usage limits depend on the selected model and provider.

## 4. Technology Stack

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Streamlit | User interface |
| FastAPI | Backend API |
| CrewAI | Agent coordination |
| OpenRouter | Language-model access |
| Tavily | Web search |
| ReportLab | PDF generation |
| Git and GitHub | Version control and code hosting |
| Render and Streamlit Community Cloud | Planned deployment |

## 5. Evaluation Plan

The application will be evaluated through functional testing. Tests will cover valid and invalid research topics, source retrieval, AI report generation, missing API keys, error handling and PDF downloads. Deployment will be tested by accessing the public application and confirming communication between the frontend and backend.

Report quality will be assessed by checking structure, clarity, source traceability and whether claims are appropriately qualified. Search results and AI-generated references will not automatically be treated as verified evidence.

## 6. Expected Outcome

The expected outcome is a working web application that accepts a research topic, retrieves online sources, coordinates multiple AI agents, produces a structured report and allows PDF download. The system is intended as a research-assistance prototype rather than a replacement for independent source verification or expert judgement.
