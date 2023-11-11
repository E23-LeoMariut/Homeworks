const request = new XMLHttpRequest();
request.open("GET", " http://localhost:5000/api/products");
request.setRequestHeader("Access-Control-Allow-Credentials", "true");
request.setRequestHeader("Content-Type", "application/json");
request.onload = processData;
request.send();

function processData() {
    const response = JSON.parse(request.response);

    console.log(request.response);

    var obj = JSON.parse(request.response);

    document.getElementById("title").value = obj.data[0].title;
    document.getElementById("descr").value = obj.data[0].description;
    document.getElementById("phone").value = obj.data[0].phone;
    document.getElementById("mail").value = obj.data[0].email;
    document.getElementById("descr").value = obj.data[0].descr;
}

function onSave() {
    const requestToSendData = new XMLHttpRequest();
    requestToSendData.open("POST", " http://localhost:5000/api/products/1", true);
    requestToSendData.setRequestHeader("Access-Control-Allow-Credentials", "true");
    requestToSendData.setRequestHeader("Content-Type", "application/json");
    requestToSendData.onload = processRequestToSendDataResponse;

    const data = {
        "title": document.getElementById("title").value,
        "description": document.getElementById("descr").value
    }
    requestToSendData.send(JSON.stringify(data));

    function processRequestToSendDataResponse() {
        const response = JSON.parse(request.response);
        console.log(response);
    }
}

function onEdit() {
    document.getElementById("editbtn").disabled = true;
    document.getElementById("savebtn").disabled = false;

    document.getElementById("panel").innerHTML = editPanel;
}

function onSave() {
    document.getElementById("editbtn").disabled = false;
    document.getElementById("savebtn").disabled = true;

    document.getElementById("panel").innerHTML = prodPanel;
}

const editPanel = '<div class="col h-100" id="editPanel"><input type="text" id="title" class = "w-100" placeholder="Title"/><textarea class="h-75 w-100" id="descr" placeholder="Description"></textarea></div>';
const prodPanel = '<div class="col h-100 text-left" id="prodPanel"><h3 class="text-white" id="title">Title</h3><hr class="solid"><p class="text-white" id="descr">A brief description about nothing</p></div>'