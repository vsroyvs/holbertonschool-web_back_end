export default class HolbertonClass {
  constructor(size, location) {
    if (typeof size !== 'number') throw TypeError('size must be a number');
    if (typeof location !== 'string') throw TypeError('location must be a string');
    this._size = size;
    this._location = location;
  }

  // getter and setter
  get size() {
    return this._size;
  }

  set size(value) {
    if (typeof value !== 'number') throw TypeError('value must be a number');
    this._size = value;
  }

  get location() {
    return this._location;
  }

  set location(value) {
    if (typeof value !== 'string') throw TypeError('value must be a string');
    this._location = value;
  }

  valueOf() {
    return this._size;
  }

  toString() {
    return this._location;
  }
}
