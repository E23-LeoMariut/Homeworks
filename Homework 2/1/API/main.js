
window.onload = function() {
    console.log("Script loaded succesfully");

    var name = JSON.parse(localStorage.getItem("name"))
    if(name != null) document.getElementById("name").value = name;
    var surname = JSON.parse(localStorage.getItem("surname"))
    if (surname != null) document.getElementById("surname").value = surname;
    var phone = JSON.parse(localStorage.getItem("phone"))
    if(phone != null) document.getElementById("phone").value = phone;
    var descr = JSON.parse(localStorage.getItem("descr"))
    if(descr != null) document.getElementById("descr").value = descr;
}

function onSave() {
    console.log("Saving");

    localStorage.setItem("name", JSON.stringify(document.getElementById("name").value));
    localStorage.setItem("surname", JSON.stringify(document.getElementById("surname").value));
    localStorage.setItem("phone", JSON.stringify(document.getElementById("phone").value));
    localStorage.setItem("descr", JSON.stringify(document.getElementById("descr").value));
}