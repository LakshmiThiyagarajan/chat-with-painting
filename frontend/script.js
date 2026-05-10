const API_URL = "http://127.0.0.1:8000/chat";

let selectedPainting = "";

const characters = {

  "Stolen Interview": ["woman", "man"],

  "Damayanti and the Swan": [
    "damayanti",
    "swan"
  ],

  "Mohini on a Swing": ["mohini"]
};

function selectPainting(painting) {

  selectedPainting = painting;

  document.getElementById(
    "selectedPainting"
  ).innerText = painting;

  const dropdown =
    document.getElementById("characterSelect");

  dropdown.innerHTML = "";

  characters[painting].forEach(character => {

    const option =
      document.createElement("option");

    option.value = character;

    option.textContent = character;

    dropdown.appendChild(option);
  });
}

async function sendMessage() {

  const character =
    document.getElementById("characterSelect").value;

  const message =
    document.getElementById("messageInput").value;

  const replyBox =
    document.getElementById("replyBox");

  replyBox.innerText = "Thinking...";

  const response = await fetch(API_URL, {

    method: "POST",

    headers: {
      "Content-Type": "application/json"
    },

    body: JSON.stringify({

      painting: selectedPainting,
      character: character,
      message: message
    })
  });

  const data = await response.json();

  replyBox.innerText = data.reply;
}