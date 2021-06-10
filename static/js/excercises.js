let GameBtns = document.querySelectorAll('.excercise');
GameBtns.forEach(item =>{item.addEventListener('click', redirect);})

function redirect() {
  window.location.href = `/${this.id}`;

}