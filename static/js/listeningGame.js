function get_data(question_id) {
    fetch(`/listening-game/${question_id}`)
        .then(response => response.json())
        .then(data => getElements(data))
        .then(error => console.log("Error: " + error))
}


function getElements(data) {
    elements = ``

    for (let element of data) {

        // console.log(element);
        console.log(" ")
        elements += `
            <div class="card">
                <input type="image" id="speak" value="${element['answer']}" src="./static/images/play.png"
                    draggable="false"  class="answer" >
                <div class="asd">
                <div class="possibilities">
                    <p>${element["possibilities"][0]}</p>
                   </div>
                    <div class="possibilities">
                    <p>${element["possibilities"][1]}</p>
                    </div>
                    <div class="possibilities">
                    <p>${element["possibilities"][2]}</p>
                </div>
                </div>
            </div>
    `
    }
    showElements(elements)

}

function showElements(elements) {
    let container = document.getElementById("container")
    container.innerHTML = elements
    init()

}


function init() {
    let buttons = document.querySelectorAll('.answer')
    for (let button of buttons) {
        button.addEventListener("click", e => {
            let answer = e.target.value
            responsiveVoice.speak(answer);
        });
    }
}

get_data(1)