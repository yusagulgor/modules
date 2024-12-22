import express from 'express';
const app = express();
const port = 5000;

interface Text {
  type: string;
  color: string;
  text: string;
}

interface Card {
  type: string;
  fyt: string;
  wh: [number, number];
  border_radius: number;
  bgColor: string;
  texts: Text[];
}

interface Navbar {
  bgColor: string;
  links: Text[];
}

interface Footer {
  bgColor: string;
  text: Text;
}

interface Page {
  name: string;
  elements: (Card | Text)[];
}

interface WebData {
  name: string;
  navbar: Navbar;
  footer: Footer;
  pages: Page[];
}

fetch('http://127.0.0.1:8000/api/apy')
  .then(response => response.json())
  .then((data: WebData) => {

    data.pages.forEach((page) => {
      app.get(`/${page.name}`, (req, res) => {
        res.send(`
          <html>
            <head>
              <title>${page.name}</title>
              <style>
                body { font-family: Arial, sans-serif; background-color: #f5f5f5; margin: 0; padding: 0; }
                nav { background-color: ${data.navbar.bgColor}; padding: 10px; }
                nav ul { list-style-type: none; margin: 0; padding: 0; overflow: hidden; }
                nav ul li { float: left; margin-right: 15px; }
                nav ul li a { text-decoration: none; color: ${data.navbar.links[0]?.color}; }

                .card {
                  padding: 20px;
                  margin: 20px;
                  border-radius: ${page.elements[0] && 'border_radius' in page.elements[0] ? (page.elements[0] as Card).border_radius : 0}px;
                  background-color: ${page.elements[0] && 'bgColor' in page.elements[0] ? (page.elements[0] as Card).bgColor : 'transparent'};
                  display: flex;
                  flex-wrap: wrap;
                  gap: 10px; /* Card içindeki elemanlar arasında boşluk */
                }

                .card.single {
                  justify-content: center;
                  width: ${page.elements[0] && 'wh' in page.elements[0] ? (page.elements[0] as Card).wh[0] : 100}px;
                  height: ${page.elements[0] && 'wh' in page.elements[0] ? (page.elements[0] as Card).wh[1] : 100}px;
                }

                .card.double {
                  justify-content: space-between;
                  width: ${page.elements[0] && 'wh' in page.elements[0] ? (page.elements[0] as Card).wh[0] : 100}px;
                  height: ${page.elements[0] && 'wh' in page.elements[0] ? (page.elements[0] as Card).wh[1] : 100}px;
                }

                .card.triple-four {
                  display: grid;
                  grid-template-rows: repeat(2, 1fr);
                  grid-template-columns: repeat(2, 1fr);
                  width: ${page.elements[0] && 'wh' in page.elements[0] ? (page.elements[0] as Card).wh[0] : 100}px;
                  height: ${page.elements[0] && 'wh' in page.elements[0] ? (page.elements[0] as Card).wh[1] : 100}px;
                  gap: 10px; /* Grid içindeki elemanlar arasında boşluk */
                }

                .card a, .card p, .card h3 {
                  color: ${page.elements[0] && 'texts' in page.elements[0] && page.elements[0].texts.length > 0 ? (page.elements[0] as Card).texts[0]?.color : '#000'};
                  display: inline-block; /* Her öğeyi blok yaparak hizalamayı düzeltiyoruz */
                  margin: 0; /* Varsayılan margin değerlerini sıfırlıyoruz */
                }

                footer { background-color: ${data.footer.bgColor}; padding: 10px; text-align: center; position: fixed; width: 100%; bottom: 0; }
                footer p { color: ${data.footer.text.color}; }
              </style>
            </head>
            <body>
              <nav>
                <ul>
                  ${data.navbar.links.map(link => 
                    `<li><a href="${link.text}">${link.text}</a></li>`
                  ).join('')}
                </ul>
              </nav>
              <h1>${page.name}</h1>
              ${page.elements.map((element) => {
                if ('texts' in element) {
                  return `
                    <div class="card ${element.texts.length === 1 ? 'single' : 
                      element.texts.length === 2 ? 'double' : 
                      'triple-four'}">
                      ${element.texts.map(text => {
                        switch (text.type) {
                          case 'a':
                            return `<a href="${text.text}" style="color:${text.color};">${text.text}</a>`;
                          case 'h3':
                            return `<h3 style="color:${text.color};">${text.text}</h3>`;
                          case 'p':
                          default:
                            return `<p style="color:${text.color};">${text.text}</p>`;
                        }
                      }).join('')}
                    </div>
                  `;
                } else {
                  return `<p style="color:${element.color};">${element.text}</p>`;
                }
              }).join('')}
              <footer>
                <p>${data.footer.text.text}</p>
              </footer>
            </body>
          </html>
        `);
      });
    });

    app.listen(port, () => {
      console.log(`Server is running at http://localhost:${port}/${data.pages[0].name}`);
    });
  })
  .catch(error => {
    console.error('Error fetching data:', error);
});
