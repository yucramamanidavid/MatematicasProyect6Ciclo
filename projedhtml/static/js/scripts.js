document.addEventListener('DOMContentLoaded', function() {
    updateForm(); // Cargar el formulario por defecto

    // Validar el formulario principal antes de enviarlo
    document.getElementById('methodForm').addEventListener('submit', function(event) {
        const method = document.getElementById('method').value;
        const functionInput = document.getElementById('function').value;
        if (!functionInput) {
            alert('La función es un campo obligatorio.');
            event.preventDefault();
        }
    });

    // Actualizar el formulario según el tipo de comparación
    document.getElementById('compareForm').addEventListener('submit', function(event) {
        const compareType = document.getElementById('compareType').value;
        if (compareType === 'hybrid') {
            const method1 = document.getElementById('method1').value;
            const method2 = document.getElementById('method2').value;
            if (!method1 || !method2) {
                alert('Por favor, selecciona dos métodos híbridos para comparar.');
                event.preventDefault();
            }
        }
    });
});

function updateForm() {
    const method = document.getElementById("method").value;
    let formHtml = "";

    switch (method) {
        case "bisection":
            formHtml = `
                <label for="function">Función (en términos de x):</label>
                <input type="text" id="function" name="function" required>
                <label for="a">Valor de a:</label>
                <input type="number" id="a" name="a" required>
                <label for="b">Valor de b:</label>
                <input type="number" id="b" name="b" required>
                <label for="tolerance">Tolerancia:</label>
                <input type="number" id="tolerance" name="tolerance" step="0.00001" required>
                <label for="maxIterations">Número máximo de iteraciones:</label>
                <input type="number" id="maxIterations" name="maxIterations" required>
            `;
            break;
        case "falsePosition":
            formHtml = `
                <label for="function">Función (en términos de x):</label>
                <input type="text" id="function" name="function" required>
                <label for="a">Valor de a:</label>
                <input type="number" id="a" name="a" required>
                <label for="b">Valor de b:</label>
                <input type="number" id="b" name="b" required>
                <label for="tolerance">Tolerancia:</label>
                <input type="number" id="tolerance" name="tolerance" step="0.00001" required>
                <label for="maxIterations">Número máximo de iteraciones:</label>
                <input type="number" id="maxIterations" name="maxIterations" required>
            `;
            break;
        case "newtonRaphson":
            formHtml = `
                <label for="function">Función (en términos de x):</label>
                <input type="text" id="function" name="function" required>
                <label for="x0">Valor inicial x<sub>0</sub>:</label>
                <input type="number" id="x0" name="x0" required>
                <label for="tolerance">Tolerancia:</label>
                <input type="number" id="tolerance" name="tolerance" step="0.00001" required>
                <label for="maxIterations">Número máximo de iteraciones:</label>
                <input type="number" id="maxIterations" name="maxIterations" required>
            `;
            break;
        case "secant":
            formHtml = `
                <label for="function">Función (en términos de x):</label>
                <input type="text" id="function" name="function" required>
                <label for="x0">Valor inicial x<sub>0</sub>:</label>
                <input type="number" id="x0" name="x0" required>
                <label for="x1">Valor inicial x<sub>1</sub>:</label>
                <input type="number" id="x1" name="x1" required>
                <label for="tolerance">Tolerancia:</label>
                <input type="number" id="tolerance" name="tolerance" step="0.00001" required>
                <label for="maxIterations">Número máximo de iteraciones:</label>
                <input type="number" id="maxIterations" name="maxIterations" required>
            `;
            break;
        case "fixedPoint":
            formHtml = `
                <label for="function">Función (en términos de x):</label>
                <input type="text" id="function" name="function" required>
                <label for="x0">Valor inicial x<sub>0</sub>:</label>
                <input type="number" id="x0" name="x0" required>
                <label for="tolerance">Tolerancia:</label>
                <input type="number" id="tolerance" name="tolerance" step="0.00001" required>
                <label for="maxIterations">Número máximo de iteraciones:</label>
                <input type="number" id="maxIterations" name="maxIterations" required>
            `;
            break;
        case "hybridBisectionFalsePosition":
            formHtml = `
                <label for="function">Función (en términos de x):</label>
                <input type="text" id="function" name="function" required>
                <label for="a">Valor de a:</label>
                <input type="number" id="a" name="a" required>
                <label for="b">Valor de b:</label>
                <input type="number" id="b" name="b" required>
                <label for="tolerance">Tolerancia:</label>
                <input type="number" id="tolerance" name="tolerance" step="0.00001" required>
                <label for="maxIterations">Número máximo de iteraciones:</label>
                <input type="number" id="maxIterations" name="maxIterations" required>
            `;
            break;
        case "hybridNewtonSecantFixedPoint":
            formHtml = `
                <label for="function">Función (en términos de x):</label>
                <input type="text" id="function" name="function" required>
                <label for="x0">Valor inicial x<sub>0</sub>:</label>
                <input type="number" id="x0" name="x0" required>
                <label for="tolerance">Tolerancia:</label>
                <input type="number" id="tolerance" name="tolerance" step="0.00001" required>
                <label for="maxIterations">Número máximo de iteraciones:</label>
                <input type="number" id="maxIterations" name="maxIterations" required>
            `;
            break;
        default:
            formHtml = "";
    }

    document.getElementById("formContainer").innerHTML = formHtml;
}

function updateCompareForm() {
    const compareType = document.getElementById("compareType").value;
    let compareFormHtml = "";

    if (compareType === "hybrid") {
        compareFormHtml = `
            <label for="method1">Selecciona el primer método híbrido:</label>
            <select id="method1" name="method1">
                <option value="hybridBisectionFalsePosition">Híbrido Bisección y Falsa Posición</option>
                <option value="hybridNewtonSecantFixedPoint">Híbrido Newton-Raphson, Secante y Punto Fijo</option>
            </select>
            <label for="method2">Selecciona el segundo método híbrido:</label>
            <select id="method2" name="method2">
                <option value="hybridBisectionFalsePosition">Híbrido Bisección y Falsa Posición</option>
                <option value="hybridNewtonSecantFixedPoint">Híbrido Newton-Raphson, Secante y Punto Fijo</option>
            </select>
        `;
    }

    document.getElementById("compareFormContainer").innerHTML = compareFormHtml;
}
