# ASNPepper - Recon in ASN - Extracting CIDR's - Fast and efficient scanning

## Help
<img height="300em" src="https://user-images.githubusercontent.com/54555784/188523522-3a373814-3c55-4117-ac96-5cae43189e6d.png" />

## Usage

### View organization CIDRs by searching the ASN's and save in a txt
```
python asnpepper.py -o <org> -O output.txt
```
<img height="200em" src="https://user-images.githubusercontent.com/54555784/188524712-362d65a0-c9b0-4928-9ee3-f52f0b59e7df.png" />

### View organization CIDR IPs by searching ASNs and save in a txt
```
python asnpepper.py -o <org> --show-ip -O output.txt
```
<img height="200em" src="https://user-images.githubusercontent.com/54555784/188536672-a53443d7-a6a4-415f-854c-7d90e8044590.png" />

### Port scan a certain port on all ASN IP's in an organization
```
python asnpepper.py -o <org> --test-port 80,443
```
<img height="200em" src="https://user-images.githubusercontent.com/54555784/188536782-943242f8-414e-4331-87ac-1f688f1c060d.png" />

### Fetch Git Exposed on all an organization's ASN IP's on port 80
```
python asnpepper.py -o <org> --test-git (in development and testing phase)
```
### It is also possible to set the number of threads to --test-git or --test-port which by default is 1000
```
python asnpepper.py -o <org> --test-port 80,443 -t 2000
```
## Install Linux 
```
sudo apt install chromium-driver && pip install selenium
```
## Install Windows  
```
pip install selenium webdriver_manager
```

References:
https://rodolfomarianocy.medium.com/recon-em-asns-262a7f7b9297
