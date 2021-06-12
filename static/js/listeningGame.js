let gameId = document.querySelector(".listening-game").id;
let sendSolutionBtn = document.getElementById('send');

function get_data() {
    fetch(`/get-listening-game/${gameId}`)
        .then(response => response.json())
        .then(data => getElements(data))
        .then(error => console.log("Error: " + error))
}

function getElements(data) {
    elements = ``
    for (let element of data) {
        elements += `
            <div class="card">
                <input type="image" value="${element['correct_answer']}" name="${element['language']}" src="../static/images/play.png"
                    draggable="false"  class="answer" >
                <div class="answers" id="${element['correct_answer']}">
                <div class="possibilities" >
                    <p>${element["answers"][0]}</p>
                   </div>
                    <div class="possibilities">
                    <p>${element["answers"][1]}</p>
                    </div>
                    <div class="possibilities">
                    <p>${element["answers"][2]}</p>
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
    setupEventListener()

}

function check(e) {
    return e.innerText === e.parentElement.id;

}

function setupEventListener(){
    let words = document.querySelectorAll('.possibilities');
        for( let word of words){
            word.addEventListener("click", e=>{
                e.target.classList.toggle('selected');
            })
        }
}


function init() {
    let buttons = document.querySelectorAll('.answer')
    for (let button of buttons) {
        button.addEventListener("click", e => {
            let answer = e.target.value
            let language = e.target.name
            responsiveVoice.speak(answer, language);
            console.log(language)
        });
    }
}

get_data();