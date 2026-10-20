# ResearchFlow AI: Multi-Agent Research and Report Writer

## 1. Introduction

Finding relevant information and preparing a research report can be time-consuming. Users must search multiple websites, compare information, organise findings and prepare a clear document. The quality of a report also depends on the reliability of its sources and the accuracy of its references.

ResearchFlow AI was developed as a Python-based web application to assist with this process. It combines web search, a multi-agent AI workflow and PDF generation. Users can enter a research topic, retrieve online sources, generate a structured report and download the result as a PDF.

The project was developed for the Module 27 Capstone Project. It demonstrates how frontend development, backend programming and AI integration can be combined to address a practical information-management problem.

## 2. Objectives

The project objectives were to:

1. Develop a user interface for submitting research topics.
2. Retrieve relevant web sources through a search API.
3. Coordinate specialised AI agents for research, analysis, writing and editing.
4. Generate a structured report with source links.
5. Provide a PDF download function.
6. Use Git and GitHub for version control and code hosting.
7. Deploy the application online and test its main workflow.

The implementation includes the frontend, backend API, web search integration, agent workflow, PDF generation and GitHub repository. The application was also deployed using Render and Streamlit Community Cloud.

## 3. System Architecture and Technology

ResearchFlow AI uses Python as its main programming language. Streamlit provides the frontend, while FastAPI handles backend requests. CrewAI coordinates the agents, OpenRouter provides access to the selected language model, Tavily retrieves web search results, and ReportLab generates PDF documents.

Git was used for version control, and GitHub hosts the source code. Render hosts the backend, while Streamlit Community Cloud hosts the frontend.

The system follows this workflow:

1. The user submits a topic through the Streamlit interface.
2. The frontend sends a request to the FastAPI backend.
3. Tavily retrieves relevant web search results.
4. CrewAI coordinates the Researcher, Analyst, Writer and Editor.
5. The backend returns the generated report and source information.
6. The user can inspect the report and download it as a PDF.

The project is organised into separate frontend, backend, documentation and screenshot directories. This structure helps separate user-interface code, API logic, AI orchestration and supporting documentation.

## 4. AI Workflow and Methodology

### 4.1 Researcher

The Researcher reviews the retrieved search results and identifies information relevant to the submitted topic. It is instructed to preserve source URLs, distinguish supported claims from uncertainty and avoid inventing references.

### 4.2 Analyst

The Analyst compares the available evidence, identifies common themes and differences, and describes limitations and evidence gaps. Its output provides an analytical basis for the report.

### 4.3 Writer

The Writer prepares a structured report using the research and analysis outputs. The intended structure includes an executive summary, introduction, key findings, discussion, limitations, conclusion and references.

### 4.4 Editor

The Editor reviews the draft for clarity, logical organisation, repetition and consistency between claims and the supplied sources. It is instructed to qualify unsupported statements and avoid inventing references.

CrewAI executes these tasks sequentially, passing the outputs of earlier tasks to later tasks. OpenRouter provides the language-model access, while Tavily supplies the initial web search results.

Although the workflow is designed to improve organisation and consistency, the agents do not guarantee that every statement or citation is correct. Human verification remains necessary.

## 5. Implementation

### 5.1 Frontend

The Streamlit interface provides a research-topic input field, a report-length selector and a Start Research button. It displays the generated report, retrieved sources and agent workflow status. A PDF download button allows the user to save the report.

### 5.2 Backend

FastAPI provides endpoints for the home page, health check, research generation and PDF download. The research endpoint validates the submitted topic, calls the search function and coordinates report generation. Error handling returns appropriate responses when requests fail.

### 5.3 Web research and PDF generation

The research module sends search requests to Tavily and collects source titles, URLs and text excerpts. The PDF generator uses ReportLab to produce a document containing the report text and retrieved source links.

### 5.4 Version control and deployment

Git was used to maintain the project history, and the code was uploaded to the ResearchFlow AI GitHub repository. The backend was deployed on Render and the frontend on Streamlit Community Cloud. The deployed application was opened in a browser and used to generate a research report.

## 6. Testing and Results

Testing was conducted locally through VS Code and the FastAPI interactive documentation, followed by testing of the deployed application.

