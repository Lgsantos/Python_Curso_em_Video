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

//Ex.005
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

//Ex.006

function solucao006() {
    const n = Number(document.getElementById('input006').value),
    dobro = n * 2,
    triplo = n * 3,
    raiz = Math.sqrt(n),
    divSolucao006 = document.getElementById('solucao006'),
    lista = document.createElement('ul'),
    item1 = document.createElement('li'),
    item2 = document.createElement('li'),
    item3 = document.createElement('li');
    item1.appendChild(document.createTextNode(`O dobro de ${n} é ${dobro}`));
    item2.appendChild(document.createTextNode(`O triplo de ${n} é ${triplo}`));
    item3.appendChild(document.createTextNode(`A raiz de ${n} é ${raiz.toFixed(2)}`));
    lista.append(item1, item2, item3);
    if (divSolucao006.hasChildNodes()) {
        divSolucao006.removeChild(divSolucao006.firstChild);
    }
    divSolucao006.appendChild(lista);
}

//Ex. 007
function resolve007() {
    document.getElementById('input007a').click();
    document.getElementById('input007b').click();
    const nota1 = Number(document.getElementById('input007a').value), nota2 = Number(document.getElementById('input007b').value),
    media = (nota1 + nota2) / 2;
    document.getElementById('solucao007').innerHTML = `A média das notas do aluno é ${media.toFixed(2)}`;
}

function mostra1_4() {
    document.getElementById('ex1ate4').style.display = 'block';
}

function mostra5_8() {
    document.getElementById('ex5ate8').style.display = 'block';
}
