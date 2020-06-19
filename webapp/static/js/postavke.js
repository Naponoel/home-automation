$(function() {
    let request = $.ajax({
        url: '/get-controllers',
        type: 'GET'
    });

    request.done(function (data){
        createData(data['response']);
    });
});

let getData = function(array){

}

let createData = function(array){
    let container = document.getElementById("existing-controllers");

    for (let i = 0; i < array.length; i++){
        console.log(array[i]);
        let controllerData = document.createElement("div");
        let headerButton = document.createElement("button");
        headerButton.className = "btn btn-primary w-100 mt-3";
        headerButton.id = String(i + 1);
        headerButton.innerHTML = array[i].komponenta;

        Object.keys(array[i]).forEach(function(key) {
            if (key !== 'id') {
                let mainElementContainer = document.createElement('div');
                mainElementContainer.className = 'mt-3';

                let text = document.createElement('p');
                text.className = 'text-muted';
                text.innerHTML = key.toUpperCase() + ' : ' + array[i][key];
                mainElementContainer.appendChild(text);

                let inputGroup = document.createElement('div');
                inputGroup.className = 'input-group';

                let span = document.createElement('input');
                span.className = 'form-control';
                span.placeholder = array[i][key];
                span.id = array[i][key];
                inputGroup.appendChild(span);

                let buttonHolder = document.createElement('div');
                buttonHolder.className = 'input-group-append';

                let inputButton = document.createElement('button');
                inputButton.className = 'btn btn-outline-success';
                inputButton.innerHTML = 'Promjeni';
                inputButton.type = 'button';
                inputButton.addEventListener('click', function () {
                    console.log('SQL komponenta: ' + headerButton.innerHTML);
                    console.log('SQL ID komponente: ' + headerButton.id);
                    console.log('Subsection: ' + key);
                    console.log('Current value: ' + span.placeholder);
                    console.log('New value: ' + span.value);
                });
                buttonHolder.appendChild(inputButton);

                inputGroup.appendChild(buttonHolder);
                mainElementContainer.appendChild(inputGroup);
                controllerData.appendChild(mainElementContainer);
                controllerData.style.display = 'none';
            }
        });

        headerButton.addEventListener('click', function () {
            if (controllerData.style.display === "none") {
                controllerData.style.display = "block";
            }
            else {
                controllerData.style.display = "none";
            }
        })

        container.appendChild(headerButton);
        container.appendChild(controllerData);
    }
};
