const DRAGGABLES = document.querySelectorAll('.draggable');
const DROPPABLES = document.querySelectorAll('.droppable');
const SUBMIT = document.querySelector('.submit');
const SOLUTION = {};

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

function collect() {
    const themes = document.querySelectorAll('.theme-card');
    themes.forEach(theme => { //Initializing object's keys as given themes
        SOLUTION[theme.innerText.split("\n")[0]] = [];
        for (let i = 0; i < theme.childElementCount; i++) {
            SOLUTION[theme.innerText.split("\n")[0]].push(theme.children[i].innerText);
        }
    })
    console.log(SOLUTION);
}

SUBMIT.addEventListener('click', collect);
