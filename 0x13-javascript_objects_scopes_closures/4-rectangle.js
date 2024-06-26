#!/usr/bin/node
/* a class called Recatngle */
class Rectangle {
	constructor (w, h) {
		if (w <= 0 || h <= 0 || isNaN(w) || isNaN(h)) {
			return this;
		}
		this.width = w;
		this.height = h;
	}
	print() {
		for (let i = 0; i < this.height; i++) {
			console.log('X'.repeat(this.width));
		}
	}
	rotate() {
		[this.width,this.height] = [this.height, this.width];
	}
	double() {
		this.width = this.width * 2;
		this.height = this.height * 2;
	}
}
module.exports = Rectangle;
