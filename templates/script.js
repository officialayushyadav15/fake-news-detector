const urlTabBtn = document.getElementById("tab-url");
const textTabBtn = document.getElementById("tab-text");
const urlInputContainer = document.getElementById("url-input-container");
const textInputContainer = document.getElementById("text-input-container");
const analyzeBtn = document.getElementById("analyze-btn");
const urlInput = document.getElementById("url-input");
const textInput = document.getElementById("text-input");
const loadingDiv = document.getElementById("loading");
const resultDiv = document.getElementById("result");
const errorDiv = document.getElementById("error");
const progressContainer = document.getElementById("progress-container");
const progressBar = document.getElementById("progress-bar");
const progressText = document.getElementById("progress-text");

// Set default tab to URL Analysis
let activeTab = "url";

// Tab switching logic
urlTabBtn.addEventListener("click", () => switchTab("url"));
textTabBtn.addEventListener("click", () => switchTab("text"));

// Updated switchTab() function with optimizations
function switchTab(tab) {
    // Deactivate both tabs
    [urlTabBtn, textTabBtn].forEach((btn) => btn.classList.remove("active"));

    // Activate selected tab and show the respective section
    if (tab === "url") {
        urlTabBtn.classList.add("active");
        showSection("url-section");
        activeTab = "url";
    } else {
        textTabBtn.classList.add("active");
        showSection("text-section");
        activeTab = "text";
    }
}

// Show section dynamically
function showSection(sectionId) {
    document.getElementById("text-section").style.display = "none";
    document.getElementById("url-section").style.display = "none";
    document.getElementById(sectionId).style.display = "block";
}

// Analyze button event listener
analyzeBtn.addEventListener("click", async () => {
    resetUI(); // Reset UI before new analysis

    if (activeTab === "url") {
        await analyzeURL();
    } else {
        await analyzeText();
    }
});

// Analyze text
async function analyzeText() {
    const text = textInput.value.trim();
    if (!text) {
        showError("Please enter some text for analysis.");
        return;
    }

    try {
        const response = await fetch("/predict", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ text }),
        });

        const result = await handleResponse(response);
        const verificationPercentage = calculateConfidence(result);
        displayResult(result, verificationPercentage);
    } catch (error) {
        showError(error.message);
    }
}

// Analyze URL
async function analyzeURL() {
    const url = urlInput.value.trim();
    if (!url || !isValidURL(url)) {
        showError("Please enter a valid URL.");
        return;
    }

    try {
        const response = await fetch("/analyze", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ url }),
        });

        const result = await handleResponse(response);
        const verificationPercentage = calculateConfidence(result);
        displayResult(result, verificationPercentage);
    } catch (error) {
        showError(error.message);
    }
}

// Validate URL with a stricter regex pattern
function isValidURL(string) {
    const urlPattern = /^(https?:\/\/)?(www\.)?[\w-]+(\.[\w-]+)+([\w.,@?^=%&:/~+#-]*[\w@?^=%&/~+#-])?$/;
    return urlPattern.test(string);
}

// Handle API response
async function handleResponse(response) {
    const result = await response.json();
    if (!response.ok) {
        throw new Error(result.error || "Something went wrong!");
    }
    return result;
}

// Display result with progress bar
// Display result inside "Verification Ready" block
function displayResult(result, verificationPercentage) {
    resultDiv.innerHTML = `
        <div class="text-center space-y-2">
            <div class="text-2xl font-bold ${
                result.isFake ? "text-red-400" : "text-green-400"
            }">
                ${result.isFake ? "⚠️ Fake News Detected" : "✅ Content is Legitimate"}
            </div>
            <p class="text-sm text-gray-400">
                ${result.details || "Analysis complete. Check the report for more insights."}
            </p>
        </div>
    `;
    resultDiv.classList.remove("hidden");
    loadingDiv.classList.add("hidden"); // Hide loading after result

    showProgress(verificationPercentage); // Display progress bar if applicable
}


// Show progress with smooth animation
function showProgress(percentage) {
    const radius = 58;
    const circumference = 2 * Math.PI * radius;
    const offset = circumference - (percentage / 100) * circumference;

    // Smooth transition for progress bar
    progressBar.style.transition = "stroke-dashoffset 0.5s ease-in-out";
    progressBar.style.strokeDashoffset = offset;
    progressText.innerText = `${percentage}%`;

    progressContainer.style.display = "block";
}

// Simulate confidence score calculation based on result
function calculateConfidence(result) {
    return result.isFake
        ? Math.floor(Math.random() * 30) + 50 // 50% - 80% for fake
        : Math.floor(Math.random() * 20) + 80; // 80% - 100% for legitimate
}

// Show error message with improved UX
function showError(message) {
    errorDiv.innerText = message;
    errorDiv.classList.remove("hidden");
    loadingDiv.classList.add("hidden");
}

// Reset UI before each analysis
function resetUI() {
    errorDiv.classList.add("hidden");
    resultDiv.classList.add("hidden");
    loadingDiv.classList.remove("hidden");
    progressContainer.style.display = "none"; // Hide progress initially
}
