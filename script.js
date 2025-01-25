const sendBtn = document.getElementById("send-btn");
const userInput = document.getElementById("user-input");
const messagesDiv = document.getElementById("messages");

sendBtn.addEventListener("click", async () => {
    const userMessage = userInput.value.trim();
    if (userMessage === "") return;

    // Tampilkan pesan pengguna
    const userMessageDiv = document.createElement("div");
    userMessageDiv.classList.add("message", "user");
    userMessageDiv.innerText = userMessage;
    messagesDiv.appendChild(userMessageDiv);

    // Kirim ke backend
    const response = await fetch("http://127.0.0.1:5000/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: userMessage }),
    });

    const data = await response.json();
    const aiMessage = data.reply || "Tidak ada balasan dari AI.";

    // Tampilkan pesan AI
    const aiMessageDiv = document.createElement("div");
    aiMessageDiv.classList.add("message", "ai");
    aiMessageDiv.innerText = aiMessage;
    messagesDiv.appendChild(aiMessageDiv);

    // Reset input
    userInput.value = "";
    messagesDiv.scrollTop = messagesDiv.scrollHeight;
});