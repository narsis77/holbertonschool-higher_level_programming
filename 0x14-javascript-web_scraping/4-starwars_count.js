#!/usr/bin/node

const request = require('request');

request(process.argv[2], function (err, res, body) {
  if (err) console.log(err);
  else {
    let wedgefilms = 0;
    let films = JSON.parse(body).results;
    for (let film in films) {
      characters = films[film].characters;
      for (let character in characters) {
	console.log(characters[character]);
	if (characters[character].search(/18\/$/) > -1) wedgefilms++;
      }
    }
    console.log(wedgefilms);
  }
});
