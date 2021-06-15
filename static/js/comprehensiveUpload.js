import {networkHandler} from "./networkHandler.js";

let DATA = {};
const questionAdder = document.getElementById('button');
const submit = document.getElementById('submit');

questionAdder.addEventListener('click', newQuestion);
submit.addEventListener('click', collectAndSend);


function collectAndSend() {
    DATA['language'] = document.getElementById("language").value;
    DATA['theme'] = document.getElementById('theme').value;
    DATA['long-text'] = document.getElementById('long-text').value;
    const questionInputs = document.querySelectorAll('.questions'); //Question's number are dependent on the user, so looping through them by class
    let questions = [];
    for (let question of questionInputs) {
        if (question.value !== 'Itt tehetsz fel újabb kérdést') questions.push(question.value);
    }
    DATA['questions'] = questions;
    networkHandler.sendData(DATA, '/comprehensive-reading-upload', networkHandler.redirectHome);
}




function newQuestion() {
    let additionalQuestion = `<input type="text" class="questions" value="${questionAdder.previousElementSibling.value}">`;
    document.querySelector('.question-container').firstElementChild.insertAdjacentHTML('beforeend', additionalQuestion);
    questionAdder.previousElementSibling.value = '';
}


