const buttons = document.querySelectorAll('.button');
const inserter = document.getElementById('text-inserter');

function resetInserter() {
    inserter.value='';
    inserter.placeholder='Szöveg helye';
}

function insertField() {
    let content = this.classList.contains('purple') ? inserter.value : '';
    const field = `<input type="text" name="text" value="${content}" class="long-text">`;
    inserter.parentElement.insertAdjacentHTML('beforeend', field);
    resetInserter();
}

buttons.forEach(button => button.addEventListener('click', insertField));