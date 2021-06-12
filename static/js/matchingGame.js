import { stopCheck } from "./matching-stopper.js";

let gameId = document.querySelector(".matching-game").id;
let numberOfCards = 6;

const matchingGame = {
    getData: function (route, callback) {
        fetch(route)
            .then(response => response.json())
            .then(data => this.showData(data[0]))

    },

    showData: function (cards) {
        let wordContainer = document.querySelector('.word-container');
        let imageContainer = document.querySelector('.image-container');

        let imageList = '';
        let wordList = '<ul>';
        for (let i = 1; i <= numberOfCards; i++) {
            wordList += `<li class="words-to-match" id="${cards[`text${i}`]}">${cards[`text${i}`]}</li>`;
            imageList += `
            <div class="flashcard-container">
            <img class="flashcard images-to-match" src="data:image/png;base64,${cards[`image${i}`]}" data-word="${cards[`text${i}`]}">
            </div>
            `
        }
        wordList += '</ul>'
        wordContainer.innerHTML = wordList;
        imageContainer.innerHTML = imageList;
        logic();
    },

}

function logic() {
    let WORDS = document.querySelectorAll('.words-to-match');
    let IMAGES = document.querySelectorAll('.images-to-match');
    let hasChosenWord = false;
    let hasChosenImage = false;
    let CHOSEN_WORD, CHOSEN_IMAGE;

    function setup() {
        //Blocking right clicks
        WORDS.forEach(word => word.addEventListener('contextmenu', event => event.preventDefault()));
        IMAGES.forEach(image => image.addEventListener('contextmenu', event => event.preventDefault()));
        IMAGES.forEach(image => image.addEventListener('click', chooseImage));
        WORDS.forEach(word => word.addEventListener('click', chooseWord));
    }

    setup();


    function chooseWord() {
        if (this.id === CHOSEN_WORD){
            this.classList.remove('marked-purple');
            CHOSEN_WORD = null;
            hasChosenWord = false;
        }else{
            if (hasChosenWord) return;
            this.classList.add('marked-purple');
            hasChosenWord = true;
            CHOSEN_WORD = this.id;
            if (hasChosenImage) checkMatch();
        }
    }

    function chooseImage() {
        if (this.dataset['word'] === CHOSEN_IMAGE){
            this.parentElement.classList.remove('flashcard-active');
            CHOSEN_IMAGE = null;
            hasChosenImage = false;
        }else{
            if (hasChosenImage) return;
            this.parentElement.classList.add('flashcard-active');
            hasChosenImage = true;
            CHOSEN_IMAGE = this.dataset['word'];
            if (hasChosenWord) checkMatch();
        }

    }

    function mark() {
        let img = document.createElement('img');
        img.src = "../static/images/tick.jpg";
        img.classList.add('tick');
        document.querySelector('.flashcard-active').appendChild(img);
    }

    function checkMatch() {
        let match = CHOSEN_IMAGE === CHOSEN_WORD;
        match ? handleMatch() : reset();
    }

    function reset() {
        document.querySelector('.flashcard-active').firstElementChild.classList.remove('images-to-match');
        document.querySelector('.flashcard-active').classList.remove('flashcard-active');
        document.getElementById(CHOSEN_WORD).classList.remove("words-to-match", "marked-purple");
        [CHOSEN_WORD, CHOSEN_IMAGE] = [null, null];
        [hasChosenWord, hasChosenImage] = [null, null];
    }

    function scoreWord() {
        document.getElementById(CHOSEN_WORD).classList.add('marked-green');

    }

    function handleMatch() {
        scoreWord();
        mark();
        WORDS = document.querySelectorAll('.words-to-match');
        IMAGES = document.querySelectorAll('.images-to-match');
        reset();
         if (winCheck()) stopCheck.stop();
    }

    function winCheck() {
        return document.querySelectorAll('.words-to-match').length === 0;
    }

    (function shuffle() {
        let randomPos = Math.floor(Math.random() * 6);
        WORDS.forEach(word => {
            word.style.order = randomPos;
        });
        IMAGES.forEach(image => {
            image.style.order = randomPos;
        });
    })();

}

function init() {
    matchingGame.getData(`/get-matching-game/${gameId}`, matchingGame.showData);
}

init();
