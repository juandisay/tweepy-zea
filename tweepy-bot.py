#!/usr/bin/env python 
# -*_ coding: utf-8 -*-

import tweepy, time, sys

argfile = str(sys.argv[1])

# Masukan informasi berdasarkan aplikasi twitter yang di buat

CONSUMER_KEY = 'AOKKBFq3rQ1KdzOtrd6jKQ'
CONSUMER_SECRET = 'YpFIWHfz13H6dkrLO8SF0l2rZkooBWlBLAMzlyOeVg0'
ACCESS_KEY = '166649152-kviqTRpj7xOjRkshVjdJN5kcCiP9RPdCngKSWqFz'
ACCESS_SECRET = 'auM52W2Boq2lonJnRebt3lnSGGWZnwS9V2znMJqYgOsJj'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

filename=open(argfile, 'r')
f=filename.readlines()
filename.close()

for line in f:
    api.update_status(line)
    time.sleep(900) # Tweet setiap 15 menit
