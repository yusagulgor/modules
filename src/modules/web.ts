
// ? 2024y05m01d (Yüşa Mervan Gülgör)

import http from 'http';
import express from 'express';

interface WebData {
  bgColor: number[];
  elements: string[];
  elementsText: string[];
  // footer: boolean;
  modelname: string;
  name: string;
  // navbar: boolean;
  textColor: number[];
  port:number;
}

let users: { [username: string]: string } = {};

const fetchData = () => {
  const options = {
    hostname: '127.0.0.1',
    port: 8000,
    path: '/api/data',
    method: 'GET',
  };

  const req = http.request(options, (res) => {
    console.log(`statusCode: ${res.statusCode}`);

    let rawData = '';

    res.on('data', (chunk) => {
      rawData += chunk;
    });

    res.on('end', () => {
      try {
        const data: WebData = JSON.parse(rawData);
        // console.log('Received data:', data);
        sendHtmlToServer(data);
      } catch (err) {
        console.error('Error parsing JSON data:', err);
      }
    });
  });

  req.on('error', (error) => {
    console.error('Error fetching data:', error);
  });

  req.end();
};

const sendHtmlToServer = (data: WebData) => {
  const app = express();

  const port = 8001;

  // ! This code is for readyweb and webdev

  if (data["modelname"] === "LoginRegister" || data["modelname"] === "BasicCustom") {
    data.elements.forEach((element, index) => {
      const prevElement = index > 0 ? data.elements[index - 1] : data.elements[data.elements.length - 1];
      app.get(`/${element}`, (req, res) => {
        const navbarHTML = `<nav><ul><li><a href="/${prevElement}">${prevElement}</a></li></ul></nav>`;
        const contentHTML = `<div id="content"><p>${data.elementsText[data.elements.indexOf(element)]}</p></div>`;
        const footerHTML = '<footer>Footer Content</footer>';

        const html = `
          <!DOCTYPE html>
          <html>
            <head>
              <title>${data.name}</title>
              <style>
                body {
                  background-color: rgb(${data.bgColor.join(', ')});
                  color: rgb(${data.textColor.join(', ')});
                }
                ul {
                  list-style-type: none;
                  margin: 0;
                  padding: 0;
                  overflow: hidden;
                  background-color: #333;
                }
                
                li {
                  float: left;
                }
                
                li a {
                  display: block;
                  color: white;
                  text-align: center;
                  padding: 14px 16px;
                  text-decoration: none;
                }
                
                /* Change the link color to #111 (black) on hover */
                li a:hover {
                  background-color: #111;
                }
  
                footer {
                  position: fixed; /* Sayfanın altında sabit kalacak */
                  bottom: 0; /* Sayfanın altına yaslanacak */
                  width: 100%; /* Footer'ın genişliği sayfanın tamamını kaplayacak */
                  text-align: center;
                  padding: 3px;
                  background-color: DarkSalmon;
                  color: black;
                }
              </style>
            </head>
            <body>
              ${navbarHTML} <!-- Navbar HTML eklendi -->
              ${contentHTML} <!-- İçerik eklendi -->
              ${footerHTML}
            </body>
          </html>
        `;

        res.send(html);
        // console.log('HTML content sent to client:', html);
      });
    });

    app.get('/register', (req, res) => {
      const username = req.query.username as string;
      const password = req.query.password as string;
      users[username] = password;
      res.send('Kullanıcı kaydedildi.');
    });

    app.get('/login', (req, res) => {
      const username = req.query.username as string;
      const password = req.query.password as string;
      if (users[username] && users[username] === password) {
        res.redirect(`/${data.elements[0]}`);
      } else {
        res.send('Kullanıcı adı veya şifre yanlış.');
      }
    });

    if (data["modelname"] === "LoginRegister") {
      const LRhtml = `
      <!DOCTYPE html>
      <html lang="en">
      
      <head>
          <meta charset="UTF-8">
          <meta name="viewport" content="width=device-width, initial-scale=1.0">
          <title>Login / Register</title>
          <style>
              body {
                  font-family: Arial, sans-serif;
                  background-color: #f4f4f4;
                  margin: 0;
                  padding: 0;
                  display: flex;
                  justify-content: center;
                  align-items: center;
                  height: 100vh;
              }
      
              .container {
                  background-color: #fff;
                  padding: 20px;
                  border-radius: 5px;
                  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
              }
      
              h2 {
                  text-align: center;
                  margin-bottom: 20px;
              }
      
              input[type="text"],
              input[type="password"],
              input[type="submit"] {
                  width: 100%;
                  padding: 10px;
                  margin-bottom: 15px;
                  border: 1px solid #ccc;
                  border-radius: 5px;
                  box-sizing: border-box;
              }
      
              input[type="submit"] {
                  background-color: #4caf50;
                  color: white;
                  cursor: pointer;
              }
      
              input[type="submit"]:hover {
                  background-color: #45a049;
              }
      
              .form-group {
                  margin-bottom: 20px;
              }
      
              .form-group:last-child {
                  margin-bottom: 0;
              }
      
              .form-group label {
                  display: block;
                  margin-bottom: 5px;
                  font-weight: bold;
              }
          </style>
      </head>
      
      <body>
      
          <div class="container">
              <h2>Login</h2>
              <form action="/login" method="GET">
                  <div class="form-group">
                      <label for="username">Username:</label>
                      <input type="text" id="username" name="username" required>
                  </div>
                  <div class="form-group">
                      <label for="password">Password:</label>
                      <input type="password" id="password" name="password" required>
                  </div>
                  <input type="submit" value="Login">
              </form>
      
              <hr>
      
              <h2>Register</h2>
              <form action="/register" method="GET">
                  <div class="form-group">
                      <label for="newUsername">Username:</label>
                      <input type="text" id="newUsername" name="username" required>
                  </div>
                  <div class="form-group">
                      <label for="newPassword">Password:</label>
                      <input type="password" id="newPassword" name="password" required>
                  </div>
                  <input type="submit" value="Register">
              </form>
          </div>
      
      </body>
      
      </html>
      `;

      app.get(`/LoginRegister`, (req, res) => {
        res.send(LRhtml);
      });
    }
  }

  app.listen(port, () => {
    if (data["modelname"] === "LoginRegister") {
      console.log(`Server is running at http://127.0.0.1:8001/LoginRegister`);
    } else {
      console.log(`Server is running at http://127.0.0.1:8001/${data.elements[0]}`);
    }

  });
};

fetchData();
