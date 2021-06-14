let gameId = document.querySelector(".comprehensive-reading").id;

let saveBtn = document.getElementById('save');


let solution = [];
let answers = [];
saveBtn.addEventListener('click', () => {
    answers = document.querySelectorAll('.answer');
    for (let answer of answers) {
        solution.push(answer.value);
    }
    comprehensiveReading.sendData(solution);
})



const comprehensiveReading = {
    getData: function (route, callback) {
        fetch(route)
            .then(response => response.json())
            .then(data => this.showData(data[0]))

    },

    showData: function (data) {
        let readingContainer = document.querySelector('.reading-container');
        let questionContainer = document.querySelector('.question-container');
        let questions = data['questions'];

        let questionList = '<ul>';
        for (let question of questions) {
            questionList += `<li class="question" >${question}</li>  <input class="answer" type="text">`;

        }
        questionList += '</ul>'
        readingContainer.innerHTML = data['long_text'];
        questionContainer.innerHTML = questionList;

    },

    sendData: function (solution) {
    fetch(`/comprehensive-reading-solution-saver/${gameId}`, {
        method: "POST",
        body: JSON.stringify(solution),
        headers: {"Content-type": "application/json; charset=UTF-8"}
    })
        .then(response => response.json())
        .then(json => console.log(json))
}

}


function init() {
    comprehensiveReading.getData(`/get-comprehensive-reading/${gameId}`, comprehensiveReading.showData);
}

init();
