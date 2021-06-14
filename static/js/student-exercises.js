let GameBtns = document.querySelectorAll('.exercise');
let studentId = document.querySelector(".student-id").id;

GameBtns.forEach(item =>{item.addEventListener('click', redirect);})

function redirect() {
  window.location.href = `/${this.id}/${studentId}`;

}