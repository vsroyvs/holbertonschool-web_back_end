const createInt8TypedArray = (length, position, value) => {
  if (position >= length || position < 0) {
    throw new Error('Position outside range');
  }

  const buffer = new ArrayBuffer(length);
  const data = new DataView(buffer);

  data.setInt8(position, value);

  return data;
};

export default createInt8TypedArray;
