document.addEventListener('DOMContentLoaded', (event) => {
    const fileInput = document.getElementById('fileInput');
    const photo = document.getElementById('photo');
    const predictBtn = document.getElementById('predictBtn');
    const jsonResult = document.getElementById('jsonResult');
    const loading = document.getElementById('loading');

    fileInput.addEventListener('change', function(e) {
        const file = e.target.files[0];
        if (file) {
            const reader = new FileReader();
            reader.onload = function(e) {
                photo.src = e.target.result;
                photo.classList.add('fade-in');
            }
            reader.readAsDataURL(file);
        }
    });

    predictBtn.addEventListener('click', function() {
        if (fileInput.files.length > 0) {
            loading.style.display = 'block';
            const file = fileInput.files[0];
            const reader = new FileReader();
            reader.onload = function(e) {
                const base64Image = e.target.result.split(',')[1];
                fetch('/predict', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({ image: base64Image }),
                })
                .then(response => response.json())
                .then(data => {
                    loading.style.display = 'none';
                    // Display the full prediction result
                    jsonResult.innerHTML = `<pre>${JSON.stringify(data, null, 2)}</pre>`;
                    jsonResult.classList.add('fade-in');
                })
                .catch((error) => {
                    console.error('Error:', error);
                    loading.style.display = 'none';
                    jsonResult.textContent = 'An error occurred during prediction.';
                });
            };
            reader.readAsDataURL(file);
        } else {
            alert('Please select an image first.');
        }
    });
});