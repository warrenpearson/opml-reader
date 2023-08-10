## opml-reader

A simple utility for outputting the .opml output from CloudOutliner into more convenient formats.

Currently supports txt (with status) and csv (without status: TODO).

To run:

```bash
./build_env.sh

source venv/bin/activate

python3 opml_reader.py <your_data>.opml

cat <your_data>.txt
```