| Test | Observed result | Status |
|---|---|---|
| FastAPI startup | Server started successfully | Pass |
| Health endpoint | Returned a healthy status | Pass |
| Tavily search | Returned web sources for the test topic | Pass |
| OpenRouter connection | A text response was received during the isolated model test | Pass |
| Research generation | The research endpoint returned HTTP 200 and report content | Pass |
| PDF generation | A PDF was downloaded through the API documentation | Pass |
| Streamlit interface | Topic input, report output and source list were displayed | Pass |
| Backend deployment | Render reported a successful deployment | Pass |
| Frontend deployment | The public Streamlit application loaded and generated a report | Pass |
| GitHub upload | Project files were pushed to the main branch | Pass |

During development, the initial OpenAI API request failed because the account had insufficient credits. The application was subsequently configured to use OpenRouter. An initial model identifier was also rejected before a different free-model configuration returned a response.

The first report output required further review because some content was irrelevant and some retrieved sources were commercial or outdated. This demonstrated that successful model execution does not automatically ensure research quality. The report-writing instructions were subsequently revised to emphasise source quality, citation consistency and concise writing.

The tests establish that the main workflow operates, but they do not establish that every generated claim is accurate. A more comprehensive evaluation would require a larger test set, systematic citation checks and documented measurements of report quality.

## 7. Limitations

The application depends on external APIs and internet access. Free-model availability, request limits, provider capacity and hosting behaviour can change.

Search results may include commercial pages, outdated articles or excerpts that omit important context. The agents may produce unsupported statements, inconsistent citations or reports that do not follow the requested word limit. Automated editing cannot guarantee complete factual accuracy.

The current prototype also lacks a comprehensive automated test suite and a systematic evaluation of report quality. These limitations should be considered when interpreting the output.

## 8. Conclusion and Future Improvements

ResearchFlow AI demonstrates a working multi-agent research and report-writing prototype. It integrates a Streamlit frontend, FastAPI backend, Tavily web search, CrewAI orchestration, OpenRouter model access and ReportLab PDF generation.

The application was tested locally and deployed online. The observed results show that it can retrieve web sources, generate report content, display results through a user interface and provide a downloadable PDF.

Future improvements include stronger source ranking, more reliable citation verification, automated tests, improved progress reporting, stricter report-length checks and systematic evaluation using multiple research topics. The application should be treated as a research-assistance tool rather than a substitute for independent verification.

## 9. Innovation and Impact

### 9.1 Innovation

ResearchFlow AI integrates web search, multi-agent collaboration and automated report generation within a single application. Instead of relying on a single language-model response, the system separates the workflow into four roles: Researcher, Analyst, Writer and Editor. This design provides a structured process for collecting information, analysing findings, drafting a report and reviewing its clarity.

The application also combines source links with downloadable PDF output. This allows users to inspect retrieved sources and retain a report for further review. A potential future improvement is a Source Quality and Citation Audit feature that checks citation consistency and flags claims requiring additional verification. This feature should be described as future work until it has been implemented and tested.

### 9.2 Potential Impact

ResearchFlow AI is intended to support students and early-stage researchers who need to organise online information and prepare initial research drafts. By combining search, analysis, writing and PDF generation, it may reduce repetitive work and provide a more organised starting point for research.

The application also makes source links visible, helping users return to the original material. However, AI-generated content may contain inaccuracies, and source availability does not guarantee that a claim is supported. Users must verify important statements against the original sources before relying on the report.

### 9.3 Evaluation of Innovation and Impact

The prototype demonstrates the integration of web research, four specialised AI-agent roles, a web interface and PDF generation. These features establish the technical basis for the proposed solution. Further evaluation is needed to measure report accuracy, citation reliability, time saved and user satisfaction. These outcomes should be assessed through documented tests rather than assumed from successful report generation alone.

## 10. Project Links

- **Live frontend:** https://researchflow-ai-vt3kzn327itgzy8wkfjquu.streamlit.app/
- **Backend API:** https://researchflow-ai-959i.onrender.com
- **API documentation:** https://researchflow-ai-959i.onrender.com/docs
- **Health check:** https://researchflow-ai-959i.onrender.com/health
- **GitHub repository:** https://github.com/AnikSharker01/ResearchFlow-AI

## References

1. CrewAI. Official documentation. https://docs.crewai.com/
2. FastAPI. Official documentation. https://fastapi.tiangolo.com/
3. OpenRouter. API documentation. https://openrouter.ai/docs
4. ReportLab. Official documentation. https://docs.reportlab.com/
5. Streamlit. Official documentation. https://docs.streamlit.io/
6. Tavily. Official documentation. https://docs.tavily.com/
