function triggerUpload() {
document.getElementById("fileInput").click();
}

function copyText() {
const text = document.getElementById("output").innerText;
navigator.clipboard.writeText(text);
alert("Copied!");
}

async function uploadFile() {
const fileInput = document.getElementById("fileInput");
const output = document.getElementById("output");


if (!fileInput.files.length) {
    alert("Please select a file");
    return;
}

const formData = new FormData();
formData.append("file", fileInput.files[0]);

output.innerText = "⏳ Processing...";

try {
    const response = await fetch("http://localhost:8001/scan", {
        method: "POST",
        body: formData
    });

    if (!response.ok) throw new Error("Server error");

    const data = await response.json();

    output.innerText = data.text || "❌ No text extracted";

} catch (error) {
    output.innerText = "❌ API Error. Check backend.";
}


}
