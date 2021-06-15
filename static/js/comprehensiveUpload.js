import {networkHandler} from "./networkHandler.js";

const addQuestionBtn = document.getElementById('button');

let comprehensiveReadingUpload = {
    init: function () {
        const submit = document.getElementById('submit');
        addQuestionBtn.addEventListener('click', this.addQuestion);
        submit.addEventListener('click', this.collectAndSendData);
    },

    collectAndSendData: function () {
        let data = {};
        data['language'] = document.getElementById("language").value;
        data['theme'] = document.getElementById('theme').value;
        data['long-text'] = document.getElementById('long-text').value;
        let questionInputs = document.querySelectorAll('.questions');
        let questions = [];
        for (let question of questionInputs) {
            if (question.value !== 'Itt tehetsz fel újabb kérdést') questions.push(question.value);
        }
        data['questions'] = questions;
        networkHandler.sendData(data, '/comprehensive-reading-upload', networkHandler.redirectHome);

    },

    addQuestion: function () {
        let additionalQuestion = `<input type="text" class="questions" value="${addQuestionBtn.previousElementSibling.value}">`;
        document.querySelector('.question-container').firstElementChild.insertAdjacentHTML('beforeend', additionalQuestion);
        addQuestionBtn.previousElementSibling.value = '';
    }
}

comprehensiveReadingUpload.init();

