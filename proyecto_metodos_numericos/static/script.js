document.getElementById('numeric-methods-form').onsubmit = function(e) {
    e.preventDefault();
    
    let form = e.target;
    let formData = new FormData(form);

    fetch('/', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            alert(data.error);
        } else {
            // Update the page with results, graphs, and comparison
            document.getElementById('results').innerHTML = data;
        }
    })
    .catch(error => console.error('Error:', error));
};
