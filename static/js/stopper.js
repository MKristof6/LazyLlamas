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


function stopWatch(){
    seconds++;
    if (seconds/60 ===1){
        seconds = 0;
        minutes++;
    }
    if (seconds<10){
        displaySeconds = "0"+seconds.toString();
    }else{
        displaySeconds = seconds.toString();
    }
       if (minutes<10){
        displayMinutes = "0"+minutes.toString();
    }else{
        displaySeconds = minutes.toString();
    }

     document.getElementById("stopper-display").innerHTML = displayMinutes + ":" + displaySeconds;
}



function start(){
    console.log('start');
    interval = window.setInterval(stopWatch, 1000);
}


function stop() {
    console.log('stopped');
    window.clearInterval(interval);
    //TODO: get the time it was stopped on and send to database
    time = document.getElementById("stopper-display").innerHTML
    console.log(countSeconds(time));
    fetch('/memory-solution-saver', {
        method: "POST",
        body: JSON.stringify(countSeconds(time)),
        headers: {"Content-type": "application/json; charset=UTF-8"}
    })
        .then(response => response.json())
        .then(json => console.log(json))
        .catch(err => console.log(err));
}



const countSeconds = (str) => {
   const [mm = '0', ss = '0'] = (str || '0:0').split(':');
   const minute = parseInt(mm, 10) || 0;
   const second = parseInt(ss, 10) || 0;
   return  (minute*60) + (second);
};
