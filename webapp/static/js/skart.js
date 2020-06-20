// $(function() {
//     let request = $.ajax({
//         url: '/get-controllers',
//         type: 'GET'
//     });
//
//     request.done(function (data){
//         create(data['response']);
//     });
// });
//
// document.getElementById("add-new-device").addEventListener('click', function () {
//     expandSetup();
// });
//
// let expandSetup = function(){
//     console.log('yee');
// }
//
//
// let create = function(array){
//     let newDeviceContainer = document.getElementById("new-device-container");
//
//     let neededData = ['Ime komponente', 'LAN IP', 'Lokacija'];
//     neededData.forEach(function (data) {
//         let inputGroup = document.createElement('div');
//         inputGroup.className = 'input-group my-3';
//
//         let span = document.createElement('input');
//         span.className = 'form-control';
//         span.placeholder = data;
//         span.id = data;
//
//         inputGroup.appendChild(span);
//         newDeviceContainer.appendChild(inputGroup);
//
//
//     });
//
//     let addPinButton = document.createElement('button');
//     addPinButton.className = 'btn btn-outline-success';
//     addPinButton.innerHTML = 'Dodaj pin';
//
//     newDeviceContainer.appendChild(addPinButton);
//
//     addPinButton.addEventListener('click', function () {
//         let newPinContainer = document.createElement('div');
//     });
//
//     let container = document.getElementById("container");
//     for (let i = 0; i < array.length; i++){
//         let controllerData = document.createElement("div");
//         let headerButton = document.createElement("button");
//         headerButton.className = "btn btn-outline-primary w-100 my-3";
//         headerButton.id = String(i + 1);
//         headerButton.innerHTML = array[i].komponenta;
//
//         Object.keys(array[i]).forEach(function(key) {
//             if (key !== 'id') {
//                 let mainElementContainer = document.createElement('div');
//                 mainElementContainer.className = 'mt-3';
//
//                 let text = document.createElement('p');
//                 text.className = 'text-muted';
//                 text.innerHTML = key.toUpperCase() + ' : ' + array[i][key];
//                 mainElementContainer.appendChild(text);
//
//                 let inputGroup = document.createElement('div');
//                 inputGroup.className = 'input-group';
//
//                 let span = document.createElement('input');
//                 span.className = 'form-control';
//                 span.placeholder = 'Nova vrijednost...';
//                 span.id = array[i][key];
//                 inputGroup.appendChild(span);
//
//                 let buttonHolder = document.createElement('div');
//                 buttonHolder.className = 'input-group-append';
//
//                 let inputButton = document.createElement('button');
//                 inputButton.className = 'btn btn-outline-success';
//                 inputButton.innerHTML = 'Promjeni';
//                 inputButton.addEventListener('click', function () {
//                     $.ajax({
//                         data : {
//                             komponenta : headerButton.innerHTML,
//                             sqlID : headerButton.id,
//                             subsection : key,
//                             currentValue : span.placeholder,
//                             newValue : span.value
//                         },
//                         type : 'POST',
//                         url : 'controller-update'
//                     }).done(function (data) {
//                         console.log(data);
//                     });
//                 });
//                 buttonHolder.appendChild(inputButton);
//
//                 inputGroup.appendChild(buttonHolder);
//                 mainElementContainer.appendChild(inputGroup);
//                 controllerData.appendChild(mainElementContainer);
//                 controllerData.style.display = 'none';
//             }
//         });
//
//         headerButton.addEventListener('click', function () {
//             if (controllerData.style.display === "none") {
//                 controllerData.style.display = "block";
//             }
//             else {
//                 controllerData.style.display = "none";
//             }
//         });
//
//         container.appendChild(headerButton);
//         container.appendChild(controllerData);
//     }
// };
