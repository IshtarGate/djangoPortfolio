# Django Portfolio

This is my portfolio for my work at MAXX Potential.

It was build using Django.

# Dev Guide

## Setup Assuming This Is The First Time

- Clone the repository
    
    `git clone https://github.com/IshtarGate/djangoPortfolio.git`

- Create a folder for virtual environments.

    `mkdir ~/.virtualenvs`
- Create a Python3 virtual environment.
    ```
    virtualenv --python=`which python3` ~/.virtualenvs/djamesPortfolio
    ```
    - `/djamesPortfolio` can be anything you want
- Activate the virtual environment.
    
    `. ~/.virtualenvs/djangodev/bin/activate`

- Install Django
    - `git clone git://github.com/django/django.git`
    - `pip install -e django/`
        - Where `django/` is the Django repository.
