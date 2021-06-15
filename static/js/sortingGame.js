import {networkHandler} from "./networkHandler.js";

let gameId = document.querySelector(".sorting-game").id;

const sortingGame = {
    showData: function (data) {
        const wordContainer = document.querySelector('.word-container');
        const theme = `<h2>${data.theme}</h2>`;
        wordContainer.insertAdjacentHTML('afterbegin', theme);
        for (let i = 0; i < data.words.length; i++) {
            let pTag = `<p class="words draggable" draggable="true">${data.words[i]}</p>`
            wordContainer.insertAdjacentHTML('beforeend', pTag);
        }
        for (let i = 0; i < data.categories.length; i++) {
            const themeContainer = document.querySelector('.theme-container');
            let categoryDiv = `<div class="theme-card droppable">${data.categories[i]}</div>`;
            themeContainer.insertAdjacentHTML('beforeend', categoryDiv);
        }
        logic();
    }
}

function logic() {
    const DRAGGABLES = document.querySelectorAll('.draggable');
    const DROPPABLES = document.querySelectorAll('.droppable');
    const SUBMIT = document.querySelector('.submit');

    DRAGGABLES.forEach(ele => { //Toggling class for better visualisation
        ele.addEventListener('dragstart', () => {
            ele.classList.add('dragging');
        })

        ele.addEventListener('dragend', () => {
            ele.classList.remove('dragging');
        })
    })

    DROPPABLES.forEach(droppable => { //
        droppable.addEventListener('dragover', (e) => {
            e.preventDefault();
            const dragged = document.querySelector('.dragging');
            droppable.appendChild(dragged);
        });
    })

    function collectSolution() {
        let SOLUTION = {};
        const themes = document.querySelectorAll('.theme-card');
        themes.forEach(theme => { //Initializing object's keys as given themes
            SOLUTION[theme.innerText.split("\n")[0]] = [];
            for (let i = 0; i < theme.childElementCount; i++) {
                SOLUTION[theme.innerText.split("\n")[0]].push(theme.children[i].innerText);
            }
        })
        console.log(SOLUTION);
        networkHandler.sendData(SOLUTION, `/sorting-solution-saver/${gameId}`)//, networkHandler.redirectHome);
    }

    SUBMIT.addEventListener('click', collectSolution);
}


function init() {
    networkHandler.getData(`/get-sorting-game/${gameId}`, sortingGame.showData);
}

init();