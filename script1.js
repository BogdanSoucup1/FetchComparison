fetch('http://localhost:8080')
  .then(response => {
    console.log("Script1: ", new Date().toLocaleString());
  });