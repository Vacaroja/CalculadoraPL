function inicializarGrafico(datos) {
    const ctx = document.getElementById('canvasGrafico').getContext('2d');
    
    new Chart(ctx, {
        type: 'scatter',
        data: {
            datasets: [
                {
                    label: 'Región Factible',
                    data: datos.poligono,
                    showLine: true,
                    fill: true,
                    backgroundColor: 'rgba(75, 192, 192, 0.4)',
                    borderColor: 'rgba(75, 192, 192, 1)',
                    pointRadius: 4,
                    tension: 0
                },
                {
                    label: 'Punto Óptimo',
                    data: [datos.optimo],
                    pointRadius: 10,
                    pointBackgroundColor: 'red',
                    pointBorderColor: 'black',
                    pointStyle: 'triangle'
                }
            ]
        },
        options: {
            responsive: true,
            scales: {
                x: { 
                    title: { display: true, text: 'Variable X1' },
                    beginAtZero: true 
                },
                y: { 
                    title: { display: true, text: 'Variable X2' },
                    beginAtZero: true 
                }
            },
            plugins: {
                tooltip: {
                    callbacks: {
                        label: function(context) {
                            return `X: ${context.raw.x}, Y: ${context.raw.y}`;
                        }
                    }
                }
            }
        }
    });
}