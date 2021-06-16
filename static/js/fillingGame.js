import {networkHandler} from "./networkHandler.js";

const fillingGame = {
    init: function () {
        const gameId = document.querySelector(".filling-gaps").id;
        let solution = [];
        const saveBtn = document.getElementById('save');

        saveBtn.addEventListener('click', () => {
            const answers = document.querySelectorAll('.gap');
            answers.forEach(answer => solution.push(answer.value));
            networkHandler.sendData(solution, `/filling-gap-solution-saver/${gameId}`, networkHandler.redirectHome);
        })

        networkHandler.getData(`/get-filling-game/${gameId}`, fillingGame.showData);

    },
    showData: function (data) {
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
    }

}


fillingGame.init();
