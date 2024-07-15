const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.question('Por favor, introduce los valores de a y b separados por un espacio: ', (input) => {
    const [a, b] = input.trim().split(' ').map(Number);

    let maxContador = 0;

    for (let num = b; num >= a; num--) {
        let contador = 1;
        let aux2 = num;

        while (aux2 !== 1) {
            if (aux2 % 2 === 0) {
                aux2 /= 2;
            } else {
                aux2 = aux2 * 3 + 1;
            }
            contador++;
        }

        if (contador > maxContador) {
            maxContador = contador;
        }
    }

    console.log(`El máximo contador es: ${maxContador}`);
    rl.close();
});