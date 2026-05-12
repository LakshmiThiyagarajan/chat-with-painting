const API_URL = "http://localhost:8000/chat";

console.log("SCRIPT LOADED");

let selectedPainting = "";

let session_id = localStorage.getItem("paintchat_session");
if (!session_id) {
  session_id = crypto.randomUUID();
  localStorage.setItem("paintchat_session", session_id);
}

const characters = {
  "Stolen Interview": ["woman", "man"],
  "Damayanti and the Swan": ["damayanti", "swan"],
  "Mohini on a Swing": ["mohini"]
};

// Card click handler (ONLY here)
document.querySelectorAll(".card").forEach(card => {
  card.addEventListener("click", () => {
    selectPainting(card.dataset.painting);
  });
});

// Send button handler (ONLY here)
document.getElementById("sendBtn").addEventListener("click", sendMessage);

function selectPainting(painting) {
  selectedPainting = painting;
  document.getElementById("selectedPainting").innerText = painting;

  const dropdown = document.getElementById("characterSelect");
  dropdown.innerHTML = "";

  characters[painting].forEach(character => {
    const option = document.createElement("option");
    option.value = character;
    option.textContent = character;
    dropdown.appendChild(option);
  });

  document.getElementById("chatWindow").innerHTML = "";
}

function addMessage(message, type) {
  const div = document.createElement("div");
  div.className = `message ${type}`;
  div.innerText = message;
  document.getElementById("chatWindow").appendChild(div);
}

async function sendMessage() {
  const messageInput = document.getElementById("messageInput");
  const message = messageInput.value.trim();
  const character = document.getElementById("characterSelect").value;

  if (!message || !selectedPainting) return;

  addMessage(message, "user-message");
  messageInput.value = "";

  const thinking = document.createElement("div");
  thinking.className = "message bot-message";
  thinking.innerText = "...";
  document.getElementById("chatWindow").appendChild(thinking);

  const response = await fetch(API_URL, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      session_id,
      painting: selectedPainting,
      character,
      message
    })
  });

  const data = await response.json();
  thinking.remove();
  addMessage(data.reply, "bot-message");
}