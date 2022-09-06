This tool is designed to look up CIDR of organization name, to save the results into an output file.

# Usage
![image](https://user-images.githubusercontent.com/54555784/188219497-a42b93c4-cab7-41d2-9225-25152529f223.png)
# Usage 

### View organization CIDRs by searching the ASN's and save in a txt
```
python asnpepper.py -o <org> -O output.txt
```
![image](https://user-images.githubusercontent.com/54555784/188293281-8bfa8d1c-820e-4478-8b80-fa01990757a6.png)

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
apt install chrome
## Install Windows  
```
pip install selenium webdriver_manager
```
