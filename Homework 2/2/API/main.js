/*
Postman create user with POST, raw body:

{
    "first_name": "John",
    "last_name": "Doe",
    "email": "john@email.com",
    "phone": "+22222222",
    "descr": "A short description about nothingness",
    "type": 1
}
*/

const request = new XMLHttpRequest();
request.open("GET", "http://localhost:5000/api/user");
request.setRequestHeader("Access-Control-Allow-Credentials", "true");
request.setRequestHeader("Content-Type", "application/json");
request.onload = processData;
request.send();

function processData() {
    const response = JSON.parse(request.response);

    console.log(request.response);

    var obj = JSON.parse(request.response);

    document.getElementById("name").value = obj.data[0].first_name;
    document.getElementById("surname").value = obj.data[0].last_name;
    document.getElementById("phone").value = obj.data[0].phone;
    document.getElementById("mail").value = obj.data[0].email;
    document.getElementById("descr").value = obj.data[0].descr;
}

function onSave() {
    const requestToSendData = new XMLHttpRequest();
    requestToSendData.open("POST", "http://localhost:5000/api/user", true);
    requestToSendData.setRequestHeader("Access-Control-Allow-Credentials", "true");
    requestToSendData.setRequestHeader("Content-Type", "application/json");
    requestToSendData.onload = processRequestToSendDataResponse;

    const data = {
        "first_name": document.getElementById("name").value,
        "last_name": document.getElementById("surname").value,
        "email": document.getElementById("mail").value,
        "phone": document.getElementById("phone").value,
        "descr": document.getElementById("descr").value,
        "type": 1
    }
    requestToSendData.send(JSON.stringify(data));

    function processRequestToSendDataResponse() {
        const response = JSON.parse(request.response);
        console.log(response);
    }
}