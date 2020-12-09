$(function () {
    $.ajax({
        type: 'POST',
        url: 'get-active-microcontrollers'
    }).done(function (data) {
        let main_container = document.getElementById('devices');
        let parsed = JSON.parse(data);

        parsed.forEach(function (microcontroler_obj) {
            let pins = microcontroler_obj.pins

            let controller_container = document.createElement('div');
            controller_container.className = 'border';
            controller_container.id = 'controller_container';


            let span_container = document.createElement('div');
            span_container.className = 'text-center my-5';
            let controller_name = document.createElement('span');
            controller_name.innerHTML = microcontroler_obj.controller_info.controller_name;
            span_container.appendChild(controller_name);
            controller_container.appendChild(span_container);

            pins.forEach(function (pin) {
                // Create button container
                let btn_container = document.createElement('div');
                btn_container.className = 'w-100 pb-4 px-5';
                let pin_object = document.createElement('button');

                // Get initial pin state
                let data = {"pin_id":pin.id}
                $.ajax({
                        type: 'POST',
                        data: data,
                        url: 'get-pin-state'
                    }).done(function (data) {
                        // console.log(data)
                        pin_object.current_value = data.db_state;
                        if (pin_object.current_value === 0){
                            pin_object.className = "btn btn-secondary w-100";
                        }
                        else {
                            pin_object.className = "btn btn-warning w-100";
                        }
                    });
                btn_container.appendChild(pin_object);
                controller_container.appendChild(btn_container);

                if (pin.used_for !== null){
                    pin_object.innerHTML = pin.used_for;
                }
                else{
                    pin_object.innerHTML = "Unknown";
                }

                pin_object.addEventListener('click', function () {
                    // console.log(pin_object.current_value);
                    let data;
                    if (pin_object.current_value === 0){
                        data = {
                            'controller_mac':microcontroler_obj.controller_info.mac_address,
                            'wanted_pin_value':1,
                            'pin_id':pin.id,
                            'embeded_id':pin.embeded_pin_name
                        }
                    }
                    else{
                        data = {
                            'controller_mac':microcontroler_obj.controller_info.mac_address,
                            'wanted_pin_value':0,
                            'pin_id':pin.id,
                            'embeded_id':pin.embeded_pin_name
                        }
                    }
                    $.ajax({
                        type: 'POST',
                        data: data,
                        url: 'switch-pin-state'
                    }).done(function (response) {
                        // console.log(data.new_value)
                        pin_object.current_value = data.wanted_pin_value;
                    if (pin_object.current_value === 0){
                        pin_object.className = "btn btn-secondary w-100";
                    }
                    else {
                        pin_object.className = "btn btn-warning w-100";
                    }
                    });
                });
            });
            main_container.appendChild(controller_container);
        });
    });
});