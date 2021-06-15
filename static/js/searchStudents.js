import {networkHandler} from "./networkHandler.js";

export let searchStudents = {
    setUp: function () {
        let searchByLanguage = document.getElementById('language');
        let searchByEmail = document.getElementById('email');
        let searchByBirth = document.getElementById('age');
        let searchParams = [searchByBirth, searchByEmail, searchByLanguage]
        searchParams.forEach(item => item.addEventListener('input', function () {
            networkHandler.getData(`/search/${item.id}/${item.value}`, searchStudents.showData)}
        ))
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
    <td>${student['age']}</td>
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
        let rows = document.querySelectorAll(".student");
        if (tableContainer.classList.contains('feedback') ){
            searchStudents.displayFeedbackBtn(rows);
        }
        else{
            searchStudents.selectStudents(rows);
        }
    },
    selectStudents: function (rows){
        for (let row of rows) {
            row.addEventListener('click', () => {
                row.classList.toggle('selected');
            })
        }
    },

    displayFeedbackBtn: function (rows) {
        for (let row of rows) {
            let feedbackBtn = document.createElement('td');
            feedbackBtn.innerHTML = `<intput type="button" onclick="location.href='/feedback/${row.id}';"> Értékelés </intput>`
            row.appendChild(feedbackBtn);
        }
    }

}

searchStudents.setUp();