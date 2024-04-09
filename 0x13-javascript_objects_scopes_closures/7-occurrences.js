#!/isr/bin/node
/* returns number of occurences in alist */
exports.nbOccurences = function (list, searchElement) {
	const filteredElement = list.filter(item => item === searchElement);
	return filteredElement.length;
}
