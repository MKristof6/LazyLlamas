let base64String = "";
let images =[];
let texts =[];
let data = {};

let saveBtn = document.getElementById("save");

saveBtn.addEventListener('click', uploadData);


async function uploadData(){
    let imageUploads = document.querySelectorAll('input[type=file]');
    let textUploads = document.querySelectorAll('.text');
    let theme = document.getElementById("theme").value;
    let language = document.getElementById("language").value;
    textUploads.forEach(item => {
        texts.push(item.value);

    })
    let promises = [...imageUploads].map((item, index) =>{
        let text = texts[index];
        return imageUploader(item['files'][0], text);
    })
    await Promise.all(promises);
    data.language = language;
    data.theme = theme;
    data.images = images;
    saveData(data);
}

function imageUploader(file, text) {
    let done;
    let promise = new Promise((resolved)=>{done = resolved});
       let reader = new FileReader();
    reader.onload = function () {
        base64String = reader.result.replace("data:"+ file.type +";base64,", '');
        images.push({ text: text, image: base64String });
        done();
    }
    reader.readAsDataURL(file);
    return promise;
}

function saveData(data) {
         fetch('/memory-game-upload', {
                method: "POST",
                body: JSON.stringify(data),
                headers: {"Content-type": "application/json; charset=UTF-8"}
            })
                .then(response => response.json())
                .then(json => console.log(json))
                .catch(err => console.log(err));
}