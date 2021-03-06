# SpellingCorrectorApp

This is a spelling correction application for our thesis
## Installation
Create conda environment
```bash
conda create -n spellingcorrection python=3.7
```

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install requirements.

```bash
cd backend
python -m pip install -r requirements.txt
python -m pip install -e .
```

Download model checkpoint
```bash
# download tokenizer
cd autocorrection
mkdir input
mkdir input/luanvan
cd input/luanvan
gdown <link>
cd ../..

# download model
mkdir weights
mkdir weights/history
mkdir weights/model
gdown <link>
cd ../..

# download pretrained tokenization repair
cd tokenization_repair
mkdir data/estimators/
mkdir data/estimators/lm/
cd data/estimators
gdown https://drive.google.com/drive/folders/1zhtQmPTah7qneEHPHuFHuf3qd5R047-W -O / --folder
cd ../lm
gdown https://drive.google.com/drive/folders/1lG3swcUyUPYOf4ziJGfPQboaYtD5SgTM -O / --folder
```

## Usage

Run backend server
```bash
python app.py
```

Use postman to send a post request
```yaml
{
    "text": "hôm nay toi dihoc . cjpcsong rất là vui"
}
```
## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)