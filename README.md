
Built by https://www.blackbox.ai

---

# pump.fun n8n Automation Architect

## Project Overview
The `pump.fun n8n Automation Architect` is a frontend application designed to interact with a Gradio backend. This application allows users to display and retrieve structured architect directives related to the n8n automation process specifically for the pump.fun ecosystem. Users can obtain information about personas, missions, phase descriptions, and various actions generated for setting up automated workflows.

## Installation
To set up the project, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd pump.fun-n8n-architect
   ```

2. **Install Gradio for Backend**:
   If you don't have Gradio installed, use pip:
   ```bash
   pip install gradio
   ```

3. **Run the Backend**:
   Save the provided backend code in a file named `app.py` and execute:
   ```bash
   python app.py
   ```

   This starts a Gradio server, which by default runs on `http://localhost:8000/gradio`.

4. **Frontend Setup**:
   Ensure that the following files are in the same directory:
   - `index.html`
   - `style.css`
   - `script.js`
   
   In `script.js`, set the `gradioAppUrl` variable to point to your running Gradio app:
   ```javascript
   const gradioAppUrl = "http://localhost:8000/gradio";
   ```

## Usage
1. **Open the Frontend**:
   Open `index.html` in a web browser.

2. **Fetch Architect Output**:
   Click the "Fetch Architect Output" button to retrieve the architect's directives. The output will be displayed in designated sections: Persona, Mission, Phase Description, and Actions.

3. **Using the Output**:
   The information displayed can then be used to set up workflows in the n8n automation platform.

## Features
- Display structured information from the Gradio backend.
- Fetch and parse architect directives tailored for the pump.fun ecosystem.
- Highlight interaction design with responsive feedback using loading states and error handling.
- Maintain an output history to revisit fetched data.

## Dependencies
- Python with the Gradio library

Install dependencies with:
```bash
pip install gradio
```

For the frontend, ensure you include the necessary CDN links for libraries in `index.html` such as Tailwind CSS and Font Awesome.

## Project Structure
```
pump.fun-n8n-architect/
│
├── app.py                # Backend application using Gradio
├── index.html            # Main HTML frontend file
├── style.css             # CSS styles for the frontend
├── script.js             # JavaScript file for handling interactions
└── tasks.md              # Project tasks and description
```

### Additional Notes
- Make sure to replace `"YOUR_GRADIO_APP_URL_HERE"` in `script.js` with the actual URL of your running Gradio application.
- The output parsing logic in JavaScript may require adjustments depending on the actual output format from the backend.

For contributions or further inquiries, please contact the project maintainers or raise an issue on the repository.