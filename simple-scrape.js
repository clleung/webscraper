/**
 * scraper-javascript.js
 * code by Joe Osborne, https://medium.com/@joerosborne/intro-to-web-scraping-build-your-first-scraper-in-5-minutes-1c36b5c4b110
 * To run this script, copy and paste `node scraper-javascript.js` in the terminal
 */

const cheerio = require('cheerio');



(async () => {
    const url = 'https://www.example.com';
    const response = await fetch(url);

    const $ = cheerio.load(await response.text());
//   console...html prints the entire page
//   console.log($.html());
    const title = $('h1').text();
    const text = $('p').text();
    const link = $('a').attr('href');

    console.log(title);
    console.log(text);
    console.log(link);

})();