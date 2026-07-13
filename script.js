function sendMessage() {

    let input = document.getElementById("userInput");
    let chatBox = document.getElementById("chatBox");

    let message = input.value.trim();

    if (message === "") {
        return;
    }

    // Show user message
    chatBox.innerHTML += `
        <div class="user-message">
            ${message}
        </div>
    `;


    fetch("/chat", {

        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify({
            message: message
        })

    })

    .then(response => response.json())

    .then(data => {

        chatBox.innerHTML += `
            <div class="bot-message">
                ${data.response}
            </div>
        `;

        chatBox.scrollTop = chatBox.scrollHeight;

    })

    .catch(error => {

        chatBox.innerHTML += `
            <div class="bot-message">
                Error connecting to WattWise AI
            </div>
        `;

        console.log(error);

    });


    input.value = "";

}