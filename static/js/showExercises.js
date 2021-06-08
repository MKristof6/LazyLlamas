const CARDS_TO_CHANGE = document.querySelectorAll('.exercise-change');
const ORIGINAL_MENU = []
CARDS_TO_CHANGE.forEach(e => ORIGINAL_MENU.push(e.firstElementChild.innerHTML));

const EXERCISES = [`<a class="blacklink" href="/matching-game"><h2>Párosítás</h2></a>`,
                `<a class="blacklink" href="/memory-game"><h2>Memóriajáték</h2></a>`,
                `<a class="blacklink" href="/sorting-game"><h2>Sorba rendezés</h2></a>`,
                `<a class="blacklink" href="/listening-game"><h2>Hallás utáni szövegértés</h2></a>`,
                `<a class="blacklink" href="/comprehensive-reading"><h2>Szövegértés</h2></a>`,
                `<a class="blacklink" href="/filling-game"><h2>Kiegészítés</h2></a>`];


function change() {
    for (let i = 0; i < CARDS_TO_CHANGE.length; i++) {
        CARDS_TO_CHANGE[i].innerHTML = EXERCISES[i];
    }
    const backButton = `<div class="student-card-small"><h4>Vissza</h4></div>`;
    document.querySelector('.green-background').insertAdjacentHTML('afterbegin', backButton);
    CARDS_TO_CHANGE.forEach(card => card.removeEventListener('click', change));
    document.querySelector('.student-card-small').addEventListener('click', changeBack);
}

function changeBack() {
    for (let i = 0; i < CARDS_TO_CHANGE.length; i++) {
        CARDS_TO_CHANGE[i].innerHTML = ORIGINAL_MENU[i];
    }
    document.querySelector('.green-background').removeChild(document.querySelector('.green-background').firstElementChild);
    CARDS_TO_CHANGE.forEach(card => card.addEventListener('click', change));
}

function init() {
    CARDS_TO_CHANGE.forEach(card => card.addEventListener('click', change));
}

window.onload = () => init();