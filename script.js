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

//Ex004
function solucao004() {
    const algo = document.getElementById('algo').value;
    if(algo != '') {
        const conteudo = [];
        
        conteudo.push(document.createTextNode(`${algo} é do tipo ${typeof(algo)}`));
        stringEval(algo, conteudo);
    } else {
        const divSolucao004 = document.getElementById('solucao004');
    if(divSolucao004.hasChildNodes()) {
        divSolucao004.removeChild(divSolucao004.lastElementChild);
    }
    }
    
}

function stringEval(a, conteudo) {
    const divSolucao004 = document.getElementById('solucao004');
    if(divSolucao004.hasChildNodes()) {
        divSolucao004.removeChild(divSolucao004.lastElementChild);
    }
    const lista = document.createElement('ul');
    //if 'a' is just a string
    conteudo.push(document.createTextNode(`${a} tem tamanho de ${a.length} caracteres`));

    //Tests if 'a' can be converted to a number
    const aNumber = Number(a);
    if(!Number.isNaN(aNumber)) {
        conteudo.push(document.createTextNode(`A string '${a}' pode ser convertida no número ${aNumber}`));
        conteudo.push(document.createTextNode(`${a} é NaN? ${Number.isNaN(aNumber)}`));
        conteudo.push(document.createTextNode(`${a} é finito? ${Number.isFinite(aNumber)}`));
        conteudo.push(document.createTextNode(`${a} é inteiro? ${Number.isInteger(aNumber)}`));
        conteudo.push(document.createTextNode(`${a} é um inteiro seguro? ${Number.isSafeInteger(aNumber)}`));
    }

    //Generate the list of 'properties' of 'a'
    for (const i of conteudo) {
        console.log(i);
        const item = document.createElement('li');
        item.appendChild(i);
        lista.appendChild(item);
        divSolucao004.appendChild(lista); 
    }
}

//
function solucao005() {
    const divSolucao005 = document.getElementById('solucao005'),
    nInput = document.getElementById("nEx005").value;
    if (divSolucao005.hasChildNodes()) {
        divSolucao005.removeChild(divSolucao005.lastChild);
    }
    const n = Number(nInput),
    lista = document.createElement('ul'),
    item1 = document.createElement('li'),
    item2 = document.createElement('li'),
    a = n - 1,
    s = n + 1;
    item1.appendChild(document.createTextNode(`O antecessor de ${n} é ${a}`));
    item2.appendChild(document.createTextNode(`O sucesor de ${n} é ${s}`));
    lista.append(item1, item2);
    divSolucao005.appendChild(lista);
}
