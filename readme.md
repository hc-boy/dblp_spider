# DBLP web crawler
a web crawler that is based on Crawl-ConOrJou
### Installation
```
    pip install scrapy
```

### Use
in input_dblp.py file，modify start_urls and year
```
    start_urls = []  # dblp homepage from needed conf/jou
    year = n  # Recent n years
```
Then we can begin
```
    # -o para stands for file format, it supports info.json, iofo.json1, info.csv, info.xml，for example:
    scrapy crawl dblp -o info.csv

    # suggested way
    scrapy crawl dblp -o info.json # will outputinfo.json as original file
    python json_to_xlsx.py # will output a file that we need: dblp_list_info
```

