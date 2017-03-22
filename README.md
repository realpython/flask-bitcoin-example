# Flask Bitcoin

Build an app that will find the best exchange rates for Bitcoin (USD -> Bitcoin)  from the following cryptocurrency exchanges:

1. [Bitstamp](https://www.bitstamp.net/)
1. [YoBit](https://yobit.net/)
1. [Bittrex](https://bittrex.com/)

It should have the following pages:

1. The first page should display the rates and highlight the best one
1. The second page should display the rates over time

## Getting Started

1. Fork/Clone
1. Create and activate a virtualenv
1. Install dependencies
1. Create the db - `python create_db.py`

### Sanity Check

1. Grab data - `python data.py`
1. Run the app - `python app.py` and then navigate to - [http://localhost:8080/data](http://localhost:8080/data) and you should see something like:

  ```json
  [
    {
      "exchange": "bitstamp",
      "price": 1201.37,
      "time": 1201.37
    }
  ]
  ```

Kill the server once done.

### Run

```
$ sh run.sh
```

This will run *data.py* to collect data and then run the server in the background. Check [http://localhost:8080/data](http://localhost:8080/data) to make sure it's working. You should also see `got data` outputs in the terminal whenever data is collected.
