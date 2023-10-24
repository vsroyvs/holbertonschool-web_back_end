function getResponseFromAPI() {
  return new Promise((resolve, reject) => {
    if (true) {
      resolve('es true');
    } else {
      reject('es false');
    }
  });
}

export default getResponseFromAPI;
