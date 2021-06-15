import {networkHandler} from "./networkHandler.js";

export let searchStudents = {
    setUp: function () {
        let searchByLanguage = document.getElementById('search_language');
        let searchByEmail = document.getElementById('search_email');
        let searchByBirth = document.getElementById('search_bday');

        searchByLanguage.addEventListener("input", function () {
            networkHandler.getData(`/get-students-by-language/${searchByLanguage.value}`, searchStudents.showData)
        })
        searchByEmail.addEventListener("input", function () {
            networkHandler.getData(`/get-students-by-email/${searchByEmail.value}`, searchStudents.showData)
        })
        searchByBirth.addEventListener("input", function () {
            networkHandler.getData(`/get-students-by-birthday/${searchByBirth.value}`, searchStudents.showData)
        })
    },

    showData: function (studentList) {
        let columnHeaders = ``
        columnHeaders += `
    <tr>
    <th>Tanuló neve</th>
    <th>Email</th>
    <th>Születési idő</th>
    <th>Tanult nyelv</th>
    <th>Pontok</th>
    </tr>`
        let tableRows = '';
        for (let student of studentList) {
            tableRows += `
      
  <tr class=student id="${student['id']}">
    <td>${student['name']}</td>
    <td>${student['email']}</td>
    <td>${student['birthday']}</td>
    <td>${student['language']}</td>
    <td>${student['points']}</td>
  </tr>
       `
        }

        let table = columnHeaders + tableRows;
        searchStudents.displayTable(table);

    },
    displayTable: function (table) {
        let tableContainer = document.getElementById('container');
        tableContainer.innerHTML = table;

        let rows = document.querySelectorAll("tr");
        for (let row of rows) {
            row.addEventListener('click', () => {
                row.classList.toggle('selected');
            })
        }
        if (tableContainer.classList.contains('feedback') ){
            searchStudents.displayFeedbackBtn();
        }


    },
    displayFeedbackBtn: function () {
        let rows = document.querySelectorAll(".student");
        for (let row of rows) {
            let feedbackBtn = document.createElement('td');
            feedbackBtn.innerHTML = `<intput type="button" onclick="location.href='/feedback/${row.id}';"> Értékelés </intput>`
            row.appendChild(feedbackBtn);
        }
    }

}

searchStudents.setUp();