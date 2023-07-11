// start: express
const express = require('express');
const app = express();
const port = 3000;
// end: express

// start: prometheus
const prom = require('prom-client');
const collectDefaultMetrics = prom.collectDefaultMetrics;
collectDefaultMetrics({});

app.get('/metrics', async function (req, res) {
  res.set('Content-Type', prom.register.contentType);
  const r = await prom.register.metrics();
  res.write(r);
  res.end();
});

const PROM_GET_HELLO = new prom.Summary({
  name: 'get_hello_seconds',
  help: 'Time spent processing GET / request',
});

const PROM_GET_SLOW = new prom.Summary({
  name: 'get_slow_seconds',
  help: 'Time spent processing GET /api/slow request',
});
// end: prometheus

// utility
function sleep(time) {
  return new Promise(resolve => setTimeout(resolve, time));
}
function getRandomInt(min, max) {
  min = Math.ceil(min);
  max = Math.floor(max);
  return Math.floor(Math.random() * (max - min + 1)) + min;
}

app.get('/', async (req, res) => {
  // PROMETHEUS: start tracking time
  const end =  PROM_GET_HELLO.startTimer();

  // actual logic
  res.send('Hello World!');

  // PROMETHEUS: start tracking time
  end();
});

app.get('/api/slow', async (req, res) => {
  // PROMETHEUS: start tracking time
  const end =  PROM_GET_SLOW.startTimer();

  // actual logic
  const v = getRandomInt(1, 4);
  await sleep(v * 1000);
  res.send('I slept for ' + v + ' seconds!');

  // PROMETHEUS: start tracking time
  end();
});

app.listen(port, () => { console.log(`Example app listening on port ${port}`); });
