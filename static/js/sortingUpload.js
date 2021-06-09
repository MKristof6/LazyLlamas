const WORD_ADDER = document.getElementById('word-adder');
const THEMES = document.querySelectorAll('.theme-card');
let THEME_ADDER = document.getElementById('theme-adder');
const THEME_ADDER_ORIGINAL = document.getElementById('theme-adder').innerHTML;
const SAVE_THEME = document.getElementById('theme-button');

function insertWord() { //
    const target = document.getElementById('word-form');
    let source = document.getElementById('word-source');
    if (source.value !== '') {
        let toInsert = `<input class="words" type="text" value="${source.value}" disabled>`;
        source.value = '';
        target.insertAdjacentHTML('beforeend', toInsert);
    }
}

WORD_ADDER.addEventListener('click', insertWord);

function insertIntoEmptyDiv() { //inserts given user input only if there is available empty card
    const text = THEME_ADDER.value;
    for (let theme of THEMES) {
        if (theme.textContent === '') {
            theme.textContent = text;
            // removeThemeListener();
            THEME_ADDER.value = "Új téma hozzáadása"; //Changing textarea back to "Új téma hozzáadása"
            addThemeListener();
            return;
        }
    }
}

function insertTheme(e) {
    THEME_ADDER.value = '';
    let target = e.target;
    // let form = '<form class="borderless"><input id="text-to-add" type="text" placeholder="Írd ide a témát"></form>'
    // target.insertAdjacentHTML('afterbegin', form);
    // removeThemeListener();
    e.target.addEventListener('focusout', insertIntoEmptyDiv); //inserts the new word user clicks out of the textbox
}

function addThemeListener() {
    styleThemeAdder();
    THEME_ADDER.addEventListener('focusin', insertTheme);
}

function styleThemeAdder() { //Failed to color it in css, JS solution works however
    THEME_ADDER.style.background = '#993166';
    THEME_ADDER.style.color = 'white';
    THEME_ADDER.style.textAlign = 'center';
}

addThemeListener();


