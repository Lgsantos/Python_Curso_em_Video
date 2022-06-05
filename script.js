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

//Ex.008
function resolve008() {
    const medida = Number(document.getElementById('input008').value),
    c = medida * 100,
    m = medida * 1000;
    document.getElementById('solucao008').innerHTML = `${medida} metros equivale a ${c} centímetros e ${m} milímetros.`
}

//Ex. 009
function solucao009() {
    if (document.getElementById('solucao009').hasChildNodes()) {
        document.getElementById('solucao009').removeChild(document.getElementById('solucao009').firstChild);
    }

    const n = Number(document.getElementById('nEx009').value),
    lista = document.createElement('ul');

    for (let i=2; i<=10; i++) {
        item = document.createElement('li');
        item.innerHTML = `${n} x ${i} = ${n*i}`;
        lista.appendChild(item);
    }

    document.getElementById('solucao009').appendChild(lista);
}

//Ex. 010
function solucao010() {
    const input10 = document.getElementById('input010'),
    reais = Number(input10.value),
    dolares = Math.floor(reais / 5.01),
    cents = reais % 5.01;
    document.getElementById('solucao010').innerHTML = `Com ${reais} reai(s) você pode comprar ${dolares} dólar(es) e ${cents.toFixed(2)} centavo(s) de dólar. Cotação: US$ 1,00 = R$ 5,01`;
}

//Ex. 011
function solucao011() {
    const input11a = document.getElementById('input011a'),
    input11b = document.getElementById('input011b');
    input11a.click();
    input11b.click();
    const largura = Number(input11a.value),
    altura = Number(input11b.value),
    area = largura * altura,
    rendimento = 2,
    litros = area / rendimento;
    document.getElementById('solucao011').innerHTML = `Sua parede tem ${area} metros quadrados e são necessários ${litros} litros de tinta para pintá-la.`;
}

//Ex. 012
function solucao012() {
    const preco = Number(document.getElementById('input012').value),
    desconto = 5,
    precoFinal = preco * (1 - (desconto / 100));
    document.getElementById('solucao012').innerHTML = `O preço final do produto, com desconto de ${desconto}% é de ${precoFinal.toFixed(2)} reais.`
}

//Ex. 013
function solucao013() {
    const input13 = document.getElementById('input013'),
    salarioAtual = Number(input13.value),
    aumento = 15,
    salarioFinal = salarioAtual * (1 + aumento / 100);
    document.getElementById('solucao013').innerHTML = `O salário final, após aumento de ${aumento}% é de ${salarioFinal} reais.`;
}

//Ex. 014
function solucao014() {
    const input14 = document.getElementById('input014'),
    celsius = Number(input14.value),
    fahrenheit = celsius * (9/5) + 32
    document. getElementById('solucao014').innerHTML = `${celsius.toFixed(2)} graus Celsius correspondem a ${fahrenheit.toFixed(2)} graus Fahrenheit.`
}

//Ex. 015
function solucao015() {
    const input15a = document.getElementById('input015a'),
    input15b = document.getElementById('input015b'),
    dias = Number(input15a.value),
    km = Number(input15b.value),
    aluguel = dias * 60 + km * 0.15
    document.getElementById('solucao015').innerHTML = `O total a pagar pelo aluguel do carro é de R$ ${aluguel.toFixed(2)}`;
}

//Ex. 016
function solucao016() {
    const input16 = document.getElementById('input016').value,
    num = Number(input16);
    document.getElementById('solucao016').innerHTML = `A parte inteira de ${num.toFixed(3)} é ${Math.floor(num)}`;
}

//Ex. 017
function solucao017() {
    document.getElementById('input017a').click();
    document.getElementById('input017b').click();
    const input17a = document.getElementById('input017a').value,
    input17b = document.getElementById('input017b').value,
    cateto_oposto = Number(input17a),
    cateto_adjacente = Number(input17b),
    hipotenusa = Math.hypot(cateto_oposto, cateto_adjacente);
    document.getElementById('solucao017').innerHTML = `A hipotenusa desse triângulo é ${hipotenusa.toFixed(2)}`;
}

//Ex. 018
function solucao018() {
    const input18 = document.getElementById('input018').value,
    angulo = grausParaRadianos(+(input18)),
    seno = Math.sin(angulo).toFixed(2),
    cosseno = Math.cos(angulo).toFixed(2),
    tangente = Math.tan(angulo).toFixed(2);
    document.getElementById('solucao018').innerHTML = `Para o ângulo de ${input18} graus temos:<br>seno = ${seno}<br>cosseno = ${cosseno}<br>tangente = ${tangente}`;
}

function grausParaRadianos(g) {
    return ((g * (Math.PI)) / 180);
}

