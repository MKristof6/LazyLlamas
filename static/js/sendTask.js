import {networkHandler} from "./networkHandler.js";

let sendTask = {
    init: function () {
        let sendBtn = document.querySelector('.send');
        let route = sendBtn.id;
        let selectedStudents = [];
        let studentList = [];
        sendBtn.addEventListener('click', () => {
            selectedStudents = document.querySelectorAll('.selected');
            for (let student of selectedStudents) {
                studentList.push(student.id);
            }
            networkHandler.sendData(studentList, route);
        })
    },

}

sendTask.init();
