const gradioAppUrl = "http://localhost:8000/gradio";
let outputHistory = [];

async function fetchArchitectOutput() {
    const personaText = document.getElementById('persona-text');
    const missionText = document.getElementById('mission-text');
    const phaseDescriptionText = document.getElementById('phase-description-text');
    const actionsText = document.getElementById('actions-text');
    const fetchButton = document.getElementById('fetchButton');
    const spinner = document.getElementById('spinner');
    const errorMessage = document.getElementById('error-message');
    const errorText = document.getElementById('error-text');
    const historyList = document.getElementById('history-list');

    // Reset UI state
    [personaText, missionText, phaseDescriptionText, actionsText].forEach(element => {
        element.textContent = 'Fetching...';
        element.closest('section').classList.add('animate-pulse');
    });

    errorMessage.classList.add('hidden');
    spinner.classList.remove('hidden');
    fetchButton.disabled = true;

    try {
        const response = await fetch(gradioAppUrl + '/api/predict', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                session_hash: Math.random().toString(36).substring(7),
                fn_index: 0,
                data: []
            })
        });

        if (!response.ok) {
            throw new Error('Network response was not ok');
        }

        const result = await response.json();
        const outputString = result.data[0];

        // Parse output based on regex markers
        const personaMatch = outputString.match(/# n8n Automation Architect & Algorithmic Trading Strategist.*?\n.*?The app description is: "(.*?)"/s);
        const missionMatch = outputString.match(/Your Mission: (.*?)\n/);
        const phaseDescriptionMatch = outputString.match(/Phase 1: (.*?)\n/);
        const actionsMatch = outputString.match(/<ACTION.*?<\/ACTION>[\s\S]*/s);

        const personaContent = personaMatch && personaMatch[1] ? personaMatch[1].trim() : 'Not found';
        const missionContent = missionMatch && missionMatch[1] ? missionMatch[1].trim() : 'Not found';
        const phaseContent = phaseDescriptionMatch && phaseDescriptionMatch[1] ? phaseDescriptionMatch[1].trim() : 'Not found';
        const actionsContent = actionsMatch && actionsMatch[0] ? actionsMatch[0].trim() : 'No actions found for Phase 1.';

        // Update UI with parsed content
        personaText.textContent = personaContent;
        missionText.textContent = missionContent;
        phaseDescriptionText.textContent = phaseContent;
        actionsText.textContent = actionsContent;

        // Update history sidebar
        const historyItem = document.createElement('li');
        const now = new Date().toLocaleTimeString();
        historyItem.className = 'p-3 bg-gray-50 rounded-lg hover:bg-gray-100 transition-colors duration-200';
        historyItem.innerHTML = `
            <div class="text-sm text-gray-500">${now}</div>
            <div class="text-gray-700 truncate">${missionContent.substring(0, 50)}...</div>
        `;
        historyList.prepend(historyItem);

        // Store in history
        outputHistory.push({
            timestamp: now,
            persona: personaContent,
            mission: missionContent,
            phase: phaseContent,
            actions: actionsContent
        });

        // Limit history to last 10 items
        if (historyList.children.length > 10) {
            historyList.lastElementChild.remove();
        }

    } catch (error) {
        console.error("Error fetching data:", error);
        [personaText, missionText, phaseDescriptionText, actionsText].forEach(element => {
            element.textContent = 'Error fetching data.';
        });
        
        errorText.textContent = "Failed to fetch architect output. Please check your network or Gradio endpoint.";
        errorMessage.classList.remove('hidden');

        // Auto-hide error after 5 seconds
        setTimeout(() => {
            errorMessage.classList.add('hidden');
        }, 5000);
    } finally {
        // Remove loading states
        spinner.classList.add('hidden');
        fetchButton.disabled = false;
        [personaText, missionText, phaseDescriptionText, actionsText].forEach(element => {
            element.closest('section').classList.remove('animate-pulse');
        });
    }
}

// Add event listener to the button
document.getElementById('fetchButton').addEventListener('click', fetchArchitectOutput);

// Add click listeners to history items to show previous outputs
document.getElementById('history-list').addEventListener('click', (e) => {
    const historyItem = e.target.closest('li');
    if (!historyItem) return;

    const index = Array.from(historyItem.parentNode.children).indexOf(historyItem);
    const historicalOutput = outputHistory[outputHistory.length - 1 - index];
    
    if (historicalOutput) {
        document.getElementById('persona-text').textContent = historicalOutput.persona;
        document.getElementById('mission-text').textContent = historicalOutput.mission;
        document.getElementById('phase-description-text').textContent = historicalOutput.phase;
        document.getElementById('actions-text').textContent = historicalOutput.actions;
    }
});
