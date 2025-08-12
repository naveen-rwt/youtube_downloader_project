const downloadBtn = document.getElementById('downloadBtn');
const urlInput = document.getElementById('urlInput');
const status = document.getElementById('status');

downloadBtn.addEventListener('click', () => {
    const url = urlInput.value.trim();

    if (!url) {
        status.textContent = 'Please enter a URL.';
        return;
    }

    status.textContent = 'Downloading... Please wait.';

    fetch('/download', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ url })
    })
    .then(res => {
        if (!res.ok) throw new Error('Server error: ' + res.status);
        return res.json();
    })
    .then(data => {
        if (data.success) {
            status.textContent = `Download ready: ${data.title}`;
            window.location.href = `/video/${data.filename}`;
        } else {
            status.textContent = 'Error: ' + data.error;
        }
    })
    .catch(err => {
        status.textContent = 'Request failed: ' + err.message;
    });
});
