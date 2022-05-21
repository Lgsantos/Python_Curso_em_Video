//Ex001
const subtitulo = document.createElement('h2');
const solucaoExercicio = document.createElement('p');
const exercicio = document.getElementById('ex001');

subtitulo.innerText = 'Ex. 001';
solucaoExercicio.innerText = 'Hello World!';

exercicio.appendChild(subtitulo);
exercicio.appendChild(solucaoExercicio);

//Ex002
const ex002 = document.getElementById('ex002');

function solucao002() {  
    const nameInput = document.getElementById('nameInput').value;
    const solucao002 = document.getElementById('solucao002');

    solucao002.innerText = `É um prazer te conhecer, ${nameInput}!`;
}

//Ex003


function solucao003() {
    document.getElementById('n1').click();
    document.getElementById('n2').click();
    const n1 = Number(document.getElementById('n1').value);
    const n2 = Number(document.getElementById('n2').value);
    const s = n1 + n2;
    document.getElementById('solucao003').innerText = `A soma de ${n1} e ${n2} é ${s}.`
}


