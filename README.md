# La-Zanzara-Download
Python script to download all episodes of La Zanzara

> [!NOTE]  
> Project has been developed and tested with `python 3.11.8`


## How to use

First you have to clone the repository:

```bash
git clone https://github.com/giovannipollo/la-zanzara-download.git
```

Now, go in to the folder of the cloned repository:

```bash
cd la-zanzara-download
```

Now you can create a python virtual environment

```bash
python3 -m venv venv
```

Then, proceed by installing all the required packages:

```bash
pip3 install -r requirements.txt
```

Now you are ready to run the program:

```bash
python3 download.py --year 2023 --month 2 --day 20
```

With this command you can try to download the episode of the 20th of February 2023. 

In case you can to download a full month of a specific year, just don't specify the day.

```bash
python3 download.py --year 2023 --month 2
```

Even more, if you want to download a full year, don't specify neither the day nor the month.

```bash
python3 download.py --year 2023
```