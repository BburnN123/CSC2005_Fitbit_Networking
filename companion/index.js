import * as messaging from "messaging";

messaging.peerSocket.onopen = () => {
  console.log("Companion Connected");
  sendMessage();
}

messaging.peerSocket.onerror = (err) => {
  console.log(`Connection error: ${err.code} - ${err.message}`);
}

messaging.peerSocket.onmessage = (evt) => {
  console.log(JSON.stringify(evt.data));
  fetch("http://10.0.0.138:9090/", {method:"POST", body:JSON.stringify(evt.data)})
    .then(function(resp) {
    console.log("connected");
  })
    .catch(function (error) {
    console.log("error");
  });
}

function sendMessage() {
  if (messaging.peerSocket.readyState === messaging.peerSocket.OPEN) {
    // Send the data to peer as a message
    messaging.peerSocket.send({
      sampleData: 123456
    });
  }
}