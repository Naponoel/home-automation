$(function() {
    let request = $.ajax({
        url: '/get-controllers',
        type: 'GET'
    });

    request.done(function (data){
        createData(data['response']);
    });
});

let toggle = function(elementId){
    let elem = document.getElementById(elementId);
    if (elem.style.display === "none") {
        elem.style.display = "block";
    }
    else {
        elem.style.display = "none";
    }
}

let createData = function(array){
    let container = document.getElementById("existing-controllers");

    for (let i = 0; i < array.length; i++){
        let controllerData = [];

        // console.log(array[i]);
        let header = document.createElement("button");
        header.className = "btn btn-outline-primary w-100 mt-3";
        header.id = "controller-params-" + i;
        header.innerHTML = array[i].komponenta;

        Object.keys(array[i]).forEach(function(key) {
            let mainContainer = document.createElement('div');
            mainContainer.className = 'input-group mt-3'
            let spanContainer = document.createElement('div');
            spanContainer.className = 'input-group-prepend w-25';
            let span = document.createElement('span');
            span.className = 'input-group-text w-100';
            span.innerHTML = key;
            spanContainer.appendChild(span);
            mainContainer.appendChild(spanContainer);
            controllerData.push(mainContainer);
        });
        container.appendChild(header);

        // OVI ELEM-i MORAJU BITI U ZAJEDNIKOM DIV-u KOJI SE ONDA PALI I GASI

        controllerData.forEach(function (elem) {
            container.appendChild(elem);
        });
        header.addEventListener('click', function () {

        });
    }
};
