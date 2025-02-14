function calcularAmor() {
    let nombre1 = document.getElementById("nombre1").value.trim();
    let nombre2 = document.getElementById("nombre2").value.trim();
    let resultadoDiv = document.getElementById("resultado");

    if (nombre1 === "" || nombre2 === "") {
        resultadoDiv.innerHTML = "<p style='color:red;'>❌ Ingresa ambos nombres.</p>";
        return;
    }

    fetch("/calcular", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ nombre1: nombre1, nombre2: nombre2 })
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            resultadoDiv.innerHTML = `<p style='color:red;'>${data.error}</p>`;
        } else {
            resultadoDiv.innerHTML = `<p>💑 ${data.nombre1} y ${data.nombre2} tienen un <strong>${data.porcentaje}%</strong> de compatibilidad 💞</p>`;
        }
    })
    .catch(error => console.error("Error:", error));
}
//try