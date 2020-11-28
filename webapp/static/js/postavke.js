$(function (){
    $.ajax({
        type : 'POST',
        url : 'get-controllers'
    }).done(function (data) {
        let parsed = JSON.parse(data);
        console.log(parsed);
        parsed.forEach(function (item){
            console.log(item);
            // Main container
            const all_devices = document.getElementById("devices");
            all_devices.id = 'Main-container';

            // Device container
            let device_container = document.createElement('div');
            device_container.className = 'w-100 border';
            device_container.id = 'Device-container';

            // Create header (MAC address)
            let uC_header = document.createElement('div');
            uC_header.className = 'w-100 pt-3 text-center';
            uC_header.id = 'MAC-address-header';
            let mac_address = document.createElement('div');
            mac_address.className = 'w-100 pt-3 text-center';
            let title_mac_address = document.createElement('p');
            title_mac_address.className = 'text-muted my-0';
            title_mac_address.innerHTML = 'MAC adresa mikrokontrolera';
            let mac_address_span = document.createElement('p');
            mac_address_span.className = 'text-muted';
            mac_address_span.innerHTML = item.controller_info.mac_address;
            // Append childs
            mac_address.appendChild(title_mac_address);
            mac_address.appendChild(mac_address_span);
            uC_header.appendChild(mac_address);
            device_container.appendChild(uC_header);

            // Create checkbox (the "Active: " one)
            let checkbox_container = document.createElement('div');
            checkbox_container.className = 'w-100 text-center';
            checkbox_container.id = 'Active-checkbox';
            // Text "Active: "
            let text_active = document.createElement('label');
            text_active.className = 'pr-3 my-0';
            text_active.innerHTML = 'Aktivan: ';
            // Create checkbox
            let active_checkbox = document.createElement('input');
            active_checkbox.type = 'checkbox';
            active_checkbox.checked = item.controller_info.active;
            // On click sent POST request if microcontroller is active
            active_checkbox.addEventListener('click', function (){
                let data = {"controler_id":item.controller_info.mac_address}
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
            // Append childs
            checkbox_container.appendChild(text_active);
            checkbox_container.appendChild(active_checkbox);

            device_container.appendChild(checkbox_container);

            // Create "Change microcontroller name"
            let uC_name_container = document.createElement('div');
            uC_name_container.className = 'input-group p-3 mt-3';
            uC_name_container.id = 'Change-microcontroller-name';
            // Header text div
            let header_text_div = document.createElement('div');
            header_text_div.className = 'w-100 text-left';
            header_text_div.id = 'Header_text_div';
            // Header text
            let text_current_name = document.createElement('p');
            text_current_name.className = 'text-muted mb-2';
            text_current_name.innerHTML = 'Trenutno ime mikrokontrolera:';
            header_text_div.appendChild(text_current_name);
            uC_name_container.appendChild(header_text_div);
            // Input field
            let uC_name_input = document.createElement('input');
            uC_name_input.className = 'form-control';
            if (item.controller_info.controller_name){
                uC_name_input.placeholder = item.controller_info.controller_name;
            }
            else {
                uC_name_input.placeholder = 'Dodaj ime mikrokontroleru';
            }
            uC_name_input.type = 'text';
            uC_name_input.id = item.controller_info.mac_address;
            uC_name_container.appendChild(uC_name_input);
            // Input field button
            let input_btn = document.createElement('div');
            input_btn.className = 'input-group-append';
            let btn = document.createElement('button');
            btn.className = 'btn btn-outline-success';
            btn.type = 'button';
            btn.innerHTML = 'Promijeni';
            btn.addEventListener('click', function (){
                let new_name = document.getElementById(item.controller_info.mac_address).value
                data = {"controler_id":item.controller_info.mac_address, "new_name":new_name}
                $.ajax({
                    data : data,
                    type : 'POST',
                    url : 'update-controller-name'
                    }).done(function () {
                        console.log('Name change successful')
                    });
            });
            // Append childs
            input_btn.appendChild(btn);
            uC_name_container.appendChild(input_btn);
            device_container.appendChild(uC_name_container);

            // Create control table
            let control_table = document.createElement('table');
            control_table.className = 'table table-hover mb-0';

            // Add table head
            let thead = document.createElement("thead");
            let pin_embeded_name = document.createElement("th");
            pin_embeded_name.innerHTML = 'Embeded name';
            thead.appendChild(pin_embeded_name);
            let used_for = document.createElement("th");
            used_for.innerHTML = 'Friendly name';
            thead.appendChild(used_for);
            let text_cell = document.createElement("th");
            text_cell.className = 'text-right';
            text_cell.innerHTML = 'Active';
            thead.appendChild(text_cell);
            control_table.appendChild(thead);

            let table_body = document.createElement("tbody");
            item.pins.forEach(function (element){
                if (element.io_type === 'OUTPUT') {
                    // table row creation
                    let row = document.createElement("tr");

                    // Create pin_embeded_name text container
                    let text_cell = document.createElement("td");
                    let embeded_name = document.createElement('label');
                    embeded_name.innerHTML = element.embeded_pin_name;
                    text_cell.appendChild(embeded_name);

                    // Create human readable name container
                    let human_readable_name = document.createElement("td");
                    human_readable_name.className = 'text-muted';
                    let readable_name = document.createElement('label');
                    readable_name.innerHTML = '[' + element.used_for + ']';
                    human_readable_name.appendChild(readable_name);

                    // Create checkbox container
                    let checkbox_cell = document.createElement("td");
                    checkbox_cell.className = 'text-right';
                    let active_checkbox = document.createElement('input');
                    active_checkbox.type = 'checkbox';
                    active_checkbox.checked = element.active;
                    active_checkbox.addEventListener('click', function (){
                        let data = {"element_id":element.id}
                        if (active_checkbox.checked === true){
                            $.ajax({
                                data : data,
                                type : 'POST',
                                url : 'activate-pin'
                            }).done(function () {
                                console.log('pin activated')
                            });
                        }
                        else {
                            $.ajax({
                                data : data,
                                type : 'POST',
                                url : 'deactivate-pin'
                            }).done(function () {
                                console.log('pin deactivated')
                            });
                        }
                    });

                    checkbox_cell.appendChild(active_checkbox);

                    row.appendChild(text_cell);
                    row.appendChild(human_readable_name);
                    row.appendChild(checkbox_cell);

                    //row added to end of table body
                    table_body.appendChild(row);
                }

                // append the <tbody> inside the <table>
                control_table.appendChild(table_body);
            });

            // Add childs
            device_container.appendChild(control_table);

            // Add device container to main container
            all_devices.appendChild(device_container);
            });
        });
})