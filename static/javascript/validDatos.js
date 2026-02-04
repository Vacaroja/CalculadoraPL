document.getElementById('formRestricciones').addEventListener('submit', function(event) {
    const cantVar = document.getElementById('CantVar').value;
    const metodo = document.querySelector('input[name="metodo"]:checked').value;
    
    if (cantVar == "" || isNaN(cantVar) || parseInt(cantVar) < 2) {
        alert('Por favor, ingrese un número válido de variables mayor que 2.');
        event.preventDefault();
    }
    if (metodo == "grafico" && parseInt(cantVar) > 2) {
        alert('El método gráfico solo es aplicable para 2 variables.');
        event.preventDefault();
    }
    
});