export let networkHandler = {

    getData: function (route, callback) {
        fetch(route)
            .then(response => response.json())
            .then(data => callback(data))
    },

    getTableData: function (route, callback, columnHeaders, row) {
        fetch(route)
            .then(response => response.json())
            .then(data => callback(data, columnHeaders, row))
    },

    showTableData: function (dataList, columnHeaders, row) {
        let tableRows = '';
        for (let dataRow of dataList) {
            tableRows += row;
        }
        return columnHeaders + tableRows;
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