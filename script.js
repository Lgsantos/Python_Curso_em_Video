//Ex001
const subtitulo = document.createElement('h2'),
solucaoExercicio = document.createElement('p'),
exercicio = document.getElementById('ex001');

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
    solucao('solucao024', `${cidade} começa com "SANTO"? 
    ${cidade.startsWith('SANTO').toString().toUpperCase()}`);
}

//Ex. 025
function solucao025() {
    const nome = input('input025').trim().toUpperCase();
    solucao('solucao025', `Seu nome tem "Silva"? ${nome.includes('SILVA').toString().toUpperCase()}`);
}

//Ex. 026
function solucao026() {
    const frase = input('input026').trim().toUpperCase(), fraseArray = frase.split('A'),
    n = 0;
    solucao('solucao026', `A letra "A" aparece ${fraseArray.length - 1} nessa frase.<br>A letra "A" aparece pela primeira vez na posição: ${frase.indexOf('A')}.<br>A letra "A" aparece pela última vez na posição: ${frase.length - fraseArray[(fraseArray.length-1)].length - 1}.`);
}

//Ex. 027
function solucao027() {
    const nome = input('input027').trim().split(' ');
    solucao('solucao027', `Seu primeiro nome é ${nome[0]}.<br>Seu último nome é ${nome[nome.length - 1]}.`);
}

//Ex. 028
function solucao028() {
    const n = Math.floor(Math.random() * 5.9),
    num = Number(input('input028'));
    solucao('solucao028', (num == n ? 'Você acertou!' : 'Você errou!'));
}
//Ex. 029
function solucao029() {
    const vel = Number(input('input029'));
    solucao('solucao029', 
            vel > 80? `Você foi multado em ${(vel-80)*7} reais.` : `Você respeita o limite de velocidade. Parabéns!`);
}

//Ex. 030 - Desafio Extra que vi no instagram em 07_06_2022: somar os dois menores números de uma matriz dada
function solucao030() {
    const matriz = input('input030').split(',').map(x => Number(x)).sort((a, b) => a - b);
    console.log(matriz[0]+matriz[1]);
}

//Ex. 030a - O exercício original do Curso em Vídeo
function solucao030a() {
    const num = Number(input('input030a'));
    solucao('solucao030a', 
            num % 2 == 0? `${num} é par.` : `${num} é ímpar.`);
}

//Ex. 031
function solucao031() {
    const km = Number(input('input031'));
    solucao('solucao031',
            km <= 200? `O preço da passagem será ${km*0.50} reais` :
            `O preço da passagem será ${km*0.45} reais`);
}

//Ex. 032
function solucao032() {
    const ano = Number(input('input032')),
    anoAtual = new Date();
    let texto = ``;
    ano == 0?
     texto = `${anoAtual.getFullYear()}` :
     (ano % 4 == 0 & ano % 100 != 0 | 
     ano % 400 == 0)?
        texto = `${ano} é bissexto`:
        texto = `${ano} não é bissexto`;
    solucao('solucao032', texto);
}
//Ex. 033
function solucao033() {
    const n1 = Number(input('input033a')), n2 = Number(input('input033b')), n3 = Number(input('input033c')), vetor = [n1, n2, n3];
    vetor.sort((a,b) => a - b);
    solucao('solucao033', `${vetor[0]} é o menor valor,<br>${vetor[2]} é o maior valor`);
    alert(`${vetor[0]} é o menor valor,\n${vetor[2]} é o maior valor`);
}
//Ex. 034
function solucao034() {
    const salario = Number(input('input034'));
    solucao('solucao034',
        salario > 1250?
        `Aumento será ${salario*10/100} reais`:
        `Aumento será ${salario*15/100} reais`);
}
//Ex. 035
function solucao035() {
    const r1 = Number(input('input035a')),
        r2 = Number(input('input035b')),
        r3 = Number(input('input035c'));
    let resultado = '';
    if(Math.abs(r2-r3) < r1 & r1 < (r2+r3)){
        if(Math.abs(r1-r3) < r2 & r2 < (r1+r3)){
            if(Math.abs(r1-r2) < r3 & r3 < (r1+r2)){
                resultado = `${r1}, ${r2} e ${r3} formam um triângulo`;
            } else {
                resultado = `${r1}, ${r2} e ${r3} não formam um triângulo`;
            };
        } else {
            resultado = `${r1}, ${r2} e ${r3} não formam um triângulo`;
        };
    } else {
        resultado = `${r1}, ${r2} e ${r3} não formam um triângulo`;
    };
    solucao('solucao035', resultado);
}

