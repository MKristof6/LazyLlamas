let sendBtn = document.querySelector('.send');
let route = sendBtn.id;
let selectedStudents = [];
let studentList = [];

sendBtn.addEventListener('click', () => {
    selectedStudents = document.querySelectorAll('.selected');
    for (let student of selectedStudents){
        studentList.push(student.id);
    }
    sendData(studentList);
})

function sendData(studentList) {
    fetch(`${route}`, {
        method: "POST",
        body: JSON.stringify(studentList),
        headers: {"Content-type": "application/json; charset=UTF-8"}
    })
        .then(response => response.json())
        .then(json => console.log(json))
}