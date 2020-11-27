$(function() {
    addNewDeviceSection();
    showAvailableDevices();
});

let addNewDeviceSection = function () {
    const generalColumns = ['Naziv komponente', 'Lokacija', 'LAN IP'];
    const PinColumns = ['Funkcija pina', 'Ime ili broj pina'];

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

    const submitNewController = document.createElement('button');
    submitNewController.innerHTML = 'Spremi novi kontroler';
    submitNewController.className = 'btn btn-success w-100 mb-3';
    newDeviceContainer.appendChild(submitNewController);

    submitNewController.addEventListener('click', function () {
        let data = {};
        generalColumns.forEach(function (elem) {
            data[elem] = document.getElementById(elem).value;
        });
        $.ajax({
            data : data,
                type : 'POST',
                url : 'add-new-controller'
            }).done(function () {
                console.log('success')
                showAvailableDevices();
        });
    });
};

let showAvailableDevices = function () {
    $.ajax({
        url: '/get-controllers',
        type: 'GET'
    }).done(function (data) {
        let array = data['response'];

        let existingDevicescontainer = document.getElementById("existing-devices-container");
        existingDevicescontainer.innerHTML = '';
        let header = document.createElement('div');
        header.className = 'w-100 py-3 text-center border-bottom';
        let headerText = document.createElement('span');
        headerText.innerHTML = 'Postojeći kontroleri';
        headerText.className = 'text-muted';
        header.appendChild(headerText);
        existingDevicescontainer.appendChild(header);

        for (let i = 0; i < array.length; i++){
            let controllerData = document.createElement("div");
            let headerButton = document.createElement("button");
            headerButton.className = "btn btn-outline-primary my-3";
            headerButton.style.width = '75%';
            headerButton.id = String(i + 1);
            headerButton.innerHTML = array[i].komponenta;

            let deleteHeaderButton = document.createElement("button");
            deleteHeaderButton.className = "btn btn-danger my-3 float-right";
            deleteHeaderButton.style.width = '15%';
            deleteHeaderButton.id = String("delete" + (i + 1));
            deleteHeaderButton.innerHTML = "Izbriši";

            Object.keys(array[i]).forEach(function(key) {
                if (key !== 'id') {
                    let mainElementContainer = document.createElement('div');
                    mainElementContainer.className = 'mt-3';

                    let text = document.createElement('p');
                    text.className = 'text-muted';
                    text.style.marginBottom = "5px";
                    text.innerHTML = key.toUpperCase() + ' : ' + array[i][key];
                    mainElementContainer.appendChild(text);

                    let inputGroup = document.createElement('div');
                    inputGroup.className = 'input-group';

                    let inputField = document.createElement('input');
                    inputField.className = 'form-control';
                    inputField.placeholder = 'Nova vrijednost...';
                    inputField.id = array[i][key];
                    inputGroup.appendChild(inputField);

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
                                currentValue : array[i][key],
                                newValue : inputField.value
                            },
                            type : 'POST',
                            url : 'controller-update'
                        }).done(function (data) {
                            let changedSection = data['changedSection'];
                            let newValue = data['response'][changedSection];
                            text.innerHTML = key.toUpperCase() + ' : ' + newValue;
                            inputField.value = '';
                            inputField.placeholder = 'Nova vrijednost...';
                            if (data['changedSection'] === 'komponenta') {
                                headerButton.innerHTML = newValue;
                            }
                        });
                    });

                    deleteHeaderButton.addEventListener('click', function () {
                        $.ajax({
                            data : {
                                komponenta : headerButton.innerHTML
                            },
                            type : 'POST',
                            url : 'delete-controller',
                            success: function () {
                                console.log("deleted");
                                let componentElement = document.getElementById(headerButton.id);
                                let componentDeleteElement = document.getElementById("delete" + (i + 1));
                                componentElement.remove();
                                componentDeleteElement.remove();
                            }
                    });

                    buttonHolder.appendChild(inputButton);
                    inputGroup.appendChild(buttonHolder);
                    mainElementContainer.appendChild(inputGroup);
                    controllerData.appendChild(mainElementContainer);
                    controllerData.style.display = 'none';
                    });
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
            existingDevicescontainer.appendChild(deleteHeaderButton);
            existingDevicescontainer.appendChild(controllerData);
        }
    });
}
