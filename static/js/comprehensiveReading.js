import {networkHandler} from "./networkHandler.js";
let comprehensiveReading = {
    init: function () {
        let gameId = document.querySelector(".comprehensive-reading").id;
        let saveBtn = document.getElementById('save');
        let solution = [];
        let answers = [];

        saveBtn.addEventListener('click', () => {
            answers = document.querySelectorAll('.answer');
            for (let answer of answers) {
                solution.push(answer.value);
            }
            networkHandler.sendData(solution, `/comprehensive-reading-solution-saver/${gameId}`, networkHandler.redirectHome);
        })
        networkHandler.getData(`/get-game/comprehensive-reading/${gameId}`, comprehensiveReading.showData);

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

    }
}
comprehensiveReading.init();
