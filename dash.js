const car = document.getElementById("cards")

function createServer(servers){
    const div = document.createElement("div")
    div.className = servers.status === "UP" ? "card up" : "card down"
    div.innerHTML = `<p>url:${servers.url}</p><p>status:${servers.status}</p><p>ms:${servers.ms}</p>`;
    car.appendChild(div);
    }
fetch("status.json").then(response => response.json()).then(servers => {for (const server of servers) {
    createServer(server)
} })