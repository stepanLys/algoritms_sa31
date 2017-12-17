function recExp(l, n){
	var e = (Math.sin(l)/Math.pow((l-1),2));
	if (l < n) {
		e *= recExp(l + 1, n);
	}
	return e
}
console.log('Рекурсія: '+recExp(2, 5));

function loopExp(l, n){
	var e = 1;
	for (var i = l; i <= n; i++) {
		e *= Math.sin(i)/Math.pow((i-1),2);
	}
	return e;
}
console.log('Цикл: '+loopExp(2, 5));