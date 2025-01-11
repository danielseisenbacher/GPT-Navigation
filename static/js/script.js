let map

// EXPANDING INPUT FIELD LOGIC
document.addEventListener("input", (e) => {
    if (e.target && e.target.id === "input-text") {
        const textarea = e.target;
        textarea.style.height = 'auto'; // Reset height for shrinkage
        textarea.style.height = `${textarea.scrollHeight}px`; // Adjust to content
    }
});

document.addEventListener("DOMContentLoaded", () => {
    const headerField = document.getElementById("slider");
    const toggleButton = document.getElementById("toggleButton");

    // Toggle header visibility and rotate toggle button
    toggleButton.addEventListener("click", () => {
        headerField.classList.toggle("collapsed"); // Add or remove the collapsed class
    });

    // Initialize OSM
    map = L.map('map', {
        center: [48.208, 16.37],
        zoom: 13
    });
    
    var osm = new L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
    });
    osm.addTo(map);
});

// Adjust textarea size (width and height) dynamically
function adjustTextareaSize(textarea) {
    // Reset height for shrinkage
    textarea.style.height = "auto";
    // Adjust the height based on content
    textarea.style.height = `${textarea.scrollHeight}px`;

    // Calculate the width dynamically based on content
    const span = document.createElement("span");
    span.style.visibility = "hidden";
    span.style.whiteSpace = "pre";
    span.style.fontFamily = getComputedStyle(textarea).fontFamily;
    span.style.fontSize = getComputedStyle(textarea).fontSize;
    span.style.padding = getComputedStyle(textarea).padding;
    span.textContent = textarea.value || textarea.placeholder; // Account for placeholder if empty
    document.body.appendChild(span);

    // Calculate minimum width, constrained by column width
    const contentWidth = Math.min(span.offsetWidth + 10, textarea.parentElement.offsetWidth); // Add padding
    textarea.style.width = `${contentWidth}px`;

    document.body.removeChild(span); // Clean up
}

// Event delegation for table textarea keyup events
document.getElementById("myTable").addEventListener("keyup", (event) => {
    if (event.target.tagName === "TEXTAREA") {
        adjustTextareaSize(event.target);
    }
});

// Add a new row to the table
function addRow(inputText, response) {
    const table = document.getElementById("myTable");

    // the question by the user
    if (response === false) {
        const newRow = table.insertRow();
        const cellEmpty = newRow.insertCell(0);
        const cellTextarea = newRow.insertCell(1);
        cellTextarea.classList.add("right-column");

        const textarea = document.createElement("textarea");
        textarea.value = inputText;
        textarea.readOnly = true;

        cellTextarea.appendChild(textarea);
        adjustTextareaSize(textarea); // Resize dynamically

        scrollToBottom(); // Scroll to the latest message
    }

    // The answer by ChatGPT
    else {
        const newRow2 = table.insertRow();
        const cellTextarea2 = newRow2.insertCell(0);
        const cellEmpty2 = newRow2.insertCell(1);
        cellTextarea2.classList.add("left-column");

        const textarea2 = document.createElement("textarea");
        textarea2.value = inputText;
        textarea2.readOnly = true;

        cellTextarea2.appendChild(textarea2);
        adjustTextareaSize(textarea2); // Resize dynamically

        scrollToBottom(); // Scroll to the latest message
    }
}

// Scroll the chat container to the bottom
function scrollToBottom() {
    const chatContainer = document.getElementById("chat");
    chatContainer.scrollTop = chatContainer.scrollHeight;
}

