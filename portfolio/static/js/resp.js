burger = document.querySelector('.ham-nav')
navbar = document.querySelector('.sidebar')
navList = document.querySelector('.listing')

burger.addEventListener('click', ()=>{
    navbar.classList.toggle('sidebar-resp');
    navList.classList.toggle('listing-resp');
})