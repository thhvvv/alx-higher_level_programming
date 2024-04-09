#!/usr/bin/node
/* returns the reversed version of a list */
exports.esrever = function (list) {
	const newList = []
	while (list.length) {
		newList.push(list.pop());
	}
	return newList;
};
