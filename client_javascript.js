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
      
      api.request(options).then(function (response) {
        console.log(response.data);
      }).catch(function (error) {
        console.error(error);
      });
}
function listen (username) {
    URL = "listen/"+username
    console.log(URL);

    api.get(URL)
        .then((res) => {
            console.log(res.data);
            decode(res.data.message);
            return res.data;
        })
        .catch(function (error) {
            console.log("error");
            return null;
        });
};

function send_message (origin_username, dest_username, message){
    URL = "encode/"
    const options = {
        method: 'GET',
        url: URL,
        headers: {'Content-Type': 'application/json'},
        data: {
          message: message
        }
    };
    
    api.request(options).then(function (response) {
        URL = "send/"+origin_username+"/"+dest_username;
        message = encode(message);
        console.log(message);

        const options = {
            method: 'POST',
            url: URL,
            headers: {'Content-Type': 'application/json'},
            data: {
                message: response.data.message
            }
        };
        console.log(options);
        api.request(options).then(function (response) {
            console.log(response.data);
        }).catch(function (error) {
            console.error("error");
        });

        return response.data;
    }).catch(function (error) {
        console.error(error);
    });

    
}


var data = send_message("guedes", "vanin", "testando");


