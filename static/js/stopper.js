let seconds = 0;
let minutes = 0;

let displaySeconds =0;
let displayMinutes = 0;

let interval = null;

let time = 0;
startBtns = document.querySelectorAll(".start");
stopBtn = document.querySelector(".stop");

startBtns.forEach(item =>{
    console.log('eventlistener added')
    item.addEventListener('click', event => {
        start();
        startBtns.forEach(item => {
            item.removeEventListener('click', start);
            item.classList.remove("start");
    })
})})

stopBtn.addEventListener('click', stop);



