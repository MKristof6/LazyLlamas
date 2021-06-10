
import { stopCheck } from "./stopper.js";

let gameId = document.querySelector(".memory-game").id
let numberOfCards = 6;

const memoryGame = {
    getData: function (route, callback) {
        fetch(route)
            .then(response => response.json())
            .then(data => this.showData(data[0]))

    },

    showData: function (cards) {
        let gameUI = document.querySelector('.memory-game');
        let rows = ''
        for (let i=1; i<=numberOfCards; i++) {
            rows += `   
        <div class="memory-card"  data-framework="${cards[`text${i}`]}">
            <div class="front-face">
                <img src="data:image/png;base64,${cards[`image${i}`]}" />
                <p> ${cards[`text${i}`]}</p>
            </div>
            <img class="back-face" src="../static/images/amigo_logo.png"/>
        </div>
        <div class="memory-card"  data-framework="${cards[`text${i}`]}">
            <div class="front-face">
                <img src="data:image/png;base64,${cards[`image${i}`]}" />
                <p> ${cards[`text${i}`]}</p>
            </div>
            <img class="back-face" src="../static/images/amigo_logo.png"/>
        </div>`
        }
        gameUI.innerHTML = rows
        logic();
    },


}

function logic(){
    let cards = document.querySelectorAll('.memory-card');
    let hasFlippedCard = false;
    let lockBoard = false;
    let firstCard, secondCard;
    cards.forEach(card => card.addEventListener('click', flipCard));


    function flipCard() {
        if (lockBoard) return;
        if (this === firstCard) return;
        this.classList.add('flip');
        if (!hasFlippedCard) {
            //first card clicked
            hasFlippedCard = true;
            firstCard = this;
            return;
        }
        //second card clicked
        hasFlippedCard = false;
        secondCard = this;
        checkForMatch();
        stopCheck.stop();
    }

    function checkForMatch() {
        let isMatch = firstCard.dataset.framework === secondCard.dataset.framework;
        isMatch ? disableMatchedCards() : unflipCards();
    }


    function disableMatchedCards() {
        firstCard.removeEventListener('click', flipCard);
        secondCard.removeEventListener('click', flipCard);
        resetBoard();
    }


    function unflipCards() {
        lockBoard = true;
        setTimeout(() => {
            firstCard.classList.remove('flip');
            secondCard.classList.remove('flip');
            resetBoard();
        }, 1500);

    }

    function resetBoard() {
        [hasFlippedCard, lockBoard] = [false, false];
        [firstCard, secondCard] = [null, null];
    }

    (function shuffle() {
        cards.forEach(card => {
            card.style.order = Math.floor(Math.random() * 12);
        });
    })();

}

function init() {
    memoryGame.getData(`/get-memory-game/${gameId}`, memoryGame.showData);
}

init();




