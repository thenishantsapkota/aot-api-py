# Attack on Titan Quotes API

A port over version of https://github.com/thestuti/aot-api from JavaScript to Python

:globe_with_meridians: Website and Demo -> https://aot-api-py.herokuapp.com/

# Setup

Setting up the API for use:

```bash
git clone https://github.com/thenishantsapkota/aot-api-py

cd aot-api-py

poetry shell

poetry install

# Run the migration script the first time

python -m migrations

uvicorn aot_quotes.main:app --reload
```

## Contributing

Add lines in `/seed/data.txt` to suggest more AOT Quotes and create a Pull Request.