//Ex. 036
function solucao036() {
    const casa = Number(input('input036a')),
    salario = Number(input('input036b')),
    anos = Number(input('input036c'));
    let prestacao = casa / (anos * 12),
    texto = '';
    prestacao <= salario * 30/100?
        texto = `Sua prestação será de R$${prestacao.toFixed(2)}`:
        texto = 'Não poderemos lhe fazer um empréstimo.';
    solucao('solucao036', texto);
}

//Ex. 037
function solucao037(event) {
    const form = document.querySelector('.formEx037'),
    data = new FormData(form);
    let output = '';
    for (const entry of data) {
        output = entry[1];
      };
      switch (output) {
        case '1': 
            solucao('solucao037', `${input037.value} escrito em formato binário é ${Number(input037.value).toString(2)}`);
            break;
        case '2':
            solucao('solucao037', `${input037.value} escrito em formato octagonal é ${Number(input037.value).toString(8)}`);
            break;
        case '3':
            solucao('solucao037', `${input037.value} escrito em formato hexagonal é ${Number(input037.value).toString(16)}`);
            break;
            default:
                solucao('solucao037', 'Número inválido!');
      }
}

//Ex. 038
function solucao038() {
    const n1 = Number(input('input038a')), n2 = Number(input('input038b'));
    // n1 > n2? solucao('solucao038', `${n1} é maior que ${n2}`):
    // n1 < n2? solucao('solucao038', `${n2} é maior que ${n1}`):
    // solucao('solucao038', `${n1} é igual a ${n2}`);
    if (n1 > n2) {
        solucao('solucao038', `${n1} é maior que ${n2}`);
    } else if (n2 > n1) {
        solucao('solucao038', `${n2} é maior que ${n1}`);
    } else {
        solucao('solucao038', `${n1} é igual a ${n2}`);
    }
}

//Ex. 039
function solucao039() {
    const anoNascimento = Number(input('input039')),
    dataAtual = new Date(), anoAtual = dataAtual.getFullYear(), idade = anoAtual - anoNascimento;
    if (idade < 18) {
        solucao('solucao039', `Você ainda não precisa se alistar. Faltam ${18 - idade} anos.`);
    } else if (idade == 18) {
        solucao('solucao039', 'Você precisa se alistar esse ano!');
    } else {
        solucao('solucao039', `Você já passou ${idade - 18} anos do tempo do alistamento.`);
    }   
}

//Ex. 040
function solucao040(event) {
    const n1 = Number(event.target[0].value), n2 = Number(event.target[1].value),
    media = (n1+n2)/2;
    if (media < 5) {
        solucao('solucao040', `A média do aluno é ${media.toFixed(1)} e ele foi reprovado.`);
    } else if (media >= 5 & media <= 6.9) {
        solucao('solucao040', `A média do aluno é ${media.toFixed(1)} e ele está de recuperação.`);
    } else {
        solucao('solucao040', `A média do aluno é ${media.toFixed(1)} e ele está aprovado.`);
    }
}

//Ex. 041
function solucao041() {
    const anoNascimento = Number(input('input041')), data = new Date(),
    anoAtual = data.getFullYear(),
    idade = anoAtual - anoNascimento;
    if (idade<=7) {
        solucao('solucao041', 'A categoria do atleta é MIRIM.');
    } else if (idade<=13) {
        solucao('solucao041', 'A categoria do atleta é INFANTIL');
    } else if (idade<=18) {
        solucao('solucao041', 'A categoria do atleta é JUNIOR.');
    } else if (idade<=30) {
        solucao('solucao041', 'A categoria do atleta é SÊNIOR.');
    } else {
        solucao('solucao041', 'A categoria do atleta é MASTER.');
    }
}

