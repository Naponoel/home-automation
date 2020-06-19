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
        // console.log(array[i]);
        let controllerData = document.createElement("div");
        let headerButton = document.createElement("button");
        headerButton.className = "btn btn-primary w-100 mt-3";
        headerButton.id = "controller-params-" + i;
        headerButton.innerHTML = array[i].komponenta;

        Object.keys(array[i]).forEach(function(key) {
            let mainElementContainer = document.createElement('div');
            mainElementContainer.className = 'mt-3'

            let text = document.createElement('p');
            text.className = 'text-muted'
            text.innerHTML = key + ' : ' + array[i][key];
            mainElementContainer.appendChild(text);

            let inputGroup = document.createElement('div');
            inputGroup.className = 'input-group'

            let span = document.createElement('input');
            span.className = 'form-control';
            span.placeholder = array[i][key];
            inputGroup.appendChild(span);

            let buttonHolder = document.createElement('div');
            buttonHolder.className = 'input-group-append';

            let inputButton = document.createElement('button');
            inputButton.className = 'btn btn-outline-success';
            inputButton.innerHTML = 'Update'
            inputButton.type = 'button';
            buttonHolder.appendChild(inputButton);
            inputGroup.appendChild(buttonHolder);
            mainElementContainer.appendChild(inputGroup)
            controllerData.appendChild(mainElementContainer);
        });
        container.appendChild(headerButton);
        container.appendChild(controllerData);
    }
};
