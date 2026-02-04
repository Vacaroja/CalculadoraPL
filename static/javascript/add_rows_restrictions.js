function addRestrictionRow() {
    const contenedor = document.getElementById('contenedor-restricciones');
    const fila = document.getElementsByClassName('fila-restriccion');

    const nuevaFila = fila[0].cloneNode(true);

    const inputs = nuevaFila.querySelectorAll('input');
    inputs.forEach(input => {
        input.value = ""; // Borra el número que haya escrito el usuario
    });
    
    if (fila.length >= 1) {
        const btnEliminar = document.createElement('button');
        btnEliminar.innerHTML = "✕";
        btnEliminar.className = "ml-2 text-red-500 font-bold hover:text-red-700";
        btnEliminar.type = "button";
        btnEliminar.onclick = function() { nuevaFila.remove(); };
        nuevaFila.appendChild(btnEliminar);
    }

    // 5. Insertar la fila en el DOM
    contenedor.appendChild(nuevaFila);
}

    