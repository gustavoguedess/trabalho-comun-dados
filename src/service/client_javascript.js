const axios = require("axios");

const api = axios.create({
  baseURL: "http://localhost:8000/",
});

function decode ( message ) {
    URL = "decode/"
    const options = {
        method: 'GET',
        url: URL,
        headers: {'Content-Type': 'application/json'},
        data: {
          message: message
        }
      };
      
    return api.request(options)
        .then(res => res.data)
        .catch(err => console.log("Erro Decode"));
}

function listen (username) {
    URL = "listen/"+username
    console.log(URL);

    return api.get(URL)
        .then(response => response.data)
        .catch(err => console.log("Erro listen"));
};

function encode ( message ){
    URL = "encode/"
    const options = {
        method: 'GET',
        url: URL,
        headers: {'Content-Type': 'application/json'},
        data: {
          message: message
        }
    };
    console.log(message);
    return api.request(options)
        .then(res => res.data)
        .catch(err => console.log("Erro Encode"));
}

function send_message (origin_username, dest_username, message){
    URL = "send/"+origin_username+"/"+dest_username;

    const options = {
        method: 'POST',
        url: URL,
        headers: {'Content-Type': 'application/json'},
        data: {
            message: message
        }
    };
    
    return api.request(options)
        .then(res => res.data)
        .catch(err => console.log("Erro Send Message"));
}


async function teste(){
    var res_listen = await listen("a")
    console.log(res_listen);
    
    var res_decode = await decode(res_listen.message)
    console.log(res_decode);
};

async function teste2(){
    var res_encode = await encode("testando")
    console.log(res_encode);

    var res_send = await send_message("guedes", "a", res_encode.encoded)
    console.log(res_send);
}