//Ex. 042
function solucao042() {
    const r1 = Number(input('input042a')), r2 = Number(input('input042b')), r3 = Number(input('input042c'));
    if (Math.abs(r2-r3) < r1 && r1 < (r2+r3)) {
        if (Math.abs(r1-r3) < r2 && r2 < (r1+r3)) {
            if (Math.abs(r1-r2) < r3 && r3 < (r1+r2)) {
                if (r1==r2 & r1==r3) {
                    solucao('solucao042', `${r1}, ${r2} e ${r3} formam um triângulo.<br>
                    O triângulo formado é equilátero.`);
                } else if ((r1 == r2 & r1 != r3) | (r3 == r2 & r3 != r1)) {
                    solucao('solucao042', `${r1}, ${r2} e ${r3} formam um triângulo.<br>
                    O triângulo formado é isósceles.`);
                } else {
                    solucao('solucao042', `${r1}, ${r2} e ${r3} formam um triângulo.<br>
                    O triângulo formado é escaleno.`);
                }
            } else {
                solucao('solucao042', `${r1}, ${r2} e ${r3} não formam um triângulo.`);
            }
        } else {
            solucao('solucao042', `${r1}, ${r2} e ${r3} não formam um triângulo.`);
        }
    } else {
        solucao('solucao042', `${r1}, ${r2} e ${r3} não formam um triângulo.`);
    }
}

//Ex. 043
function solucao043() {
    const altura = input('input043a'), peso = input('input043b'),
    imc = peso / altura ** 2;
    if (imc < 18.5) {
        solucao('solucao043', `Seu IMC é ${imc.toFixed(1)} você está ABAIXO DO PESO.`);
    } else if (imc < 25) {
        solucao('solucao043', `Seu IMC é ${imc.toFixed(1)} você está no PESO IDEAL.`);
    } else if (imc < 30) {
        solucao('solucao043', `Seu IMC é ${imc.toFixed(1)} você está com OBESIDADE.`);
    } else {
        solucao('solucao043', `Seu IMC é ${imc.toFixed(1)} Você está com OBESIDADE MÓRBIA.`);
    }
}

//Ex. 044
function solucao044(e) {
    let radio, normal = e.target[0].value;
    for (let i = 2; i < 6; i++) {
        if (e.target[i].checked) {
            radio = e.target[i].value;
            switch (radio) {
                case '1':
                    solucao('solucao044', `O preço final do produto é ${normal * 90/100}`);
                    break;
                case '2':
                    solucao('solucao044', `O preço final do produto é ${normal * 95/100}`);
                    break;
                case '3':
                    solucao('solucao044', `O preço final do produto é ${normal}`);
                break;
                case '4':
                    solucao('solucao044', `O preço final do produto é ${normal * 120/100}`);
                break;
            }
            break;
        }
    }
}

//Ex. 045
function solucao045(e) {
    let escolha = '',
    opcoes = ['pedra', 'papel', 'tesoura'],
    escolhaCPU = opcoes[Math.floor(Math.random()*3)];

    solucao('solucao045', ' ');

    for (let i=1; i < 4; i++) {
        if (e.target[i].checked) {
            escolha = e.target[i].value
            break
        }
    }

    switch (escolha) {
        case 'pedra':
            solucao1('solucao045', 'JO ');
            setTimeout(()=>{
                solucao1('solucao045', 'KEN ');
            }, 500);
            setTimeout(()=>{
                solucao1('solucao045', 'PO ');
            }, 1000);
            if (escolhaCPU == 'pedra') {
                setTimeout(()=>{
                    solucao1('solucao045', `Pedra com ${escolha}. Empatamos!`);
                }, 1500);
            } else if (escolhaCPU == 'papel') {
                setTimeout(()=>{
                    solucao1('solucao045', `Papel vence ${escolha}. Você perdeu!`);
                }, 2000);
            } else {
                setTimeout(()=>{
                    solucao1('solucao045', `Tesoura perde de ${escolha}. Você ganhou!`);
                }, 2500);
            }
            break;

            case 'papel':
                solucao1('solucao045', 'JO ');
                setTimeout(()=>{
                    solucao1('solucao045', 'KEN ')
                }, 500);
                setTimeout(()=>{
                    solucao1('solucao045', 'PO ')
                }, 1000);
                if (escolhaCPU == 'pedra') {
                    setTimeout(()=>{
                        solucao1('solucao045', `Pedra perde de ${escolha}. Você ganhou!`);
                    }, 1500);
                } else if (escolhaCPU == 'papel') {
                    setTimeout(()=>{
                        solucao1('solucao045', `Papel com ${escolha}. Empatamos!`);
                    }, 2000);
                } else {
                    setTimeout(()=>{
                        solucao1('solucao045', `Tesoura vence ${escolha}. Você perdeu!`);
                    }, 2500);
                }
                break;
        
            case 'papel':
                solucao1('solucao045', 'JO ');
                setTimeout(()=>{
                    solucao1('solucao045', 'KEN ')
                }, 500);
                setTimeout(()=>{
                    solucao1('solucao045', 'PO ')
                }, 1000);
                if (escolhaCPU == 'pedra') {
                    setTimeout(()=>{
                        solucao1('solucao045', `Pedra perde de ${escolha}. Você ganhou!`);
                    }, 1500);
                } else if (escolhaCPU == 'papel') {
                    setTimeout(()=>{
                        solucao1('solucao045', `Papel com ${escolha}. Empatamos!`);
                    }, 2000);
                } else {
                    setTimeout(()=>{
                        solucao1('solucao045', `Tesoura vence ${escolha}. Você perdeu!`);
                    }, 2500);
                }
                break;

            case 'tesoura':
                solucao1('solucao045', 'JO ');
                setTimeout(()=>{
                    solucao1('solucao045', 'KEN ')
                }, 500);
                setTimeout(()=>{
                    solucao1('solucao045', 'PO ')
                }, 1000);
                if (escolhaCPU == 'pedra') {
                    setTimeout(()=>{
                        solucao1('solucao045', `Pedra vence ${escolha}. Você perdeu!`);
                    }, 1500);
                } else if (escolhaCPU == 'papel') {
                    setTimeout(()=>{
                        solucao1('solucao045', `Papel perde de ${escolha}. Você venceu!`);
                    }, 2000);
                } else {
                    setTimeout(()=>{
                        solucao1('solucao045', `Tesoura com ${escolha}. Empatamos`);
                    }, 2500);
                }
                break;
    }
}

