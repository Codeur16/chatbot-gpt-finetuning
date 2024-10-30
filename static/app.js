document.getElementById('send-btn').addEventListener('click', function() {
    const userInput = document.getElementById('user-input').value;
    const textarea = document.getElementById('user-input');
    function formatResponse(response) {
        // Rechercher le texte après "Answer:"
        const answerIndex = response.indexOf("Completion:");
        
        // Si "Answer:" est trouvé, extraire la partie après
        if (answerIndex !== -1) {
            return response.substring(answerIndex + 11).trim(); // Extraire et supprimer les espaces inutiles
        }
        
        // Si "Answer:" n'est pas trouvé, retourner la réponse telle quelle
        return response;
    }
    
textarea.addEventListener('input', function() {
    // Réinitialise la hauteur à 'auto' pour recalculer la hauteur
    this.style.height = 'auto';
    
    // Ajuste la hauteur en fonction du contenu
    this.style.height = (this.scrollHeight) + 'px';
});

    if (userInput.trim() === '') return;

    // Ajouter le message de l'utilisateur au chat
    addMessageToChat('user', userInput);

    // Effacer l'input
    document.getElementById('user-input').value = '';

    // Afficher un loader pendant que la réponse est générée
    const loaderElement = addLoaderToChat();

    // Envoyer la question à l'API Flask
    fetch('http://127.0.0.1:5000/answer', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ question: userInput }),
    })
    .then(response => response.json())
    .then(data => {
        // Supprimer le loader
        loaderElement.remove();

        // Ajouter la réponse du chatbot au chat
        addMessageToChat('bot', formatResponse(data.response));
    })
    .catch(error => {
        console.error('Error:', error);
        loaderElement.remove();
        addMessageToChat('bot', 'Une erreur est survenue. Réessayez plus tard.');
    });
});

// Ajouter un message au chat
function addMessageToChat(sender, message) {
    const chatBox = document.getElementById('chat-box');
    const messageElement = document.createElement('div');
    messageElement.classList.add('message', sender);
    messageElement.textContent = message;
    chatBox.appendChild(messageElement);
    chatBox.scrollTop = chatBox.scrollHeight; // Scroller vers le bas
}

// Ajouter un loader au chat
function addLoaderToChat() {
    const chatBox = document.getElementById('chat-box');
    const loaderElement = document.createElement('div');
    loaderElement.classList.add('loader');
    chatBox.appendChild(loaderElement);
    chatBox.scrollTop = chatBox.scrollHeight; // Scroller vers le bas

    return loaderElement;
}
