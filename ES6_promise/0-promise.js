function getResponseFromAPI() {
  return new Promise((resolve, reject) => {
    resolve('Success');
    reject(new Error('error'));
  });
}

export default getResponseFromAPI;
