async function getRecommendations() {
    const movie = document.getElementById("movieInput").value;

    const response = await fetch("http://127.0.0.1:5000/recommend", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ movie: movie })
    });

    const data = await response.json();

    const resultDiv = document.getElementById("results");
    resultDiv.innerHTML = "";

    if (data.recommendations.length === 0) {
        resultDiv.innerHTML = "No recommendations found";
    } else {
        data.recommendations.forEach(m => {
            const p = document.createElement("p");
            p.textContent = m;
            resultDiv.appendChild(p);
        });
    }
}