const cleanSet = (set, string) => {
  if (!string || !string.length) return '';
  let str = '';
  for (const item of set) {
    if (item && item.startsWith(string)) {
      str += str.length === 0 ? item.replace(string, '') : item.replace(string, '-');
    }
  }
  return str;
};

export default cleanSet;
