function triggerUpload() {
    document.getElementById("fileInput").click();
}

function copyText() {
    const text = document.getElementById("output").innerText;

    if (!text || text === "Your result will appear here...") {
        alert("No text to copy!");
        return;
    }

    navigator.clipboard.writeText(text);
    alert("Text copied to clipboard!");
}

async function uploadFile() {
    const fileInput = document.getElementById("fileInput");
    const output = document.getElementById("output");

    if (!fileInput.files.length) {
        alert("Please select a file");
        return;
    }

    const file = fileInput.files[0];

    // File size check (5MB)
    if (file.size > 5 * 1024 * 1024) {
        alert("File too large! Max size is 5MB.");
        return;
    }

    const formData = new FormData();
    formData.append("file", file);

    output.innerText = "Processing... (may take 20-40 seconds if server is sleeping)";

    try {
        const response = await fetch("https://ocr-api-opk6.onrender.com/scan", {
            method: "POST",
            body: formData
        });

        if (!response.ok) {
            throw new Error("Server error: " + response.status);
        }

        const data = await response.json();

        if (data && data.text) {
            output.innerText = data.text;
        } else {
            output.innerText = "No text extracted";
        }

    } catch (error) {
        console.error(error);

        output.innerText =
            "Error connecting to API.\n\n" +
            "Possible reasons:\n" +
            "- Server is sleeping\n" +
            "- Network issue\n" +
            "- Backend error\n\n" +
            "Try again.";
    }
}

// Drag & Drop support
const uploadBox = document.querySelector(".upload-box");

if (uploadBox) {
    uploadBox.addEventListener("dragover", (e) => {
        e.preventDefault();
        uploadBox.style.background = "#334155";
    });

    uploadBox.addEventListener("dragleave", () => {
        uploadBox.style.background = "";
    });

    uploadBox.addEventListener("drop", (e) => {
        e.preventDefault();
        uploadBox.style.background = "";

        const fileInput = document.getElementById("fileInput");
        fileInput.files = e.dataTransfer.files;
    });
}