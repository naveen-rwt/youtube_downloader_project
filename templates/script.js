const downloadBtn = document.getElementById('downloadBtn');
const urlInput= documnet.getElementById('urlInput');
const status= documnet.getElementById('status');
downloadBtn.addEventListener('click',()=>{
	const url=urlInput.value.trim();
	if(!url){
		status.textContent='Please eneter a URL.';
		return;
	}
	status.textContent='Downloading... Please wait.';
	fetch('/download',{
		method: 'POST',
		header:{ 'Content-Type':'application/json'},
		body:JSON.stringify({url})
	})
	.then(res=>res.json())
	.then(data=>{
		if(data.success){
			status.textContent='Download ready:${data.title}';
			window.location.href='/video/${data/filename}';
		}else{
			status.textContent='Error: '+data.error;
		}
	})
	.catch(err=>{
		status.textContent='Request failed: '+ err.message;
	});
});
