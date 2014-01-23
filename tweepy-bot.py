#!/usr/bin/env python 
# -*_ coding: utf-8 -*-

import tweepy, time, sys

argfile = str(sys.argv[1])

# Masukan informasi berdasarkan aplikasi twitter yang di buat (informasi ini rahasia!)

CONSUMER_KEY = 'AOKKBFq3r****************'
CONSUMER_SECRET = 'YpFIWHfz1************************************'
ACCESS_KEY = '166649152-kviq************************************'
ACCESS_SECRET = 'auM52W2Boq2************************************'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

filename=open(argfile, 'r')
f=filename.readlines()
filename.close()

for line in f:
    api.update_status(line)
    time.sleep(900) # Tweet setiap 15 menit
