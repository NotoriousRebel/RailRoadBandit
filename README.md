# RailRoadBandit

This tool allows you to read arbitrary files from vulnerable web servers that run ruby on rails. 

The only thing you need is Python 3.x

Then install shodan and requests

```pip3 install -r requirements.txt```

### This tool uses Shodan API 

This tool requires a Shodan API key

## To use Docker

```bash
git clone https://github.com/NotoriousRebel/RailRoadBandit
cd RailRoadBandit
# place shodan key 
docker build -t railbandit .  
docker run -it railbandit
```

