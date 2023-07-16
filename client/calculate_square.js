function calculateSquare() {
    const number = document.getElementById('number').value;

    const url = `/api/v1/calculate_square?number=${number}&operator=**`;

    fetch(url)
        .then(response => response.json())
        .then(data => {
            const result = data.result;
            document.getElementById('result').textContent = `Result: ${result}`;
        })
        .catch(error => {
            console.error('Error:', error);
        });
}