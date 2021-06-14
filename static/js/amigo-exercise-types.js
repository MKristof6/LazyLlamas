let GameBtns = document.querySelectorAll('.exercise-type');
GameBtns.forEach(item =>{item.addEventListener('click', redirect);})

let sendBtns = document.querySelectorAll('.send');
sendBtns.forEach(item =>{item.addEventListener('click', sendTask)})

function redirect() {
  window.location.href = `/${this.id}`;

}

function sendTask(){
    console.log(this.id);
}