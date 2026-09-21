const aiForm = document.getElementById("ai-form");
const aiInput = document.getElementById("ai-question");
const aiSendButton = document.getElementById("ai-send-btn");
const aiChatBox = document.getElementById("ai-chat-box");

aiForm.addEventListener("submit", async function (event) {

    event.preventDefault();

    const question = aiInput.value.trim();

    if (!question) {
        return;
    }

    aiSendButton.disabled = true;
    aiSendButton.innerText = "Thinking...";

    const farmerMessage = document.createElement("div");

    farmerMessage.className = "ai-message";

    farmerMessage.innerHTML = `
        <div class="ai-avatar">👨‍🌾</div>

        <div class="ai-message-content">
            <strong>You</strong>
            <p>${question}</p>
        </div>
    `;

    
    aiChatBox.appendChild(farmerMessage);

aiForm.reset();


    const csrfToken = document.querySelector(
        '[name="csrfmiddlewaretoken"]'
    ).value;

    const formData = new FormData();

    formData.append("question", question);
    formData.append("csrfmiddlewaretoken", csrfToken);

    try {

        const response = await fetch("/ai-assistant/", {
            method: "POST",
            body: formData
        });

        console.log("Status:", response.status);

        const data = await response.json();

        console.log("AI Response:", data);

        const aiMessage = document.createElement("div");

        aiMessage.className = "ai-message";

        aiMessage.innerHTML = `
            <div class="ai-avatar">🤖</div>

            <div class="ai-message-content">
                <strong>AI Farmer Assistant</strong>
                <p>${data.answer}</p>
            </div>
        `;

        aiChatBox.appendChild(aiMessage);

        aiChatBox.scrollTop = aiChatBox.scrollHeight;

    } catch (error) {

        console.error("AI Error:", error);

        const errorMessage = document.createElement("div");

        errorMessage.className = "ai-message";

        errorMessage.innerHTML = `
            <div class="ai-avatar">⚠️</div>

            <div class="ai-message-content">
                <strong>Error</strong>
                <p>AI Assistant se response nahi aa raha hai.</p>
            </div>
        `;

        aiChatBox.appendChild(errorMessage);

    }

    aiSendButton.disabled = false;
    aiSendButton.innerText = "Send";

});