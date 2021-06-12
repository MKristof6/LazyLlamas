function get_data(question_id) {
    fetch(`/get-listening-game/${question_id}`)
        .then(response => response.json())
        .then(data => getElements(data))
        .then(error => console.log("Error: " + error))
}


function getElements(data) {
    elements = ``
    for (let element of data) {
        elements += `
            <div class="card">
                <input type="image" value="${element['answer']}" name="${element['language']}" src="./static/images/play.png"
                    draggable="false"  class="answer" >
                <div class="asd" id="${element['answer']}">
                <div class="possibilities" >
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
    setupEventListener()

}

function check(e) {
    console.log(e.innerText)
    console.log(e.parentElement.id)


    // parentElement id = child element value id


    deactivateClass()
}
function deactivateClass(){
    setupEventListener()
}


function setupEventListener(){
    let words = document.querySelectorAll('.possibilities')
        for( let word of words){
            word.addEventListener("click", e=>{
                console.log("ok")
                check(e.target)


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

get_data(1)