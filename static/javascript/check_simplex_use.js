document.getElementById('form-restricciones').addEventListener('submit', function(event) {
    const igualdad = document.querySelectorAll('select[name="igualdades[]"]');
    const metodo = document.querySelector('input[name="metodo"]').value;
    console.log(igualdad)
    console.log(metodo)

    const todosmenorigual = Array.from(igualdad).every(igualdad => igualdad.value == "<=");
    if (!todosmenorigual && metodo === "simplex"){
        event.preventDefault();
        alert("Metodo Simplex solo permite reestricciones con <=")
    }
    
});