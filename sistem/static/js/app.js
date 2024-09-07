// static/js/app.js

document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('solveForm');
    const functionInput = document.getElementById('function');
    const functionPreview = document.getElementById('function_preview');

    functionInput.addEventListener('input', function() {
        functionPreview.textContent = functionInput.value;
    });

    form.addEventListener('submit', function(event) {
        event.preventDefault();
        const formData = new FormData(form);

        fetch('/solve', {
            method: 'POST',
            body: formData
        })
        .then(response => response.text())
        .then(data => {
            document.open();
            document.write(data);
            document.close();
        })
        .catch(error => console.error('Error:', error));
    });
});
