function getWordsAndImages() {
    let WORDS = document.querySelectorAll('.words-to-match');
    let IMAGES = document.querySelectorAll('.images-to-match');
    console.log('Images: ' + IMAGES.length + " Words: " + WORDS.length);
    return {WORDS, IMAGES};
}

let {WORDS, IMAGES} = getWordsAndImages();

let CHOSEN_WORD;
let CHOSEN_IMAGE;
let TARGET_DIV;

getWordsAndImages();

//Blocking right clicks
WORDS.forEach(word => word.addEventListener('contextmenu', event => event.preventDefault()));
IMAGES.forEach(image => image.addEventListener('contextmenu', event => event.preventDefault()));

setup();

function setupImages() {
    IMAGES.forEach(word => word.addEventListener('click', chooseImage));
}

function setupWords() {
    WORDS.forEach(word => word.addEventListener('click', chooseWord));
}

function setup() {
    setupWords();
    setupImages();
}

function disableEverything() {
    disableImages();
    disableWords();
}

function disableImages() {
    IMAGES.forEach(image => image.removeEventListener('click', chooseImage));
}

function disableWords() {
    WORDS.forEach(word => word.removeEventListener('click', chooseWord));
}

function chooseWord(e) { //Changing chosen word's color to green
    e.target.classList.add('marked-purple');
    e.target.addEventListener('click', deactivateWord);
    CHOSEN_WORD = e.target.id.toLowerCase();
    disableWords();
    if (CHOSEN_IMAGE) {
        checkMatch();
    }
}

function deactivateWord() {
    WORDS.forEach(word => word.classList.remove('marked-purple'));
    WORDS.forEach(word => word.addEventListener('click', chooseWord));
    reset();
}

function unChoseImage(e) {
    e.target.classList.remove('flashcard-active');
    reset();
}

function chooseImage(e) {
    CHOSEN_IMAGE = e.target.dataset['word'];
    TARGET_DIV = e.target.parentElement.id;
    e.target.classList.add('flashcard-active');
    e.target.addEventListener('click', unChoseImage);
    disableImages();
    if (CHOSEN_WORD) checkMatch();
}

function mark(id) { //Placing a green tick to matched image
    let img = document.createElement('img');
    img.src = "/static/images/tick.jpg";
    img.classList.add('tick');
    document.getElementById(id).appendChild(img);
    document.getElementById(id).firstElementChild.classList.remove('flashcard-active', 'images-to-match');
}

function checkMatch() {
    let match = CHOSEN_IMAGE === CHOSEN_WORD;
    match ? handleMatch() : reset();
}

function reset() {
    WORDS.forEach(word => word.classList.remove('marked-purple'));
    IMAGES.forEach(image => image.classList.remove('flashcard-active'));
    [CHOSEN_WORD, CHOSEN_IMAGE, TARGET_DIV] = [null, null, null];
    setup();
}

function scoreWord() {
    document.getElementById(CHOSEN_WORD).classList.add('marked-green');
    document.getElementById(CHOSEN_WORD).classList.remove('words-to-match');
    //TODO: visual distinction (score || put an image there too)
}

function handleMatch() {
    scoreWord()
    mark(TARGET_DIV);
    getWordsAndImages();
    reset();
    if (winCheck()) disableEverything();
}

function winCheck() {
    return document.querySelectorAll('.words-to-match').length === 0;
}

(function shuffle() {
    let randomPos = Math.floor(Math.random() * 6);
    WORDS.forEach(word => {
        word.style.order = randomPos;});
    IMAGES.forEach(image => {
        image.style.order = randomPos;});})();
