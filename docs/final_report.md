# ResearchFlow AI: Multi-Agent Research and Report Writer

## 1. Introduction

Finding reliable information and preparing a research report can require considerable time. Users need to search different websites, identify relevant evidence, organise findings and prepare a clear document. The quality of a report also depends on the reliability of its sources and the accuracy of its references.

ResearchFlow AI was developed as a Python-based application to assist with these tasks. It combines web search, a multi-agent AI workflow and PDF generation. The application allows users to enter a research topic, retrieve online sources, generate a structured report and download the result as a PDF.

The project was developed for Module 27, the AI Capstone Project. Its main purpose is to demonstrate how frontend development, backend programming and AI integration can be combined to address a practical problem.

## 2. Objectives

The project had the following objectives:

1. Develop a simple interface for submitting research topics.
2. Retrieve web sources using a search API.
3. Coordinate separate AI agents for research, analysis, writing and editing.
4. Generate structured reports containing source references.
5. Provide a PDF download function.
6. use Git and GitHub for version control and code hosting.
7. Prepare the application for online deployment.

The implementation covers the main research workflow, the user interface, the backend API, PDF generation and GitHub hosting. Online deployment remains a separate task to be completed and verified.

## 3. System Design and Technology

ResearchFlow AI uses Python as its main programming language. The frontend was developed with Streamlit, while FastAPI provides the backend endpoints. CrewAI coordinates the AI agents, and OpenRouter provides access to the selected language model. Tavily retrieves web search results, while ReportLab generates PDF documents.

Git was used for version control, and GitHub hosts the source code repository.

The project is organised into separate folders. The `frontend` folder contains the Streamlit application. The `backend` folder contains the API, agent definitions, task orchestration, search functionality and PDF generator. The `docs` folder contains the project proposal and final report. Configuration files and dependencies are maintained separately.

This structure makes the main components easier to understand, test and maintain.

## 4. AI Workflow and Methodology

The application follows a sequential multi-agent workflow.

### 4.1 Researcher

The Researcher receives the topic and examines the web search results supplied by Tavily. Its task is to identify relevant information, retain source URLs and recognise limitations in the available evidence.

### 4.2 Analyst

The Analyst examines the research material, identifies common themes and compares different claims. It is instructed to distinguish supported findings from uncertainty and avoid unsupported conclusions.

### 4.3 Writer

The Writer prepares a structured report based on the research and analysis. The report can contain an executive summary, introduction, findings, analysis, limitations, conclusion and references.

### 4.4 Editor

The Editor reviews the draft for clarity, logical organisation and consistency between claims and the supplied sources. It is also instructed not to invent references.

CrewAI coordinates the agents through sequential tasks, passing earlier outputs to later tasks. The workflow is designed to improve organisation and consistency, although the agents cannot guarantee that every claim or citation is correct.

## 5. Frontend and Backend Implementation

The Streamlit interface provides a research-topic input field, report-length selection and a Start Research button. After the user submits a topic, the frontend sends a request to the FastAPI backend.

The backend validates the topic, calls the Tavily search function and passes the retrieved sources to the AI workflow. When generation succeeds, the API returns the topic, report text, source information and agent status information.

The application also includes a PDF endpoint. It accepts the report content and source list and uses ReportLab to create a downloadable PDF document. This allows the report to be saved and read outside the application.

Error handling was included for failed research requests and PDF generation. Environment variables are used to keep API credentials separate from the main source code.

## 6. Testing and Results

Testing was conducted locally in VS Code and through the browser-based API documentation.

| Test | Observed result | Status |
|---|---|---|
| FastAPI server startup | Server started successfully and reported application startup completion | Pass |
| Health endpoint | Health-check endpoint was implemented | Verify final result |
| Tavily search | Five web sources were returned for the test topic | Pass |
| OpenRouter connection | The selected free-model route returned a text response during an isolated connection test | Pass |
| AI report generation | The research endpoint returned HTTP 200 and generated report content | Pass |
| PDF generation | A PDF file was downloaded through the API documentation | Pass |
| Streamlit interface | The topic form, report display and source list appeared in the browser | Pass |
| GitHub upload | Project files were pushed to the `main` branch | Pass |
| Online deployment | Not yet completed | Pending |

During testing, an initial OpenAI API request failed because the account had no remaining credits. The project was subsequently configured to use OpenRouter. An initial model identifier was also rejected, after which a different configuration was tested successfully.

The report-generation test produced a structured document with sections discussing findings, limitations and implications. However, the initial report also contained material that required further quality review. Some retrieved sources were commercial or older articles rather than strong clinical evidence. Therefore, successful generation was treated as evidence of functional operation, not proof of research accuracy.

The table records observed implementation results. Tests marked for verification must be repeated before the final submission.

## 7. Limitations

The quality of the output depends on the retrieved sources and the selected language model. Search snippets may omit important context, and some websites may be outdated, commercial or unsuitable for supporting scientific claims.

The AI agents can produce incorrect statements, inconsistent citations or content that does not fully follow the requested word limit. The Editor can identify some problems, but automated review cannot guarantee complete accuracy.

Free model availability, rate limits and provider capacity can also change. The current prototype requires internet access and valid API credentials for web search and language-model requests.

Further work is needed to improve source ranking, verify citations against original pages, enforce report-length limits and test error handling more systematically.

## 8. Conclusion and Future Improvements

ResearchFlow AI demonstrates a working prototype of a multi-agent research and report-writing application. It combines a Streamlit frontend, FastAPI backend, Tavily web search, CrewAI agent orchestration, OpenRouter model access and PDF generation.

The local tests demonstrated that web search could return sources, the selected model could respond, the research workflow could generate report content and the PDF endpoint could produce a downloadable file. The project was also uploaded to GitHub.

Future improvements include stronger source-quality filtering, more reliable citation verification, clearer progress indicators, automated testing, report-length checks and online deployment. The final deployed version should be tested before submission.

ResearchFlow AI is intended to support research drafting rather than replace critical evaluation. Users should consult original sources and independently verify important claims before relying on the generated report.

## References

1. CrewAI. Official documentation. https://docs.crewai.com/
2. FastAPI. Official documentation. https://fastapi.tiangolo.com/
3. OpenRouter. API documentation. https://openrouter.ai/docs
4. ReportLab. Official documentation. https://docs.reportlab.com/
5. Streamlit. Official documentation. https://docs.streamlit.io/
6. Tavily. Official documentation. https://docs.tavily.com/
