function inicializarGrafico(datos) {
    const ctx = document.getElementById('canvasGrafico').getContext('2d');
    
    // Dataset de la Región Factible (El área sombreada)
    const datasets = [
        {
            label: 'Región Factible',
            data: datos.poligono,
            showLine: true,
            backgroundColor: 'rgba(75, 192, 192, 0.3)',
            borderColor: 'rgba(75, 192, 192, 1)',
            pointRadius: 0, // Ocultamos los puntos para que se vea solo el área
            tension: 0
        }
    ];

    // Dataset del Punto Óptimo (El triángulo rojo)
    datasets.push({
        label: 'Punto Óptimo',
        data: [datos.optimo],
        pointRadius: 10,
        pointBackgroundColor: 'red',
        pointBorderColor: 'black',
        pointStyle: 'triangle'
    });

    // datasets de las Rectas de Restricción
    datos.rectas.forEach((puntos, index) => {
        datasets.push({
            label: `R${index + 1}`,
            data: puntos,
            showLine: true,
            fill: false,
            borderColor: `rgba(100, 100, 100, 0.5)`, // Color gris para las líneas
            borderWidth: 2,
            pointRadius: 0,
            borderDash: [5, 5] // Líneas punteadas
        });
    });

    new Chart(ctx, {
        type: 'scatter',
        data: { datasets: datasets },
        options: {
            scales: {
                x: { beginAtZero: true, title: { display: true, text: 'X' } },
                y: { beginAtZero: true, title: { display: true, text: 'Y' } }
            }
        }
    });
}