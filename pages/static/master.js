function copyEmail() {
    navigator.clipboard.writeText("xmevans@umich.edu");
    x = document.getElementsById("success-alert");
    if (x.style.display === "none") {
        x.style.display = "block";
    } else {
        x.style.display = "none";
    }
}