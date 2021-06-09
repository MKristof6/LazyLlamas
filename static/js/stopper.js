let seconds = 0;
let minutes = 0;

let displaySeconds =0;
let displayMinutes = 0;

let interval = null;

let time = 0;

stopBtn = document.querySelector(".stop");


window.addEventListener('click', start);

cards = document.querySelectorAll(".memory-card");

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
    window.removeEventListener('click', start);
    interval = window.setInterval(stopWatch, 1000);
}


    function stop() {
        let isComplete = true;
        cards.forEach(item => {
                if (!item.classList.contains("flip")) {
                    isComplete = false;
                }
            }
        )
        if (isComplete) {
            window.clearInterval(interval);
            time = document.getElementById("stopper-display").innerHTML
            fetch('/memory-solution-saver', {
                method: "POST",
                body: JSON.stringify(countSeconds(time)),
                headers: {"Content-type": "application/json; charset=UTF-8"}
            })
                .then(response => response.json())
                .then(json => console.log(json))
                .catch(err => console.log(err));
        }
    }



const countSeconds = (str) => {
   const [mm = '0', ss = '0'] = (str || '0:0').split(':');
   const minute = parseInt(mm, 10) || 0;
   const second = parseInt(ss, 10) || 0;
   return  (minute*60) + (second);
};
