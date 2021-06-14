const WORD_ADDER = document.getElementById('word-source');
const THEMES = document.querySelectorAll('.theme-card');
let THEME_ADDER = document.getElementById('theme-adder');
const SAVE_THEME = document.getElementById('theme-button');
let DATA = {};

function removeIfEmpty(e) {
    if (e.target.value === '') e.target.remove();
}

function checkWordAvailability(word) {
    let container = document.querySelectorAll('.to-add');
    for (let i = 0; i < container.length; i++) {
        if (container[i].value === word) {
            alert('Már létezik ilyen szó!'); //TODO: replace alert with alternate method because textarea focusout glitch
            return false;
        }
    }
    return true;


}function checkThemeAvailability(theme) {
    let container = THEMES;
    for (let i = 0; i < container.length; i++) {
        if (container[i].textContent === theme && theme !== '') {
            alert('Már létezik ilyen szó!');
            return false;
        }
    }
    return true;
}

function insertWord() {
    const target = document.getElementById('word-form');
    let source = WORD_ADDER;
    source.placeholder = 'Írj ide';

    if (checkWordAvailability(source.value) && source.value !== '') {
        let toInsert = `<input class="words to-add" type="text" value="${source.value}">`;
        source.value = '';
        target.insertAdjacentHTML('beforeend', toInsert);
    }
    document.querySelectorAll('.to-add').forEach(word => word.addEventListener('change', removeIfEmpty));
}

WORD_ADDER.addEventListener('focusout', insertWord);

function insertIntoEmptyDiv() { //inserts given user input only if there is available empty card
    const text = THEME_ADDER.value;
    for (let theme of THEMES) {
        if (checkThemeAvailability(text) && theme.textContent === '') {
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
    }).then(r => {
        if (r.status === 200) window.location = '/';
    });
}

function getAllData() {
    let theme = document.getElementById("theme").value;
    let themes = [];
    let words = [];
    THEMES.forEach(theme => {
        if (theme.textContent !== "Új téma hozzáadása" && theme.textContent !== "") themes.push(theme.textContent);
    });
    document.querySelectorAll('.to-add').forEach(word => words.push(word.value));
    DATA['language'] = document.getElementById("language").value;
    DATA['theme'] = theme;
    DATA['themes'] = themes;
    DATA['words'] = words;
    console.log(DATA);
    postData();
}

SAVE_THEME.addEventListener('click', getAllData);




