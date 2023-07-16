function calculate() {
        const first_operand = document.getElementById('first_operand').value;
        const second_operand = document.getElementById('second_operand').value;
        const operator = document.getElementById('operator').value;

        const url = `/api/v1/calculate?first_operand=${first_operand}&second_operand=${second_operand}&operator=${operator}`;

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