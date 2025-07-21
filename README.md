# Strands Agent Chat Application

A full-stack web application that provides a chat interface for interacting with a Strands AI agent powered by AWS Bedrock's Claude Sonnet 4 model.

## Features

- 🤖 **AI-Powered Chat**: Interact with Claude Sonnet 4 through a clean web interface
- 🔧 **Built-in Tools**: The agent has access to:
  - **Calculator**: Perform mathematical calculations and solve equations
  - **Current Time**: Get the current date and time
  - **Letter Counter**: Count occurrences of specific letters in words
- 🌐 **Full-Stack Architecture**: FastAPI backend with Angular frontend
- ⚡ **Real-time Responses**: Fast, responsive chat experience

## Architecture

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Angular       │    │   FastAPI       │    │   Strands       │
│   Frontend      │◄──►│   Backend       │◄──►│   Agent         │
│   (Port 4200)   │    │   (Port 8000)   │    │   (AWS Bedrock) │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

## Prerequisites

- **Python 3.11+**
- **Node.js 18+**
- **AWS Account** with Bedrock access
- **AWS CLI** configured

## Setup Instructions

### 1. Clone and Navigate to Project

```bash
cd StrandsProject
```

### 2. AWS Configuration

Configure your AWS credentials with the following requirements:

```bash
aws configure
```

When prompted, provide:
- **AWS Access Key ID**: Your AWS access key
- **AWS Secret Access Key**: Your AWS secret key  
- **Default region name**: `us-east-2`
- **Default output format**: `json`

> **Important**: The region must be set to `us-east-2` as this is where the Claude Sonnet 4 model is available.

### 3. Python Backend Setup

#### Create and activate virtual environment:
```bash
python -m venv .venv
.\.venv\Scripts\Activate.ps1  # Windows PowerShell
```

#### Install Python dependencies:
```bash
pip install -r my_agent/requirements.txt
```

#### Install additional FastAPI dependencies:
```bash
pip install fastapi uvicorn python-multipart
```

### 4. Angular Frontend Setup

#### Navigate to frontend directory:
```bash
cd agent-frontend
```

#### Install Node.js dependencies:
```bash
npm install
```

## Running the Application

### 1. Start the FastAPI Backend

From the project root directory:
```bash
.\.venv\Scripts\Activate.ps1
python web_app/app.py
```

The backend will be available at: `http://localhost:8000`

### 2. Start the Angular Frontend

In a new terminal, from the `agent-frontend` directory:
```bash
npm start
```

The frontend will be available at: `http://localhost:4200`

## Usage

1. Open your browser and navigate to `http://localhost:4200`
2. You'll see a chat interface titled "🤖 Strands Agent Chat"
3. Type your message in the text area and click "Send" or press Enter
4. The agent will respond using its available tools when appropriate

### Example Interactions

**Math Calculations:**
```
User: What is 15 * 27?
Agent: I'll calculate that for you. 15 × 27 = 405
```

**Current Time:**
```
User: What time is it?
Agent: The current time is 3:45 PM UTC on July 21, 2025.
```

**Letter Counting:**
```
User: How many letter 'e's are in the word "elephant"?
Agent: The word "elephant" contains 2 letter E's.
```

## Project Structure

```
StrandsProject/
├── my_agent/                 # Core agent implementation
│   ├── agent.py             # Original agent with demo
│   ├── web_agent.py         # Agent for web service
│   └── requirements.txt     # Python dependencies
├── web_app/                 # FastAPI backend
│   ├── app.py              # Main FastAPI application
│   └── agent_service.py    # Agent service module
├── agent-frontend/          # Angular frontend
│   ├── src/app/chat/       # Chat component
│   ├── src/app/services/   # API service
│   └── package.json        # Node.js dependencies
└── README.md               # This file
```

## API Endpoints

### Backend (Port 8000)

- **GET /** - Health check endpoint
- **POST /chat** - Send message to agent
  ```json
  // Request
  {
    "message": "Your question here"
  }
  
  // Response
  {
    "response": "Agent's response",
    "status": "success"
  }
  ```

## Troubleshooting

### Common Issues

1. **"AccessDeniedException" Error**
   - Ensure your AWS region is set to `us-east-2`
   - Verify your AWS credentials have Bedrock access
   - Run `aws configure` to update your settings

2. **Frontend Not Loading**
   - Check that you're accessing `http://localhost:4200`
   - Ensure the Angular dev server is running with `npm start`

3. **Backend Connection Error**
   - Verify the FastAPI server is running on port 8000
   - Check that both virtual environment is activated

4. **"Sorry, there was an error processing your request"**
   - Check the FastAPI server logs for detailed error messages
   - Verify AWS configuration is correct

### Checking Service Status

**Backend Status:**
```bash
curl http://localhost:8000/
# Should return: {"message": "Strands Agent API is running!"}
```

**Test Chat Endpoint:**
```bash
curl -X POST "http://localhost:8000/chat" -H "Content-Type: application/json" -d '{"message": "Hello"}'
```

## Development

### Adding New Tools

To add new tools to the agent:

1. Create a new tool function in `my_agent/web_agent.py`:
```python
@tool
def my_new_tool(param: str) -> str:
    """Description of what the tool does."""
    # Tool implementation
    return result
```

2. Add it to the agent's tools list:
```python
agent = Agent(
    model="us.anthropic.claude-sonnet-4-20250514-v1:0",
    tools=[calculator, current_time, letter_counter, my_new_tool]
)
```

### Frontend Modifications

The Angular frontend is a standalone component-based application. Key files:
- `src/app/chat/chat.ts` - Chat component logic
- `src/app/chat/chat.html` - Chat component template
- `src/app/services/agent.ts` - API service for backend communication

## License

This project is for demonstration purposes. Please ensure compliance with AWS Bedrock and Strands licensing terms for production use.

## Support

For issues related to:
- **Strands SDK**: Visit [Strands Documentation](https://strandsagents.com)
- **AWS Bedrock**: Check [AWS Bedrock Documentation](https://docs.aws.amazon.com/bedrock/)
- **This Application**: Check the troubleshooting section above
