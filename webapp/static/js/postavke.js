$(function() {
    listNewControllers();
});

let listNewControllers = function (){
    $.ajax({
        type : 'POST',
        url : 'get-controllers'
    }).done(function (data) {
        data.response.forEach(function (item){
            let itemKeys = Object.keys(item);
            const newDeviceContainer = document.getElementById("devices");

            let head_text_div = document.createElement('div');
            head_text_div.className = 'w-100 py-3 text-center';

            let header_text = document.createElement('span');
            header_text.className = 'text-muted p-2 float-left';
            header_text.innerHTML = item.mac_address;
            head_text_div.appendChild(header_text);

            let active_checkbox = document.createElement('input');
            active_checkbox.type = 'checkbox';
            active_checkbox.className = 'float-right mt-3';
            active_checkbox.checked = item.active;
            head_text_div.appendChild(active_checkbox);

            newDeviceContainer.appendChild(head_text_div);

            active_checkbox.addEventListener('click', function (){
                let data = {"controler_id":item.mac_address}
                if (active_checkbox.checked === true){
                    $.ajax({
                        data : data,
                        type : 'POST',
                        url : 'activate-microcontroller'
                    }).done(function () {
                        console.log('activated')
                    });
                }
                else {
                    $.ajax({
                        data : data,
                        type : 'POST',
                        url : 'deactivate-microcontroller'
                    }).done(function () {
                        console.log('deactivated')
                    });
                }
            });

            let header = document.createElement('div');
            header.className = 'input-group mb-3';

            let input = document.createElement('input');
            input.className = 'form-control';
            if (item.controller_name){
                input.placeholder = item.controller_name;
            }
            else {
                input.placeholder = 'Dodaj ime mikrokontroleru';
            }
            input.type = 'text';
            input.id = item.mac_address;
            header.appendChild(input);

            let input_btn = document.createElement('div');
            input_btn.className = 'input-group-append';

            let btn = document.createElement('button');
            btn.className = 'btn btn-outline-success';
            btn.type = 'button';
            btn.innerHTML = 'Promijeni';

            btn.addEventListener('click', function (){
                let new_name = document.getElementById(item.mac_address).value
                data = {"controler_id":item.mac_address, "new_name":new_name}
                $.ajax({
                    data : data,
                    type : 'POST',
                    url : 'update-controller-name'
                    }).done(function () {
                        // console.log('success')
                    });
            });
            input_btn.appendChild(btn);
            header.appendChild(input_btn);
            newDeviceContainer.appendChild(header);
            });
        });
}