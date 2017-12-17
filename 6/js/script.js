let expression = new String;

function isOperator(c) {
    return c == '+' ||  c == '-' || c == '*' || c == '/' || c == '^' || c == 'sqrt' || c == 'cos' || c == 'sin';
}

function leftAssoc(c) {
    return c != '^';
}

function priority(c) {
    if (c == '^')    return 3;
    if (c == 'sqrt') return 3;
    if (c == 'sin')  return 3;
    if (c == 'cos')  return 3;
    if (c == '*')    return 2;
    if (c == '/')    return 2;
    if (c == '+')    return 1;
    if (c == '-')    return 1;
    return 0;
}

function polishNotation(expr) {
    let i = 0;
        
    function nextToken() {
        while (i < expr.length && expr[i] == ' ') i++;
        if (i == expr.length) {
        	return '';
        }
        let b = '';
        while (i < expr.length && expr[i] != ' ' && expr[i] != '(' && expr[i] != ')' && !isOperator(expr[i])){
        	b += expr[i++];
        }
        if (b != '') {
        	return b;
        }
        return expr[i++];
    }
    let S = [],
        O = [],
        tok;
    while ((tok = nextToken()) != '') {
        if (tok == '(') {
        	S.push(tok);
        }
        else if (tok == ')') {
            while (S.length > 0 && S[S.length - 1] != '('){
            	O.push(S.pop());
            }
            if (S.length == 0) {
            	return 'Проблема з дужками';
            }
            S.pop();
        } else if (isOperator(tok)) {
            while (S.length > 0 
            		&& isOperator(S[S.length - 1]) 
            		&& ((leftAssoc(tok) && priority(tok) <= priority(S[S.length - 1])) || (!leftAssoc(tok) && priority(tok) < priority(S[S.length - 1])))){
            	O.push(S.pop());
            }
            S.push(tok);
        } else {
            O.push(tok);
        }
    }
    while (S.length > 0) {
        if (!isOperator(S[S.length - 1])) {
        	return 'Проблема з дужками';
        }
        O.push(S.pop());
    }
    if (O.length == 0) {
    	return 'Помилка вводу';
    }
    let s = '';
    for (let i = 0; i < O.length; i++) {
        if (i != 0) {
        	s += ' ';
        }
        s += O[i];
    }
    return s;
}


const operators = {
    '+':    (x, y) => x + y,
    '-':    (x, y) => x - y,
    '*':    (x, y) => x * y,
    '/':    (x, y) => x / y,
    '^':    (x, y) => Math.pow(x, y),
    'sqrt': (x)    => Math.sqrt(x),
    'cos':  (x)    => Math.cos(x),
    'sin':  (x)    => Math.sin(x)
};

function evaluate(expr) {
    let stack = [];
    
    expr.split(' ').forEach(token => {
        if (token in operators) {
            let [x, y] = [stack.pop(), stack.pop()];
            stack.push(operators[token](x, y));
        } else {
            stack.push(parseFloat(token));
        }
    });

    return stack.pop();
};


const btn = document.querySelector('#calc'),
      result = document.querySelector('.result'),
      polishNot = document.querySelector('.polish');

btn.onclick = function(e){
    e.preventDefault();

    polishNot.innerHTML = 'Польська нотація: ';
    result.innerHTML    = 'Результат: ';

    const expression = document.querySelector('#expression').value,
        polish = polishNotation(expression);

    console.log(polish);

    polishNot.innerHTML += polish;
    result.innerHTML += evaluate(polish);
};
