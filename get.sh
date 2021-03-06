#!/bin/bash

aws s3 cp s3://arxiv/src/$1 ./$1 --request-payer requester
tar xvf $1
