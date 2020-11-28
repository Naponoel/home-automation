$(function () {
    $.ajax({
        type: 'POST',
        url: 'get-active-microcontrollers'
    }).done(function (data) {
        console.log(data);
        let parsed = JSON.parse(data);
        console.log(parsed);
        // let microcontroller_keys = Object.keys(parsed);
        //
        // microcontroller_keys.forEach(function (key){
        //     let microcontroller_pin_values = parsed[key];
        //     console.log(microcontroller_pin_values);
        //
        //     let microcontroller_pin_value_keys = Object.keys(parsed[key]);
        //     console.log(microcontroller_pin_value_keys);
        //
        //     // microcontroller_pin_value_keys.forEach(function (key){
        //     //     let pin_data = microcontroller_pin_values[key]
        //     //
        //     //     console.log(pin_data.embeded_pin_name);
        //     //     // if (pin_data.active === false){
        //     //     //     console.log(pin_data.embeded_pin_name);
        //     //     // }
        //     // });
        // });

            // Object.values(item).forEach(function (ite){
            //     console.log(ite)
            // });

            // let thread = document.createElement("table");
            // let table = document.createElement("table");


            // let head_text_div = document.createElement('div');
            // head_text_div.className = 'w-100 py-3 text-center';
            //
            // let header_text = document.createElement('span');
            // header_text.className = 'text-muted p-2 float-left';
            // header_text.innerHTML = item.controller_name;
            // head_text_div.appendChild(header_text);
            //
            // microcontrollers.appendChild(head_text_div);
        });
    });
// });