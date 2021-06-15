export let networkHandler = {

    getData: function (route, callback) {
        fetch(route)
            .then(response => response.json())
            .then(data => callback(data))
    },

    sendData: function (data, route, callback) {
        fetch(`${route}`, {
            method: "POST",
            body: JSON.stringify(data),
            headers: {"Content-type": "application/json; charset=UTF-8"}
        })
            .then(response => {
                callback(response);
            })
    },

    redirectHome: function (r) {
        if (r.status.code === 200) window.location = '/';
    }
}