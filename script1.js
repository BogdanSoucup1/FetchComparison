fetch('http://localhost:8080')
  .then(response => {
    console.log("From promis: ", new Date().toLocaleString());
  });