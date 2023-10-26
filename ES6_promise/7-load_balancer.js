export default function loadBalancer(chinaDownload, USDownload) {
  // Promise.race() returns a promise that resolves to the value from the first settled promise
  return Promise.race([chinaDownload, USDownload])
    .then((data) => data);
}
