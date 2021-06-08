const WORDS = document.querySelectorAll('.words-to-match');
const IMAGES = document.querySelectorAll('.flashcard');
const TICK = `<img class="tick" src="/static/images/tick.jpg" alt=Tick>`;

let CHOSEN_WORD;
let CHOSEN_IMAGE;
let TARGET_DIV;

//Blocking right clicks
WORDS.forEach(word => word.addEventListener('contextmenu', event => event.preventDefault()));
IMAGES.forEach(image => image.addEventListener('contextmenu', event => event.preventDefault()));

setup();

function setup() {
    WORDS.forEach(word => word.addEventListener('click', paintItGreen));
    IMAGES.forEach(word => word.addEventListener('click', chooseImage));
}

function paintItGreen(e) { //Changing chosen word's color to green
    e.target.classList.add('words-to-match-active');
    e.target.addEventListener('click', deactivate);
    CHOSEN_WORD = e.target.textContent.toLowerCase();
    console.log(CHOSEN_WORD);
    WORDS.forEach(word => word.removeEventListener('click', paintItGreen));
    if (CHOSEN_IMAGE) checkMatch();
}

function deactivate() {
    WORDS.forEach(word => word.classList.remove('words-to-match-active'));
    WORDS.forEach(word => word.addEventListener('click', paintItGreen));
    reset();
}

function unChoseImage(e) {
    e.target.classList.remove('flashcard-active');
    e.target.classList.add('flashcard');
    reset();
    IMAGES.forEach(image => image.addEventListener('click', chooseImage));
}

function chooseImage(e) {
    CHOSEN_IMAGE = e.target.dataset['word'];
    TARGET_DIV = e.target.parentElement.id;
    console.log(CHOSEN_IMAGE);
    e.target.classList.remove('flashcard');
    e.target.classList.add('flashcard-active');
    e.target.addEventListener('click', unChoseImage);
    IMAGES.forEach(image => image.removeEventListener('click', chooseImage));
    if (CHOSEN_WORD) checkMatch();
}

function mark(id) { //Placing a green tick to matched image
    let img = document.createElement('img');
    img.src = "/static/images/tick.jpg";
    img.classList.add('tick');
    document.getElementById(id).appendChild(img);
}

function checkMatch() {
    console.log('I work');
    let match = CHOSEN_IMAGE === CHOSEN_WORD;
    console.log(match);
    match ? handleMatch() : reset();
}

function reset() {
    [CHOSEN_WORD, CHOSEN_IMAGE, TARGET_DIV] = [null, null];
    setup();
}

function popImage() {
    for (let image of IMAGES) {
        if (image.dataset['word'] === CHOSEN_IMAGE) IMAGES.pop(image);
    }
}

function popWord() {
    for (let word of WORDS) {
        if (word.textContent.toLowerCase() === CHOSEN_WORD) WORDS.splice(WORDS.indexOf(word), 1)
    }
}

function handleMatch() {
    console.log(IMAGES + WORDS);
    mark(TARGET_DIV);
    // scoreWord();   TODO!
    setup();
    popImage();
    popWord();
}
