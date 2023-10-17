export default class Airport {
  constructor(name, code) {
    if (typeof name !== 'string') throw TypeError('name must be a string');
    if (typeof code !== 'string') throw TypeError('code must be a string');
    this._name = name;
    this._code = code;
  }

  // getter ande setter
  get name() {
    return this._name;
  }

  set name(value) {
    if (typeof value !== 'string') throw TypeError('value must be a string');
    this._name = value;
  }

  get code() {
    return this._code;
  }

  set code(value) {
    if (typeof value !== 'string') throw TypeError('value must be a string');
    this._code = value;
  }

  toString() {
    return `[object ${this._code}]`;
  }
}