// Input form logic
async function input_logic(event) {
    event.preventDefault(); // Prevent default form submission
    const inputField = document.getElementById("input-text");
    const inputText = inputField.value.trim();

    let user_answer;

    if (inputText) {
        // clear the map before adding new data
        clear_the_map()
        
        addRow(inputText, response=false); // Add the input text to the table
        inputField.value = ""; // Clear the field
        inputField.style.height = "auto"; // Reset height

        // If you type in example1 or example2 ... example18, the example jsons are used
        const examples = Array.from({ length: 18 }, (_, i) => `example${i + 1}`);
        if (examples.includes(inputText)) {
            try {
                // Get the JSON from the example files
                const json_answer = await use_example_jsons(inputText);
                // Once the JSON is fetched, interpret and display it
                if (json_answer) {
                    user_answer = await interpret_json_answer(json_answer);
                }
            } catch (error) {
                console.error('Error loading JSON:', error);
            }
        }
        else {
            // call python-anywhere
            const json_answer = await callPythonScript(inputText);

            if (json_answer) {
                user_answer = await interpret_json_answer(json_answer);
            }
        }
        
        // write the answert that is supposed to go to the user
        addRow(user_answer, response=true);
    }
}

async function callPythonScript(param) {
    try {
        console.log(`https://danielseisenbacher.pythonanywhere.com/run-script?param=${encodeURIComponent(param)}`)
        const response = await fetch(`https://danielseisenbacher.pythonanywhere.com/run-script?param=${encodeURIComponent(param)}`);
        const data = await response.json();
        console.log(data); // Output the result from the Python script
        return data;
    } catch (error) {
        console.error('Error calling Python script:', error);
        return "Error!";
    }
}

// Fetch JSON for the examples
async function use_example_jsons(inputText) {
    const match = inputText.match(/\d+/); // Extract the number from input (e.g., example1, example2)
    const number = match ? match[0] : null;
    
    if (number) {
        const fileName = `q${number}.json`;  // Example: q1.json
        const filePath = `example_json/${fileName}`;

        try {
            const response = await fetch(filePath);
            if (!response.ok) {
                throw new Error('File not found');
            }
            const data = await response.json();
            console.log('Loaded JSON data:', data);  // Handle the loaded data
            return data;  // Return the data to be used in the input_logic function
        } catch (error) {
            console.error('Error loading JSON file:', error);
            return null;  // Return null if error occurs
        }
    } else {
        console.error('Invalid input text');
        return null;  // Return null if inputText doesn't match expected format
    }
}

// Interpret the JSON and add features to the map
function interpret_json_answer(json_answer) {
    if (!json_answer || !json_answer.features || !Array.isArray(json_answer.features)) {
        console.error("Invalid JSON structure or missing 'features' property.");
        return; // Exit if the structure is not valid
    }
    
    // read the answer that should be visible to the user
    let user_answer;
    if (json_answer && json_answer.answer !== undefined) {
        user_answer = json_answer.answer;
    } else {
        user_answer = "A key in the provided JSON is missing for the answer to the user. This key should be called 'answer'. If provided, it will be visible here.";
    }

console.log(user_answer);

    // Iterate over the features and add them to the map
    json_answer.features.forEach(feature => {
        const geometry = feature.geometry;
        const properties = feature.properties;
        
        let layer;

        // Check geometry type and create appropriate layer
        if (geometry.type === 'Point') {
            layer = L.marker([geometry.coordinates[1], geometry.coordinates[0]]);
        } else if (geometry.type === 'Polygon') {
            layer = L.polygon(geometry.coordinates[0].map(coord => [coord[1], coord[0]]));
        } else if (geometry.type === 'LineString') {
            layer = L.polyline(geometry.coordinates.map(coord => [coord[1], coord[0]]));
        }

        // Bind a popup with dynamic properties
        if (properties) {
            let popupContent = `<strong>Properties:</strong><br>`;
            for (const [key, value] of Object.entries(properties)) {
                popupContent += `<strong>${key}:</strong> ${value}<br>`;
            }
            layer.bindPopup(popupContent);
        }

        // Add the layer to the map
        layer.addTo(map);
    });

    // provide an user_answer to the question
    return user_answer;
}

function clear_the_map() {
    // Clear the map before adding new features
    map.eachLayer(function(layer) {
        try {
            // Skip tile layers and remove only non-tile layers
            if (!layer.hasOwnProperty('_url')) {
                map.removeLayer(layer);
            }
        } catch (error) {
            console.log("Unsuccessful layer removal", error);
        }
    });
}


