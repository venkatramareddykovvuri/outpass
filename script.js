function generateOTP() {
    let roll = document.getElementById("rollno").value;
    let pass = document.getElementById("password").value;
    let type = document.getElementById("type").value;

    fetch("http://localhost:8000/generate", {
        method: "POST",
        body: JSON.stringify({rollno: roll, password: pass, type: type})
    })
    .then(res => res.text())
    .then(data => alert(data));
}

function verifyOTP() {
    let roll = document.getElementById("verifyRoll").value;
    let otp = document.getElementById("otp").value;

    fetch("http://localhost:8000/verify", {
        method: "POST",
        body: JSON.stringify({rollno: roll, otp: otp})
    })
    .then(res => res.text())
    .then(data => alert(data));
}
let wardenLoggedIn = false;

function wardenLogin() {
    let user = document.getElementById("wardenUser").value;
    let pass = document.getElementById("wardenPass").value;

    fetch("http://localhost:8000/warden_login", {
        method: "POST",
        body: JSON.stringify({username: user, password: pass})
    })
    .then(res => res.text())
    .then(data => {
        alert(data);
        if (data.includes("Success")) {
            wardenLoggedIn = true;
        }
    });
}

function verifyOTP() {
    if (!wardenLoggedIn) {
        alert("⚠️ Warden Login Required");
        return;
    }

    let roll = document.getElementById("verifyRoll").value;
    let otp = document.getElementById("otp").value;

    fetch("http://localhost:8000/verify", {
        method: "POST",
        body: JSON.stringify({rollno: roll, otp: otp})
    })
    .then(data => {
    alert(data);

    if (data.includes("APPROVED")) {
        localStorage.setItem("outpass", data);
        window.open("outpass.html");
    }
});
}