let GameBtns = document.querySelectorAll('.exercise-type');
GameBtns.forEach(item =>{item.addEventListener('click', redirect);})

function redirect() {
  window.location.href = `/${this.id}`;

}

