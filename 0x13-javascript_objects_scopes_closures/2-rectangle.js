#!/usr/bin/node
/* a class caller Rectangle */
class Rectangle {
	constructor(w,h) {
		if (w <= 0 || h <= 0 || isNaN(w) || isNaW(h)) {
			return this;
		}
		this.width = w;
		this.height = h;
	}
}
module.exports = Rectangle;
