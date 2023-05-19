# Pancakeswap Pool deployment script


## Dependencies
```bash
pip install -r requirements.txt
```

## initialize.py

It creates a job to deploy Pancakeswap pool via Pancakeswap Factory. This is already run so you don't run it again.

## main.py

It executes a job to deploy Pancakeswap pool via Pancakeswap Factory. The token to be paired should be put as an argument. For example, to create BSC_USDT - GRAIN pair, run the script as follows.
```bash
python main.py 0x55d398326f99059fF775485246999027B3197955
```
