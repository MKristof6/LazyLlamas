let sendBtn = document.querySelector('.send');
let route = sendBtn.id;
let selectedStudents = [];

sendBtn.addEventListener('click', () => {
    selectedStudents = document.querySelectorAll('.selected');
    console.log(route);

})

function sendData(solution) {
    fetch(`${route}`, {
        method: "POST",
        body: JSON.stringify(solution),
        headers: {"Content-type": "application/json; charset=UTF-8"}
    })
        .then(response => response.json())
        .then(json => console.log(json))
}