let timeoutId;

document.addEventListener('mousemove', function(){;
    clearTimeout(timeoutId);
    var navbar = document.querySelector('.nav-bar');
    navbar.classList.add('show');
    timeoutId = setTimeout(function() {
        document.querySelector('.nav-bar').classList.remove('show');
    }, 60000);
});