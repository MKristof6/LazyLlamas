function get_data(question_id) {
    fetch(`/listening-game/${question_id}`)
        .then(response => response.json())
        .then(data => printData(data))
        .then(error => console.log(error))
}


function printData(data){
    console.log("data[0]: " + data[0])
    console.log()
    console.log("data[1]: " + data[1])
    console.log()
    console.log("data[0][0]: " + data[0][0])
    for (let x of data){
        for(let y of x){
            console.log(y)
        }
    }
}


function getElements(data) {
    elements = ``

    for (let element of data) {
        elements += `
            <div class="card">
                <input type="image" id="speak" value="{{ answer[0]['answer'] }}" src="./static/images/play.png"
                       onclick="responsiveVoice.speak(textSpeak())">
                <div class="possibilities">
                    <p>sas</p>
                    <p>sad</p>
                    <p>asd</p>
                </div>
            </div>
    `
    }

}

function showElements(elements) {
    let container = document.getElementById("card")
}


function textSpeak() {
    responsiveVoice.speak(document.getElementById("speak").value);
}


function init() {
    let button = document.getElementById('speak')
    button.addEventListener("click", function (e){

    })

}

get_data(1)