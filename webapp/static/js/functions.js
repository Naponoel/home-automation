function showHide() {
    console.log('hehe')
    let x = document.getElementById("komponenta");
    if (x.style.display === "none") {
        x.style.display = "block";
    }
    else {
        x.style.display = "none";
    }
}