import Building from './5-building';

export default class SkyHighBuilding extends Building {
  constructor(sqft, floors) {
    super(sqft);
    if (typeof floors !== 'number') throw TypeError('floors must be a number');
    this._floors = floors;
  }

  // getter and setter
  get floors() {
    return this._floors;
  }

  set floors(value) {
    if (typeof value !== 'number') throw TypeError('value must be a number');
    this._floors = value;
  }

  evacuationWarningMessage() {
    return `Evacuate slowly the ${this._floors} floors.`;
  }
}
