<div align="center">
<h1>Bank ATM</h1>
<b>💰 Neat, Simple and Deployable</b>
</div>

![atm_login](previews/atm_login.png)

## Index
- [Contributors](#contributors)
- [Bank ATM](#)
    - [Feasibility Study](#feasibility-study)
    - [Requirements](#requirements)
        - [Functional](#functional)
        - [Non-functional](#non-functional)
    - [Use-Case Model](#use-case-model)
    - [Installation](#installation)
    - [Deployment](#deployment)
        - [Localhost](#via-localhost)
        - [Local Network](#via-local-network)

## Contributors:
- [Mark Grass](https://github.com/blade-of-grass)
- [Anthony Nguyen](https://github.com/AnthonyN3)
- [Nuha Aljammas](https://github.com/Nuha-Aljammas)
- [Eric Yeung](#contributors)

## Feasibility Study

- Automated Teller Machines (ATM) are widely used in the world. 
- They are useful since they can be used any time of the day!
- This project is minimalist, simple and straight forward.

## Requirements

The features and requirmement specifications of this project.

### Functional

- Create Account
- Sign Into Account
- Withdraw Funds
- Deposit Funds
- Change Pin
- Transaction Limits

### Non-Functional

- **Intuitive:** needs to be easy to use without much thinking
- **Simple:** needs to perform as an ATM without extra fluff
- **Fast:** slow websites are not ideal especially ones that deals with funds
- **Accessible:** distributing the system over a network provides access to all

## Use-Case Model

![use_case_model](previews/use_case_model.png)

## Installation

1. Get **python3**
2. Get **django**
3. **Clone** this repository or **download** as a zip

It's that simple :>

## Deployment

After downloading and installing the repo there are two main ways to deploy this ATM.

- **Localhost:** The ATM is only accessible to the device running it.
- **Local Network:** The ATM is accessible to any devices on the same network.

### Via Localhost

Using your terminal navigate into the ATM project and run the following command:

```console
username@device:~/atm-main$ python3 manage.py runserver
```

This will deploy the ATM onto your localhost and can be accessed by going to `http://127.0.0.1:8000/`.

### Via Local Network

To deploy onto your local network you will need to add the ip of the device that will be hosting this ATM into ``settings.py``.

1. Get your devices IP address  
2. In the ATM project go to the file `atm-main\atm\settings.py`
3. locate `ALLOWED_HOSTS = []` and add your devices ip into it `(eg. ALLOWED_HOSTS = ['192.168.1.145'])`

Note: Alternatively, you can add `device_name.local` into the allowed hosts or even do `ALLOWED_HOSTS = ['*']` instead of finding your devices IP address.

Using your terminal navigate into the ATM project and run the following command:

```console
username@device:~/atm-main$ python3 manage.py runserver 0.0.0.0:8000
```

This will deploy the ATM onto your local network and can be accessed by any devices on the same network by going to 
`http://ip_address_of_host:8000/` or `http://device_name_of_host.local:8000/`.