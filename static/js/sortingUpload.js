const WORD_ADDER = document.getElementById('word-adder');
const THEMES = document.querySelectorAll('.theme-card');
let THEME_ADDER = document.getElementById('theme-adder');
const SAVE_THEME = document.getElementById('theme-button');
let DATA = {};

function insertWord() { //
    const target = document.getElementById('word-form');
    let source = document.getElementById('word-source');
    source.placeholder = '';
    if (source.value !== '') {
        let toInsert = `<input class="words to-add" type="text" value="${source.value}" disabled>`;
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
            THEME_ADDER.value = "Új téma hozzáadása";
            addThemeListener();
            return;
        }
    }
}

function insertTheme(e) {
    THEME_ADDER.value = '';
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

 function postData() {
    fetch('/upload-words', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        },
        body: JSON.stringify(DATA)
    }).then(r => console.log(r));
}

function getAllData() {
    let themes = [];
    let words = [];
    THEMES.forEach(theme => {
         if (theme.textContent !== "Új téma hozzáadása" && theme.textContent !== "") themes.push(theme.textContent);
    });
    document.querySelectorAll('.to-add').forEach(word => words.push(word.value));
    DATA['themes'] = themes;
    DATA['words'] = words;
    postData().then(r => console.log(r));
}

SAVE_THEME.addEventListener('click', getAllData);




