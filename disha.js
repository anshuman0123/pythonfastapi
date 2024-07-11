fetch('http://localhost:8000/anshu', {
    "method": "GET",
    "headers": {
        "Access-Control-Allow-Origin": "*"
    }
  })
  .then(response => response.json())
  .then(data => {
    const imagesContainer = document.getElementById(`images-container`);
    data.forEach(stock => {
        const image = document.createElement('img')
        image.src = stock['path']
        imagesContainer.appendChild(image)
    });
  })