var max = 100;
var maxHeight = document.documentElement.scrollHeight || document.body.scrollHeight;
var width = 0;
var offset = 0;

document.addEventListener('scroll', function () {
	offset = Math.floor((window.pageYOffset || document.documentElement.scrollTop) / (maxHeight - window
		.innerHeight) * 100);
	document.querySelector('.loading').style.width = offset + '%';
});