//Ex. 019
function solucao019() {
    const aluno01 = document.getElementById('input019a').value,
    aluno02 = document.getElementById('input019b').value,
    aluno03 = document.getElementById('input019c').value,
    aluno04 = document.getElementById('input019d').value,
    lista = [aluno01, aluno02, aluno03, aluno04],
    escolhido = lista[Math.floor(Math.random()*4)],
    listaEmbaralhada = lista.sort(() => Math.random() - 0.5);
    document.getElementById('solucao019').innerHTML = `O aluno escolhido para limpar o quadro negro foi ${escolhido}<br>${listaEmbaralhada}`;
}

//Ex. 020
function solucao020() {
    const aluno01 = document.getElementById('input020a').value,
    aluno02 = document.getElementById('input020b').value,
    aluno03 = document.getElementById('input020c').value,
    aluno04 = document.getElementById('input020d').value,
    lista = [aluno01, aluno02, aluno03, aluno04],
    listaEmbaralhada = lista.sort(() => Math.random() - 0.5);
    document.getElementById('solucao020').innerHTML = `A ordem dos alunos para limpar o quadro negro será ${listaEmbaralhada}`;
}

//Ex. 021 - Pode ser resolvido apenas com o html5

//Ex. 022
function solucao022() {
    const nome = (document.querySelector('#input022').value).trim(),
    nomeUpper = nome.toUpperCase(),
    nomeLower = nome.toLowerCase(),
    nomeLen = nome.replaceAll(' ', '').length,
    prenome = nome.split(' ')[0];
    document.querySelector('#solucao022').innerHTML = `Seu nome em MAIÚSCULAS: ${nomeUpper}<br>
    Seu nome em minúsculas: ${nomeLower}<br>
    Há ${nomeLen} letras em seu nome<br>
    E seu prenome é ${prenome}`;
}

//Ex. 023
function solucao023() {
    const input23 = Number(document.querySelector('#input023').value),
    u = Math.floor(input23 / 1 % 10),
    d = Math.floor(input23 / 10 % 10),
    c = Math.floor(input23 / 100 % 10),
    m = Math.floor(input23 / 1000);
    document.querySelector('#solucao023').innerHTML = `Unidade(s): ${u}<br>
    Dezena(s): ${d}<br>
    Centena(s): ${c}<br>
    Milhar(es): ${m}`;
}

//Ex. 024
function solucao024() {
    const cidade = document.querySelector('#input024').value.trim().toUpperCase();
    document.querySelector('#solucao024').innerHTML =
    `${cidade} começa com "SANTO"? 
    ${cidade.startsWith('SANTO').toString().toUpperCase()}`;
}

//Ex. 025
function solucao025() {
    const nome = document.querySelector('#input025').value.trim().toUpperCase();
    document.querySelector('#solucao025').innerHTML = `Seu nome tem "Silva"? ${nome.includes('SILVA').toString().toUpperCase()}`;
}

//Ex. 026
function solucao026() {
    const frase = document.querySelector('#input026').value.trim().toUpperCase(), fraseArray = frase.split('A'),
    n = 0;
    document.querySelector('#solucao026').innerHTML = `A letra "A" aparece ${fraseArray.length - 1} nessa frase.<br>A letra "A" aparece pela primeira vez na posição: ${frase.indexOf('A')}.<br>A letra "A" aparece pela última vez na posição: ${frase.length - fraseArray[(fraseArray.length-1)].length - 1}.`;
}

//Ex. 027
function solucao027() {
    const nome = document.querySelector('#input027').value.trim().split(' ');
    document.querySelector('#solucao027').innerHTML = `Seu primeiro nome é ${nome[0]}.<br>Seu último nome é ${nome[nome.length - 1]}.`;
}
//Funções para mostrar grupos de exercícios

function mostra1_4() {
    document.getElementById('ex1ate4').style.display = 'block';
}
function esconder1ate4() {
    document.getElementById('ex1ate4').style.display = 'none';
}

function mostra5_8() {
    document.getElementById('ex5ate8').style.display = 'block';
}
function esconder5ate8() {
    document.getElementById('ex5ate8').style.display = 'none';
}

function mostra9_12() {
    document.getElementById('ex9ate12').style.display = 'block';
}
function esconder9ate12() {
    document.getElementById('ex9ate12').style.display = 'none';
}

function mostra13_16() {
    document.getElementById('ex13ate16').style.display = 'block';
}
function esconder13ate16() {
    document.getElementById('ex13ate16').style.display = 'none';
}

function mostra17_20() {
    document.getElementById('ex17ate20').style.display = 'block';
}
function esconder17ate20() {
    document.getElementById('ex17ate20').style.display = 'none';
}

function mostra21_24() {
    document.getElementById('ex21ate24').style.display = 'block';
}
function esconder21ate24() {
    document.getElementById('ex21ate24').style.display = 'none';
}