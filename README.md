arXiv number extraction
=======================

Basic example scripts for extracting numbers from arXiv fulltext posts.

Usage
-----


1. Sign up for Amazon web services
2. Install the aws cli tool (version 2)
3. run `aws configure` and input the access tokens you generate from the aws site
4. Run `aws s3 ls arxiv/src/ --request-payer requester` to get a list of the available tar files
5. Download the ones you want with `aws s3 cp s3://arxiv/src/arXiv_src_9902_001.tar ./arXiv_src_9902_001.tar --request-payer requester` and extract with `tar xvf` or something
6. Modify and use `open.py [directory name]` to run over the gzipped files and find numbers in papers.

the simple scripts `list.sh` and `get.sh` automate some of this.

Eg run
```
./list.sh
```
pick a file you want like `arXiv_src_1801_012.tar` and run
```
./get.sh arXiv_src_1801_012.tar
python3 open.py 1801
```

