$(function () {
    $.ajax({
        type: 'POST',
        url: 'get-active-microcontrollers'
    }).done(function (data) {
        let parsed = JSON.parse(data);
        console.log(parsed);

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