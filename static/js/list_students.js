console.log("ok")

function searchByLanguage(language) {
    fetch(`/get-students-by-language/${language}`)
        .then(response => response.json())
        .then(data => getElementsData(data))
        .catch(error => console.log(error))
}

function searchByEmail(email) {
    fetch(`/get-students-by-email/${email}`)
        .then(response => response.json())
        .then(data => getElementsData(data))
        .catch(error => console.log(error))
}

function searchByBirth(birth) {
    fetch(`/get-students-by-birthday/${birth}`)
        .then(response => response.json())
        .then(data => getElementsData(data))
        .catch(error => console.log(error))
}

function getElementsData(data) {
    elements = ``
    elements +=`
    <tr>
    <th>Tanuló neve</th>
    <th>Email</th>
    <th>Születési idő</th>
    <th>Tanult nyelv</th>
    <th>Pontok</th>
    </tr>`


    for (let element of data) {

        console.log(element)

        elements += `
      
  <tr>
    <td>${element['name']}</td>
    <td>${element['email']}</td>
    <td>${element['birthday']}</td>
    <td>${element['language']}</td>
    <td>${element['points']}</td>
  </tr>
       `
    }
    showElements(elements)

}

function showElements(elements) {
    let container = document.getElementById('container')
    container.innerHTML = elements
}


function setup() {

    let searchLanguage = document.getElementById('search_language')
    searchLanguage.addEventListener("input", function () {
        console.log("okkkke")
        searchByLanguage(searchLanguage.value)
    })

    let searchEmail = document.getElementById('search_email')
    searchEmail.addEventListener("input", function () {
        searchByEmail(searchEmail.value)
    })

    let searchDate = document.getElementById('search_bday')
    searchDate.addEventListener("input", function () {
        searchByBirth(searchDate.value)
    })


}

setup()