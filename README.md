# RailRoadBandit

This tool allows you to read arbitrary files from vulnerable web servers that run ruby on rails. 
## CVE-2019-5418

Due to ruby renders files this allows for file content disclosure.
Specially crafted accept headers in combination with calls to 'render file'
can cause arbitrary files on the target server to be rendered, disclosing file contents.

To read more visit: [More Information on CVE](https://chybeta.github.io/2019/03/16/Analysis-for%E3%80%90CVE-2019-5418%E3%80%91File-Content-Disclosure-on-Rails/)

The only thing you need is Python.

Then install requests

```pip3 install requests or pip install requests```

## TODO

##### Integrate Shodan


## To use Docker

```bash
git clone https://github.com/NotoriousRebel/RailRoadBandit
cd RailRoadBandit
# place shodan key 
docker build -t railbandit .  
docker run -it railbandit
```
