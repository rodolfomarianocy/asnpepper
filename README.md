# Help
![image](https://user-images.githubusercontent.com/54555784/188523522-3a373814-3c55-4117-ac96-5cae43189e6d.png)

## Usage

### View organization CIDRs by searching the ASN's and save in a txt
```
python asnpepper.py -o <org> -O output.txt
```
![asnpepper](https://user-images.githubusercontent.com/54555784/188524712-362d65a0-c9b0-4928-9ee3-f52f0b59e7df.png)

### View organization CIDR IPs by searching ASNs and save in a txt
```
python asnpepper.py -o <org> --show-ip -O output.txt
```
### Port scan a certain port on all ASN IP's in an organization
```
python asnpepper.py -o <org> --test-port 80,443
```
### Fetch Git Exposed on all an organization's ASN IP's on port 80
```
python asnpepper.py -o <org> --test-git
```
### It is also possible to set the number of threads to --test-git or --test-port which by default is 1000
```
python asnpepper.py -o <org> --test-port 80 -t 2000
```
## Install Linux 
```
sudo apt install chromium-driver && pip install selenium
```
## Install Windows  
```
pip install selenium webdriver_manager
```
