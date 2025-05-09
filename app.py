import gradio as gr
import logging
from datetime import datetime
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler('architect_app.log')
    ]
)

def generate_architect_output():
    """
    Generates the text output representing the n8n Architect's directives for Phase 1.
    Returns:
        str: Formatted string containing the architect's persona, mission,
             phase description, and n8n action commands.
    """
    try:
        logging.info(f"Generating architect output at {datetime.now()}")
        
        output_text = """
# n8n Automation Architect & Algorithmic Trading Strategist (pump.fun Ecosystem)

**Specialization:** Designing, implementing, and optimizing n8n workflows for pump.fun.
**Primary Directive:** Design workflows to achieve a consistent and ever-increasing upward trajectory of value in user's holdings within the pump.fun ecosystem.
**Operating Principles:** Hyper-awareness of market dynamics, risk factors, and fee structures. Maximizing profitability while proactively managing risk.
**Output Format:** Precise, actionable commands for an n8n-integrated 'computer-use' agent.

The app description is: "A sophisticated automation system for pump.fun trading optimization"

---

## Your Mission: Engineer Peak pump.fun Profitability through Advanced n8n Automation.

---

## Phase 1: Establish a Superior Real-Time pump.fun Intelligence Network via n8n

Your first priority is to construct a high-fidelity, low-latency data ingestion pipeline. This network will be the bedrock of all subsequent analysis and trading decisions.

### Directive 1.1: Master pump.fun Event Ingestion.

Below are the commands for the n8n agent to configure the initial data ingestion workflows.

```xml
<ACTION command="N8N.CREDENTIALS.CREATE_IF_NOT_EXISTS" type="httpHeaderAuth" name="bloXroute_API_Auth" data='{"headerName": "Authorization", "headerValue": "YOUR_BLOXROUTE_AUTH_TOKEN_PLACEHOLDER"}' description="CRITICAL: Securely establish bloXroute API authentication. The user must replace placeholder with their actual token. This credential is vital for low-latency data streams.">
</ACTION>

<ACTION command="N8N.WORKFLOW.CREATE" name="PumpFun_MasterEventIngestor_v2" trigger='{"type": "onStartup"}' description="Core workflow to initiate and manage persistent WebSocket connections for all critical pump.fun data streams. This workflow must be resilient and auto-reconnect on failure.">
</ACTION>

<ACTION command="N8N.WORKFLOW.ADD_NODE" workflowName="PumpFun_MasterEventIngestor_v2" nodeType="n8n-nodes-base.httpRequest" name="Stream_NewPumpFunTokens_bloXroute" params='{"method": "WEBSOCKET", "url": "wss://solana.api.bloxroute.com/v1/ws", "options": {"websocket": {"sendData": "{\"jsonrpc\":\"2.0\",\"id\":1,\"method\":\"subscribe\",\"params\":[\"getPumpFunNewTokensStream\", {}]}"}}, "authentication": "headerAuth", "credentials": {"httpHeaderAuth": {"name": "bloXroute_API_Auth"}}, "retryOnFail": true, "retryCount": 5, "retryDelay": 5000}' connectTo="START" description="Establishes and maintains WebSocket for new token stream via bloXroute. Implements retry logic.">
</ACTION>

<ACTION command="N8N.WORKFLOW.ADD_NODE" workflowName="PumpFun_MasterEventIngestor_v2" nodeType="n8n-nodes-base.httpRequest" name="Stream_PumpFunSwaps_bloXroute" params='{"method": "WEBSOCKET", "url": "wss://solana.api.bloxroute.com/v1/ws", "options": {"websocket": {"sendData": "{\"jsonrpc\":\"2.0\",\"id\":1,\"method\":\"subscribe\",\"params\":[\"getPumpFunSwapsStream\", {\"include\": [\"ALL\"]}]}"}}, "authentication": "headerAuth", "credentials": {"httpHeaderAuth": {"name": "bloXroute_API_Auth"}}, "retryOnFail": true, "retryCount": 5, "retryDelay": 5000}' connectTo="START" description="Establishes and maintains WebSocket for all pump.fun swaps via bloXroute. Implements retry logic.">
</ACTION>

<ACTION command="N8N.WORKFLOW.ADD_NODE" workflowName="PumpFun_MasterEventIngestor_v2" nodeType="n8n-nodes-base.function" name="Standardize_And_Route_Stream" params='{"functionCode": "// Standardize and route incoming stream data\nconst streamData = items[0].json;\nconst standardizedData = {\n  timestamp: Date.now(),\n  eventType: streamData.method,\n  data: streamData.params\n};\n\nreturn {json: standardizedData};"}'  connectTo="Stream_NewPumpFunTokens_bloXroute,Stream_PumpFunSwaps_bloXroute" description="Standardizes incoming stream data format and routes to appropriate handlers.">
</ACTION>
```
"""
        logging.info("Successfully generated architect output")
        return output_text
    except Exception as e:
        error_msg = f"Error generating architect output: {str(e)}"
        logging.error(error_msg)
        return f"An error occurred while generating the output: {error_msg}. Please try again."

# Create the FastAPI app
app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create the Gradio interface
demo = gr.Interface(
    fn=generate_architect_output,
    inputs=None,
    outputs=gr.Textbox(
        label="Architect's Directives",
        lines=30,
        interactive=False
    ),
    title="pump.fun n8n Automation Architect",
    description="Output of the n8n Automation Architect for setting up the pump.fun data ingestion pipeline (Phase 1).",
)

# Mount the Gradio app
app = gr.mount_gradio_app(app, demo, path="/gradio")

# Mount static files
app.mount("/", StaticFiles(directory=".", html=True), name="static")

# Launch the FastAPI app with uvicorn
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
