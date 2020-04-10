# pyvanza
A simple Avanza scraper

!This scraper is not meant for real life applications and just fulfill a "proof of concept" tool.

## Introduction
Visiting fonds and stocks on Avanza will show you historical developments in your browser. Visiting website such as "https://www.avanza.se/aktier/om-aktien.html/293975/enzymatic" is a good example.

Interested in reading such numbers? Here is Python tool to help you with

## Installation
```
1) Run: git clone https://github.com/XeBoris/pyvanza pyvanza
2) Run: cd pyvanza
3) Run: make install
```
## Usage

### Terminal
Run it simply doing:
```
pyvanza --fond https://www.avanza.se/aktier/om-aktien.html/293975/enzymatic --from 2019-01-01 --to 2019-02-01 --out output
```
### Import to Python

```
import pyvanza

ps = pyvanza.AvanzaScraper()

fond_url = "https://www.avanza.se/aktier/om-aktien.html/293975/enzymatic"

dict = pw.GetFond(fond_url=fond_url, beg="2019-01-01", end="2019-02-01")

#if you are in a jupyter notebook:
dict.keys()


```

## A word on the output
That tool is by far not perfect. In the terminal, pyvanza creates a pickle file for you. If you are intend to use the tool in your Python application or Jupyter notebook, it returns a dictionary.

## Warning
Avanza does not support you with detailed information on historical information about stocks and fonds in the chart on the website. Receiving data on a monthly basis will return you daily values but time periods beyond one month will return 7 days periods (roughly). The resulting values are percentage and not stock or fond market values! Furthermore, the percentage values are normalized to the period of receiving the data. Going beyond (e.g. by connecting two months of received data) needs further normalization on your own!

   

