export default class ClassRoom {
    constructor(maxStudentsSize){
        if (this.constructor !== ClassRoom && this.evacuationWarningMessage === undefined) {
            throw new Error('Class extending Building must override evacuationWarningMessage');
        }
        if (typeof maxStudentsSize !== 'number') throw TypeError('maxStudentsSize must be a number');
        this._maxStudentsSize = maxStudentsSize
    } 
}
