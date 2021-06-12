let data = {};
let questionNumber = 2;
let saveBtn = document.getElementById("save");
saveBtn.addEventListener('click', uploadData);

function uploadData(){
    let cardAnswers = [];
    let textUploads = [];
    let language = document.getElementById("language").value;
    let theme = document.getElementById("theme").value;
    let cards = [];
    for (let i=0; i<questionNumber; i++){
        textUploads.push(document.querySelectorAll(`[data-name=${CSS.escape(i.toString())}]`));
    }
    for (let card of textUploads) {
        cardAnswers = []
        for (let answer of card) {
            cardAnswers.push(answer.value);
        }
        cards.push(cardAnswers);
    }

    data.cards = cards;
    data.language = language;
    data.theme = theme;

    saveData(data);
}

function saveData(data) {
         fetch('/listening-game-upload', {
                method: "POST",
                body: JSON.stringify(data),
                headers: {"Content-type": "application/json; charset=UTF-8"}
            })
                .then(response => response.json())
                .then(json => console.log(json))
                .catch(err => console.log(err));
}