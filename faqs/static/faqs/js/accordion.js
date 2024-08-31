document.addEventListener('DOMContentLoaded', function() {
    var accordionButtons = document.querySelectorAll('.accordion .btn-link');
    
    accordionButtons.forEach(function(button) {
        button.addEventListener('click', function() {
            var icon = this.querySelector('i');
            icon.classList.toggle('fa-chevron-down');
            icon.classList.toggle('fa-times');
        });
    });
});