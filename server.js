var express = require('express');

const dogs = [
  {
    id: 1,
    breed: 'pembroke-welsh-corgi',
    name: 'charles'
  },
  {
    id: 2,
    breed: 'pug',
    name: 'cheese'
  },
  {
    id: 3,
    breed: 'dachshund',
    name: 'ralph'
  }
];

const cats = [
  {
    id: 1,
    breed: 'ragdoll',
    name: 'mimi'
  },
  {
    id: 2,
    breed: 'siamese',
    name: 'mocha'
  },
  {
    id: 3,
    breed: 'russian-blue',
    name: 'bean'
  }
];

var app = express();

app.get('/dogs', (req, res) => {
  res.status(200).json(dogs);
});

app.get('/cats', (req, res) => {
  res.status(200).json(cats);
});

app.get('/dogs/:id', (req, res) => {
  let id = req.params.id;
  let response = dogs.find((item) => item.id == id);

  res.status(200).json(response);
});

app.get('/cats/:id', (req, res) => {
  let id = req.params.id;
  let response = cats.find((item) => item.id == id);

  res.status(200).json(response);
});

app.listen(8080, () => {
  console.log('Server running on port 8080');
});
