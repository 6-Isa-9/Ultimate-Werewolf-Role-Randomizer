// Code to enable and disable vampire team based on no. of players
var vampire_button = document.getElementById("toggle-vampires");
var vampire_input = document.getElementById("vampires");
var vampire_label = document.getElementById("vampires-label");

var vampire_warning = document.getElementById("vampire-warning");
var player_warning = document.getElementById("players-warning");

function checkVampireCompatibility() {
    // Warning message for vampire compatibility + disabling visuals
    if (player_input.value <= 8) {
        // Disabling button
        vampire_button.disabled = true;
        vampire_button.checked = false;
        // Disabling checkbox
        vampire_input.disabled = true;
        // Visually disabling button
        vampire_button.classList.add('disabled');
        vampire_button.classList.remove('active');
        // Visually disabling label
        vampire_label.classList.add("disabled");
        // Displaying vampire warning message
        vampire_warning.style.display = 'block';
    }
    else {
        // Enabling button
        vampire_button.disabled = false;
        // Enabling checkbox
        vampire_input.disabled = false;
        // Visually enabling button and label
        vampire_button.classList.remove('disabled');
        vampire_label.classList.remove("disabled");
        // Removing warning message
        vampire_warning.style.display = 'none';
    }

    // Warning message for increased player count
    if (player_input.value >= 35) {
        // Displaying player warning message
        player_warning.style.display = 'block'
    }
    else {
        // Displaying player warning message
        player_warning.style.display = 'none'
    }

}

// Checks on page reload
window.onload = checkVampireCompatibility;





// Function to update player value
var player_input = document.getElementById("players");
var player_display = document.getElementById("player-value");

function updatePlayerValue() {
    checkVampireCompatibility();
    player_display.innerText = player_input.value;
}

player_input.addEventListener("change", updatePlayerValue);
player_input.addEventListener("mousemove", updatePlayerValue);
player_input.addEventListener("touchmove", updatePlayerValue);






// Function for fancy checkbox graphics (ooOOoOOooh nice box) 
function toggleButton(buttonId, checkboxId) {
    const button = document.getElementById(buttonId);
    const checkbox = document.getElementById(checkboxId);

    button.addEventListener('click', () => {
        checkbox.checked = !checkbox.checked;
        button.classList.toggle('active');
    });
}

toggleButton('toggle-solo', 'solo');
toggleButton('toggle-vampires', 'vampires');
toggleButton('toggle-npc', 'npc');






// Code to apply colors to role cards
var all_cards = document.querySelectorAll(".card");

all_cards.forEach(function(card) {
    var role_type = card.getAttribute("data-type");

    if (role_type === "W") {
        card.style.backgroundColor = "#743d3d";
    }
    else if (role_type === "V") {
        card.style.backgroundColor = "#4f3869";
    }
    else if (role_type === "S") {
        card.style.backgroundColor = "#9b8509";
    }
    else if (role_type === "T") {
        card.style.backgroundColor = "#38426e";
    }
});