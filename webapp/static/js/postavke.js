$(function() {
    addNewDeviceSection();
    let request = $.ajax({
        url: '/get-controllers',
        type: 'GET'
    });

    request.done(function (data){
        showAvailableDevices(data['response']);
    });
});

let addNewDeviceSection = function () {
    const generalColumns = ['Naziv komponente', 'Lokacija', 'LAN IP'];
    const PinColumns = ['Funkcija pina', 'Ime pina'];

    const newDeviceContainer = document.getElementById("new-device-container");
    const allInputs = document.createElement('div');
    allInputs.className = 'input-group border-bottom';

    let header = document.createElement('div');
    header.className = 'w-100 py-3 text-center border-bottom';
    let headerText = document.createElement('span');
    headerText.innerHTML = 'Dodaj novi kontroler';
    headerText.className = 'text-muted';
    header.appendChild(headerText);
    newDeviceContainer.appendChild(header);

    generalColumns.forEach(function (data) {
        let singleInputDiv = document.createElement('div');
        singleInputDiv.className = 'w-100 my-3';

        let generalInputField = document.createElement('input');
        generalInputField.className = 'form-control';
        generalInputField.placeholder = data;
        generalInputField.id = data;

        singleInputDiv.appendChild(generalInputField);
        allInputs.appendChild(singleInputDiv);
    });
    newDeviceContainer.appendChild(allInputs);

    const addPinBtn = document.createElement('button');
    addPinBtn.innerHTML = 'Dodaj GPIO';
    addPinBtn.className = 'btn btn-outline-success my-4';
    newDeviceContainer.appendChild(addPinBtn);


    addPinBtn.addEventListener('click', function () {
        let pinDiv = document.createElement('div');
        pinDiv.className = 'form-check form-check-inline w-100 my-2';

        PinColumns.forEach(function (data) {
            let pinInputField = document.createElement('input');
            pinInputField.className = 'form-control m-1';
            pinInputField.placeholder = data;
            pinInputField.id = data;

            pinDiv.appendChild(pinInputField);
        });
        let pinDeleteBtn = document.createElement('button');
        pinDeleteBtn.className = 'btn btn-danger btn-sm ml-3';
        pinDeleteBtn.innerHTML = 'X';
        pinDiv.appendChild(pinDeleteBtn);

        pinDeleteBtn.addEventListener('click', function () {
        pinDeleteBtn.parentElement.remove();
        });
        newDeviceContainer.insertBefore(pinDiv, this);
    });
};

let showAvailableDevices = function (array) {
    let existingDevicescontainer = document.getElementById("existing-devices-container");

    let header = document.createElement('div');
    header.className = 'w-100 py-3 text-center border-bottom';
    let headerText = document.createElement('span');
    headerText.innerHTML = 'Postojeći kontroleri kontroler';
    headerText.className = 'text-muted';
    header.appendChild(headerText);
    existingDevicescontainer.appendChild(header);

    for (let i = 0; i < array.length; i++){
        let controllerData = document.createElement("div");
        let headerButton = document.createElement("button");
        headerButton.className = "btn btn-outline-primary w-100 my-3";
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
                span.placeholder = 'Nova vrijednost...';
                span.id = array[i][key];
                inputGroup.appendChild(span);

                let buttonHolder = document.createElement('div');
                buttonHolder.className = 'input-group-append mb-3';

                let inputButton = document.createElement('button');
                inputButton.className = 'btn btn-outline-success';
                inputButton.innerHTML = 'Promjeni';
                inputButton.addEventListener('click', function () {
                    $.ajax({
                        data : {
                            komponenta : headerButton.innerHTML,
                            sqlID : headerButton.id,
                            subsection : key,
                            currentValue : span.placeholder,
                            newValue : span.value
                        },
                        type : 'POST',
                        url : 'controller-update'
                    }).done(function (data) {
                        console.log(data);
                    });
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
        });
        existingDevicescontainer.appendChild(headerButton);
        existingDevicescontainer.appendChild(controllerData);
    }
}
