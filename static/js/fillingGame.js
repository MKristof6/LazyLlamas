const gameId = document.querySelector(".filling-gaps").id;
let solution = [];
const saveBtn = document.getElementById('save');

saveBtn.addEventListener('click', () => {
    const answers = document.querySelectorAll('.gap');
    answers.forEach(answer => solution.push(answer.value));
    console.log(solution);
    fillingGame.sendData(solution);
})

const fillingGame = {
    getData: function (route, callback) {
        fetch(route)
            .then(response => response.json())
            .then(data => this.showData(data))

    },

    showData: function (data) {
        console.log(data);
        let readingContainer = document.querySelector('.filling-container');
        document.getElementById('theme').textContent = data['theme'];

        const textParts = data['long_text'];
        textParts.forEach(part => part.replaceAll('.', '.\n'));
        let content = '';
        for (let i = 0; i < textParts.length; i++) {
            content += `<p class="long-text">${textParts[i]}</p>`;
            if (i !== textParts.length - 1) content += `<input type="text" class="gap">`;
        }
        readingContainer.innerHTML = content;
    },

    sendData: function (solution) {
        fetch(`/filling-gap-solution-saver/${gameId}`, {
            method: "POST",
            body: JSON.stringify(solution),
            headers: {"Content-type": "application/json; charset=UTF-8"}
        })
            .then(response => response.json())
            .then(json => console.log(json))
            .then(r => {
                if (r.status.code === 200) window.loaction = '/';
        })
    }
}


function init() {
    fillingGame.getData(`/get-filling-game/${gameId}`, fillingGame.showData);
}

init();
