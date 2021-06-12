let data = {};
let questionNumber = 6;
let saveBtn = document.getElementById("save");
saveBtn.addEventListener('click', uploadData);

async function uploadData(){

    data.question1 = question1;
    data.question2 = question2;
    data.question3 = question3;
    data.question4 = question4;
    data.question5 = question5;
    data.question6 = question6;

    saveData(data);
}



function saveData(data) {
         fetch('/listening-game-upload', {
                method: "POST",
                body: JSON.stringify(data),
                headers: {"Content-type": "application/json; charset=UTF-8"}
            })
                .then(response => response.json())
                .then(json => console.log(json))
                .catch(err => console.log(err));
}