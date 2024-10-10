document.getElementById('classifyButton').addEventListener('click', function() {
    const comportamiento = document.getElementById('comportamiento').value;
    const entrenamiento = document.getElementById('entrenamiento').value;
    const ejercicio = document.getElementById('ejercicio').value;
    const comunicacion = document.getElementById('comunicacion').value;
    const habilidades = document.getElementById('habilidades').value;
    const cuidado = document.getElementById('cuidado').value;
    const tamano = document.getElementById('tamano').value;
    const cabeza = document.getElementById('cabeza').value;
    const vision = document.getElementById('vision').value;
    const pelaje = document.getElementById('pelaje').value;
    const orejas = document.getElementById('orejas').value;
    const cola = document.getElementById('cola').value;
    const mandibula = document.getElementById('mandibula').value;
    const movimiento = document.getElementById('movimiento').value;

    // Datos a enviar
    const data = {
        Comportamiento: comportamiento,
        Entrenamiento: entrenamiento,
        Ejercicio: ejercicio,
        Comunicacion: comunicacion,
        Habilidades: habilidades,
        Cuidado: cuidado,
        Tamaño: tamano,
        Cabeza: cabeza,
        Vision: vision,
        Pelaje: pelaje,
        Orejas: orejas,
        Cola: cola,
        Mandibula: mandibula,
        Movimiento: movimiento
    };

    // Llamada a la API
    fetch('untitled31.py', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(data => {
        const resultDiv = document.getElementById('result');
        resultDiv.innerHTML = `El animal clasificado es: ${data.resultado}`;
    })
    .catch(error => {
        console.error('Error:', error);
    });
});