//Ex. 046
function solucao046() {
    let intervalo = 500;
    const num = Number(input('input046'));
    solucao('solucao046', ' ');

    for (let i=0; i < num; i++) {
        setTimeout(()=>{
            solucao1('solucao046', `${num - i}, `);
        }, intervalo * i); 
    }
    setTimeout(()=>{
        solucao1('solucao046', `Feliz Ano Novo!!!!`);
    }, intervalo * num);
}

// Ex. 047
function solucao047() {
    const start = Number(input('input047a')),
        end = Number(input('input047b')),
        step = Number(input('input047c'));
        solucao('solucao047', ` `);
        for (let i = start; i <= end; i += step) {
            solucao1('solucao047', `${i} `);
        }
}

// Ex. 048
function solucao048() {
    const start = Number(input('input048a')),
        end = Number(input('input048b')),
        passo = Number(input('input048c'));
    let soma = 0, quantos = 0;
    solucao('solucao048', ' ');
    for (let i=start; i<=end; i+=passo) {
        soma += i;
        quantos++;
        solucao1('solucao048', `${i} `);
    }
    solucao1('solucao048', `A soma desses ${quantos} números é ${soma}.`)
}

// Ex. 049
function solucao049() {
    const num = Number(input('input049'));
    let tabuada = '';
    for (let i=1; i<=10; i++) {
        tabuada += `<li style='list-style-type: none'>${num} x ${i} = ${num*i}</li>`
    }
    solucao('solucao049', tabuada);
}

// Ex. 050
function solucao050() {
    const arrayOfStrings = input('input050').split(', '),
    arrayOfNumbers = arrayOfStrings.map(x => Number(x));
    let soma = 0;
    for (let i=0; i<=5; i++) {
        arrayOfNumbers[i]%2==0?
            soma += arrayOfNumbers[i]:
            soma = soma;
    }
    solucao('solucao050', `A soma dos números pares que você digitou é ${soma}`);
}

// Ex. 051
function solucao051() {
    const termo1 = Number(input('input051a')),
        razao = Number(input('input051b'));
    solucao1('solucao051', 'Os primeiros 10 termos dessa PA são: ');
    for (let i=0; i<10; i++) {
        solucao1('solucao051', `${termo1+razao*i} `);
    }
    solucao1('solucao051', 'FIM');
}

//Função para pegar valor do input
function input(id) {
    return document.querySelector('#'+id).value;
}

//Função para mostrar solução
function solucao(id, texto) {
    return document.querySelector('#'+id).innerHTML = texto;
}

//Função para mostrar soluções complementares, na mesma linha
function solucao1(id, texto) {
    return document.querySelector('#'+id).innerHTML += texto;
}

//Funções para mostrar e esconder grupos de exercícios

function mostraExercicios(exercicios) {
    document.getElementById(exercicios).style.display = 'block';
}

function escondeExercicios(exercicios) {
    document.getElementById(exercicios).style.display = 'none';
}
