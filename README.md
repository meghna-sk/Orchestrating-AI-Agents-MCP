# AI Debate System Using Model Context Protocol (MCP)

This project implements an AI-powered debate system where two autonomous agents engage in a structured debate on the topic of Universal Basic Income (UBI). The system uses the Model Context Protocol (MCP) to facilitate communication between the agents, ensuring a clear and organized exchange of arguments.

## Features

- Two autonomous AI agents (Pro and Con) engaging in structured debate
- Turn-based interaction with configurable number of turns
- Persistent debate transcripts
- Secure API key management
- Clear agent roles and responsibilities
- Structured message format using MCP

## Prerequisites

- Python 3.x
- Anthropic API key (Claude 3 Opus)
- Virtual environment (recommended)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/meghna-sk/Orchestrating-AI-Agents-MCP
cd Orchestrating-AI-Agents-MCP
```

2. Create and activate a virtual environment:

For Windows (Command Prompt):
```bash
python -m venv venv
venv\Scripts\activate.bat
```

For Windows (PowerShell):
```bash
python -m venv venv
.\venv\Scripts\Activate.ps1
```

For Unix/MacOS:
```bash
python -m venv venv
source venv/bin/activate
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the project root and add your Anthropic API key:
```
ANTHROPIC_API_KEY=your_api_key_here
```
## Usage

1. Ensure your virtual environment is activated
2. Run the debate:
```bash
python run_debate.py
```

The debate will run automatically, with agents taking turns to present their arguments. The output will be displayed in the console and saved to a transcript file.

## Debate Format

Each debate turn includes:
- Agent name
- Role (Pro/Con)
- Content (argument)
- Turn number

## Output

The debate results are printed on the cmd