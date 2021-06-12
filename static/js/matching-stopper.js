let gameId = document.querySelector(".matching-game").id

let seconds = 0;
let minutes = 0;

let displaySeconds = 0;
let displayMinutes = 0;

let interval = null;

let time = 0;

window.addEventListener('click', start);
function stopWatch() {
    console.log('ok');
    seconds++;
    if (seconds / 60 === 1) {
        seconds = 0;
        minutes++;
    }
    if (seconds < 10) {
        displaySeconds = "0" + seconds.toString();
    } else {
        displaySeconds = seconds.toString();
    }
    if (minutes < 10) {
        displayMinutes = "0" + minutes.toString();
    } else {
        displaySeconds = minutes.toString();
    }

    document.getElementById("stopper-display").innerHTML = displayMinutes + ":" + displaySeconds;
}


function start() {
    window.removeEventListener('click', start);
    interval = window.setInterval(stopWatch, 1000);
}

export let stopCheck = {
    stop: function () {
        let isComplete = true;
        let images = document.querySelectorAll(".images-to-match");
        if (images.length !== 0 ){
            isComplete = false;
        }


        //    TODO: Leáll a timer, ha átfordult minden kártya, de automatikusan be is küldi.
        //    TODO: Kiszervezendő a beküldés, hogy gombhoz lehessen kötni. De akár így is jó(?)

        if (isComplete) {
            window.clearInterval(interval);
            time = document.getElementById("stopper-display").innerHTML
            fetch(`/matching-solution-saver/${gameId}`, {
                method: "POST",
                body: JSON.stringify(countSeconds(time)),
                headers: {"Content-type": "application/json; charset=UTF-8"}
            })
                .then(response => response.json())
                .then(json => console.log(json))
        }
    }
}


const countSeconds = (str) => {
    const [mm = '0', ss = '0'] = (str || '0:0').split(':');
    const minute = parseInt(mm, 10) || 0;
    const second = parseInt(ss, 10) || 0;
    return (minute * 60) + (second);
};
