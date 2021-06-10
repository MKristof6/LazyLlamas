let base64String = "";
let images =[];
let texts =[];
let data = [];

let saveBtn = document.getElementById("save");

saveBtn.addEventListener('click', uploadData);


function uploadData(){
    let imageUpload = document.querySelector('input[type=file]');
    let textUploads = document.querySelectorAll('.text');
    let theme = document.getElementById("theme").value;

    textUploads.forEach(item =>{
        texts.push(item.value);

    })
    uploader(imageUpload['files'][0], theme, texts);


}

function uploader(file, theme, texts) {
       let reader = new FileReader();
    reader.onload = function () {
        base64String = reader.result.replace("data:"+ file.type +";base64,", '');
        data.push(theme);
        data.push(texts);
        data.push(base64String);
        saveData(data);
    }
    reader.readAsDataURL(file);


}

function saveData(dat) {

         fetch('/memory-game-saver', {
                method: "POST",
                body: JSON.stringify(dat),
                headers: {"Content-type": "application/json; charset=UTF-8"}
            })
                .then(response => response.json())
                .then(json => console.log(json))
                .catch(err => console.log(err));
}