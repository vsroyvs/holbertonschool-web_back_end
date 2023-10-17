export default class Building {
  constructor(sqft) {
    if(typeof sqft !== 'number') throw TypeError('sqft must be a number');
    this._sqft = sqft;
    if (this.constructor !== Building && this.evacuationWarningMessage === undefined) {
      throw new Error('Abstract Class can not be instantiated.');
    }
}

  // getter and setter
  get sqft() {
    return this._sqft;
  }

  set sqft(value) {
    if(typeof value !== 'number') throw TypeError('sqft must be a number');
    this._sqft = value;
  }
}
