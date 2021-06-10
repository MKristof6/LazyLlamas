function get_data(question_id) {
    fetch(`/listening-game/${question_id}`)
        .then(response => response.json())
        .then(data => getElements(data))
        .then(error => console.log("Error: " + error))
}


function printData(data){
    console.log("data[0]: " + data[0]["answer"])
    for (let x of data){
            console.log("asd :" + x["answer"])

    }
}


function getElements(data) {
    elements = ``

    for (let element of data) {

        // console.log(element);
        console.log(" ")
        elements += `
            <div class="card">
                <input type="image" id="speak" value="${element['answer']}" src="./static/images/play.png"
                    draggable="false"   >
                <div class="possibilities">
                    <p>${element["possibility"]}</p>
                    <p>${element["possibility"]}</p>
                    <p>${element["possibility"]}</p>
                </div>
            </div>
    `
    }
    showElements(elements)

}

// onclick="responsiveVoice.speak(textSpeak())

function showElements(elements) {
    let container = document.getElementById("container")
    container.innerHTML=elements
    init()

}


function textSpeak() {
    responsiveVoice.speak(document.getElementById("speak").value);
}


function init() {
    let button = document.getElementById('speak')
    button.addEventListener("click", e => {
        console.log(e.target.value)
    });

}

get_data(1)