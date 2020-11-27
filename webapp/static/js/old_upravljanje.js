$(function() {
    // Pitaj bazu da ti kaze koje sve pinove treba prikazati
    // Pitaj bazu koja su trenutna stanja pinova i stavi razlicite animacije za ON/OFF
    const controllersDiv = document.getElementById("container-landing");
    const addPinBtn = document.createElement('button');
    addPinBtn.innerHTML = 'Gumber';
    addPinBtn.className = 'btn btn-outline-success my-4';
    controllersDiv.appendChild(addPinBtn);
    addPinBtn.addEventListener('click', function () {
        $.ajax({
                type : 'POST',
                url : 'switch',
                success: function (data) {
                    console.log(data);
                }
        });
    });
});